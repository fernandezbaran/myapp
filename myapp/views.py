import requests
from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User
from .forms import FormResponseForm
from .models import FormResponse

def rojo_view(request):
    """Vista para mostrar el contenido de rojo.html."""
    return render(request, 'myapp/rojo.html')

def amarillo_view(request):
    """Vista para mostrar el contenido de amarillo.html."""
    return render(request, 'myapp/amarillo.html')

def form_view(request):
    # Check if the form has already been submitted
    if request.session.get('form_submitted', False):
        # Redirect to the appropriate page based on the last result
        last_result = request.session.get('last_result', '')
        if last_result == 'rojo':
            return redirect('rojo')
        elif last_result == 'amarillo':
            return redirect('amarillo')
        else:
            return redirect('/')  # Adjust according to your app's flow

    if request.method == 'POST':
        form = FormResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            data_to_send = {}
            if response.sangrado:
                data_to_send['Sangrado activo: '] = 'SI'
            if response.paralisis_facial:
                data_to_send['Paralisis facial: '] = 'SI'
            if response.debilidad_miembros:
                data_to_send['Debilidad en miembros: '] = 'SI'
            if response.alteraciones_equilibrio:
                data_to_send['Alteraciones del equilibrio: '] = 'SI'
            if response.alteraciones_visuales:
                data_to_send['Alteraciones visuales'] = 'SI'
            if response.dolor_torax:
                data_to_send['Dolor de torax: '] = 'SI'
            if response.dolor_abdominal:
                data_to_send['Dolor abdominal: '] = 'SI'
            if response.dolor_abdominal_mayor_50:
                data_to_send['Dolor abdominal mayor de 50: '] = 'SI'
            if data_to_send:
                data_to_send['NOMBRE: '] = response.nombre
                data_to_send['DNI: '] = response.dni
                data_to_send['MOTIVO DE CONSULTA: '] = response.motivo_de_consulta
                requests.post("https://ntfy.sh/triage", data=data_to_send)
                response.save()
            # Set the session data indicating success
                request.session['form_submitted'] = True
                request.session['last_result'] = 'rojo'
            # Redirect to 'rojo' page
                return redirect('rojo')
            else:
                request.session['form_submitted'] = True
                request.session['last_result'] = 'amarillo'
                return redirect('amarillo')
    else:
        form = FormResponseForm()

    return render(request, 'myapp/form.html', {'form': form})

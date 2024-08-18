from django import forms
from .models import FormResponse

class FormResponseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormResponseForm, self).__init__(*args, **kwargs)
        
        # Add help_text to each question field
        self.fields['nombre'].help_text = "Apellido y Nombre: "
        self.fields['dni'].help_text = "DNI:                "
        self.fields['motivo_de_consulta'].help_text = "Motivo de consulta: "
        self.fields['sangrado'].help_text = "Presenta heridas punzocortantes o sangrado activo de algun tipo: "
        self.fields['paralisis_facial'].help_text = "Caída o adormecimiento parcial o total de alguna parte del rostro: "
        self.fields['debilidad_miembros'].help_text = "Debilidad o adormecimiento en brazos o piernas: "

        self.fields['alteraciones_equilibrio'].help_text = "Problemas de equilibrio o inestabilidad de aparición súbita: "
        self.fields['alteraciones_visuales'].help_text = "Visión doble o perdida del la visión: "
        self.fields['dolor_torax'].help_text = "Dolor toraccico o dolor de pecho: "

        self.fields['dolor_abdominal'].help_text = "Dolor abdominal de intensidad mayor o igual a 7: "
        self.fields['dolor_abdominal_mayor_50'].help_text = "Es mayor de 50 años y presenta dolor abdominal de intensidad mayor o igual a 5: "

    class Meta:
        model = FormResponse
        fields = ['nombre', 'dni', 'motivo_de_consulta', 'sangrado', 'paralisis_facial', 'debilidad_miembros', 'alteraciones_equilibrio', 'alteraciones_visuales', 'dolor_torax', 'dolor_abdominal', 'dolor_abdominal_mayor_50']

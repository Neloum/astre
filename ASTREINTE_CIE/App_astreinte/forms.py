from django import forms
from .models import Pole, Direction, SousDirection, Site,ListeDePersonne

class PoleForm(forms.ModelForm):
    class Meta:
        model = Pole
        fields = ['lib_pole']



class SousDirectionForm(forms.ModelForm):
    class Meta:
        model = SousDirection
        fields = ['lib_sous_direc', 'direction']  # Assurez-vous que les champs sont bien ceux du modèle

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['lib_site']


class DirectionForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = ['nom_direc', 'e_mail_secre_direc', 'secre_direc', 'pole']



class ListeDePersonneForm(forms.ModelForm):
    excel_files = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': False}),
        label='Sélectionner des fichiers Excel',
        help_text='Les fichiers doivent être au format .xlsx',
        required=True
    )





# forms.py
from django import forms
from .models import UploadedFile

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file and not file.name.endswith('.xlsx'):
            raise forms.ValidationError("Seuls les fichiers .xlsx sont autorisés.")
        return file
    


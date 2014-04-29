from django.import forms
from models import File

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('fileName','desc','pub_date','file_to_upload')

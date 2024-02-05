from django import forms
from .models import mlist
class editmovie(forms.ModelForm):
    class Meta:
        model=mlist
        fields=['name','desc','mdesc','img']
from django import forms

from.models import Sample

# class Sampleinput(forms.ModelForm):  
#     model=Sampletest
#     fields='__all__'



class Sampleinput(forms.ModelForm):
    class Meta:
        model = Sample
        fields = '__all__'
        widgets={
            'samplename' : forms.TextInput(attrs={'class':'form-control'}),
            'sampledate' : forms.DateTimeInput(attrs={'class':'form-control'}),
            'samplelocation' : forms.TextInput(attrs={'class':'form-control'}),
        }
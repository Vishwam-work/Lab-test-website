from django import forms  
from adminapp.models import SampleTest  

class SampleAnalysis(forms.ModelForm):  
    class Meta:  
        model = SampleTest  
        fields = "__all__"  
       
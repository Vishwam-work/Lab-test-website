
from django import forms  
from adminapp.models import Admin_signup  
  
class Adminsignup(forms.ModelForm):  
    class Meta:  
        model = Admin_signup  
        fields = "__all__"  
        widgets={
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'firstname' : forms.TextInput(attrs={'class':'form-control'}),
            'lastname' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password' : forms.TextInput(attrs={'class':'form-control'})
        }
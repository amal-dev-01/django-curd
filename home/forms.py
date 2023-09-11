from django import forms
from .models import Employee


class EmpForm(forms.ModelForm):    
    class Meta:
        model = Employee
        fields=('fullname','emp_code','mobile','position') 
        
def __init__(self,*args, **kwargs):
        super(EmpForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label="select"
        self.fields['emp_code'].required=False
    
from django import forms
from ExpenseTracker.models import Exp

class stform(forms.ModelForm):
    class Meta:
        model=Exp
        fields=['des','amt','date','pay']
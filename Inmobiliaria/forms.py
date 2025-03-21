from django.utils import timezone
from django import forms
from .models import District, Owner, Property, State, City, TyprOwner,PropertyType ,TransactionType


class inmuebleForm(forms.ModelForm):
    class Meta:
        model = Property 
        fields = '__all__'

class DeptForm(forms.ModelForm):
    class Meta:
        model = State  
        fields = '__all__' 

class CityForm(forms.ModelForm):
    class Meta:
        model = City  
        fields = '__all__'   

class DisctictForm(forms.ModelForm):
    class Meta:
        model = District  
        fields = '__all__'   

class OwnerTyperForm(forms.ModelForm):
    class Meta:
        model = TyprOwner  
        fields = '__all__'   


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner  
        fields = '__all__'   

class PropertyTyperForm(forms.ModelForm):
    class Meta:
        model = PropertyType  
        fields = '__all__'   

class TransactionForm(forms.ModelForm):
    class Meta:
        model = TransactionType  
        fields = '__all__'   

class PropertyForm(forms.ModelForm):    
    class Meta:
        model = Property
        fields = '__all__'
        # Establecer valor predeterminado para publication_date
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Establecer publication_date a la fecha actual (solo si está vacío)
        if not self.instance.pk and not self.instance.publication_date:
            self.fields['publication_date'].initial = timezone.now().date()
        
        

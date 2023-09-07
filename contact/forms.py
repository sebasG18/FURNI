from django import forms 

class ContactForm(forms.Form):
    name=forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), min_length=3, max_length=100)
    lastname=forms.CharField(label="Apellido", required=True, widget=forms.TextInput(
        attrs={'class':'form-control'}
    ), min_length=3, max_length=100 )
    email=forms.CharField(label="Correo", required=True, widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    message=forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(
        attrs={'class':'form-control'}
    ), min_length=10, max_length=1000)
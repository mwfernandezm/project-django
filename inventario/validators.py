from django.core.exceptions import ValidationError

def solo_texto(value):
    if not value.isalpha():
        raise ValidationError(
            'El campo solo admite letras',
            params={'value': value},
        )

def maxima_cantidad(value):
    if not ((value > 0) and (value <= 100)):
        raise ValidationError(
            'Ingrese un numero Entero entre 1 y 100',
            params={'value': value},
        )
    
      

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate
from trabajador.modelos.trabajadores import Trabajador
from bootstrap_modal_forms.forms import BSModalForm
from trabajador.formularios.utils import especialidad_choices
from trabajador.modelos.nomencladores import Especialidad




class DateInput(forms.DateInput):
    input_type = 'date'


class FormAutenticacion(AuthenticationForm):
    username  = forms.CharField(min_length=1, label='Usuario', widget=forms.TextInput())
    password  = forms.CharField(min_length=1, label='Contraseña', widget=forms.PasswordInput(render_value=True))
    error_messages = {
        'invalid_login':"No se reconoce la combinación de nombre de usuario y contraseña."
                           "Note que ambos campos pueden ser sensibles a las mayúsculas.", 
        'inactive': "Su cuenta está inactiva. Póngase en contacto con el administrador para activarla.",        
    }
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                try:
                    user_temp = User.objects.get(username=username)
                except:
                    user_temp = None

                if user_temp is not None:
                    if user_temp.is_active:
                        raise forms.ValidationError(
                            self.error_messages['invalid_login'],
                            code='invalid_login',
                            params={'username': self.username_field.verbose_name},
                        )
                    else:
                        try:
                            #print(self.user_cache)
                            self.confirm_login_allowed(user_temp)
                        except:
                            raise forms.ValidationError(
                                self.error_messages['inactive'],
                                code='inactive',
                                params={'username': self.username_field.verbose_name},
                            )
                else:
                    try:
                        self.confirm_login_allowed(user_temp)
                    except:
                        raise forms.ValidationError(
                            self.error_messages['invalid_login'],
                            code='invalid_login',
                            params={'username': self.username_field.verbose_name},
                        )

        return self.cleaned_data


class FormRegistrarUsuario(UserCreationForm):
    username = forms.CharField(min_length=1, label='Usuario', widget=forms.TextInput())
    password1  = forms.CharField(min_length=1, label='Contraseña', widget=forms.PasswordInput(render_value=True))
    password2  = forms.CharField(min_length=1, label='Repetir contraseña', widget=forms.PasswordInput(render_value=True))
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
   
    # Validar que los passwords coincidan
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2


class FormRegistrarTrabajador(forms.ModelForm):
    especialidad = forms.ChoiceField(choices=[])

    class Meta:
        model = Trabajador
        exclude = ['usuario']
        labels = {
            'apellido1': 'Primer apellido',
            'apellido2': 'Segundo apellido',
        }
        widgets = {
            'tarjeta': forms.TextInput,
            'res_34_19': forms.TextInput,
            'fecha_entrada_insmet': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(FormRegistrarTrabajador, self).__init__(*args, **kwargs)
        self.fields['especialidad'].choices = especialidad_choices()

    def clean_especialidad(self):
        return Especialidad.objects.get(pk=self.cleaned_data.get("especialidad"))


class FormAppUser(BSModalForm):
    class Meta:
        model = Trabajador
        fields = '__all__'
        

    

from django.contrib.auth import authenticate
from users.models import User
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(forms.ModelForm):

    """
    A Custom form that creates a user, with no privileges, from the given email and
    password.
    """
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


# region UserCreationForm
# ---------- OR -------------
# class UserRegistrationForm(UserCreationForm):
#   '''
#   here i extend the Builtin UserCreationForm and override just the Meta class
#   To use the email field instead of the username
#   '''
#     class Meta:
#         model= User
#         fields = ('email',)
# endregion

class LoginForm(forms.Form):
    '''
    Login a user from the given email and password.
    '''

    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=120, widget=forms.PasswordInput())

    def __init__(self, request=None, **kwargs):
        super().__init__(**kwargs)
        self.request = request # to be able to use authenticate function here 
        self.user = None  # authenticated user will be stored here

    def clean(self):
        '''
        1. Checks if email belongs to a user
        2. Tries to authenticate a user if it's found otherwise raises an error
        '''
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if not User.objects.filter(email=email).exists():
            # Raise error if no user matches this email
            raise forms.ValidationError(_('Invalid email.'))
    
        user = authenticate(request=self.request, email=email, password=password)
        if not user:
            raise forms.ValidationError(_('Invalid credintials'))
        self.user = user
        return self.cleaned_data


    def confirm_login_allowed(self):
        '''
        Checks if a user is_active or not before login
        '''
        if not self.user.is_active:
            raise forms.ValidationError(_('This user has been deactivated.'))
        return None

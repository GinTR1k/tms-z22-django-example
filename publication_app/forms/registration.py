from django.contrib.auth.models import User
from django.forms import ModelForm

from publication_app.models import Profile


class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        # exclude = ('is_superuser', 'is_staff')
        # fields = '__all__'

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user

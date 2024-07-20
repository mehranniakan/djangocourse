from allauth.account.forms import SignupForm
from django import forms


class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)

    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        # Add your own processing here.

        # You must return the original result.
        return user

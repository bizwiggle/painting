from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from auth.models import MyUser

class MyUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(MyUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = MyUser
        fields = ("email",)

class MyUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(MyUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = MyUser


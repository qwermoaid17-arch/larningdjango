from django import forms

#larning :
# label
# initial
#disabled
#help_text
#widget
#required
class login_form(forms.Form):

    username = forms.CharField(max_length=100, label='Username',initial='user', help_text="enter the user name", required=True )
    password = forms.CharField(max_length=100, label='Password', disabled=True ,widget=forms.PasswordInput )
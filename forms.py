from django import forms

class Reviewform(forms.Form):
    first_name = forms.CharField(label='First Name',max_length=100)
    last_name = forms.CharField(label ='Last Name',max_length=100)
    emmail = forms.EmailField(label='Email')
    review = forms.CharField(label='Please write your review here')
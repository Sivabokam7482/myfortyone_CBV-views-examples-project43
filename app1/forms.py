from django import forms

class studentform(forms.Form):
    Name=forms.CharField(max_length=100)
    Age=forms.IntegerField()
    Email=forms.EmailField(max_length=464)
from django import forms
from .models import Post
from draceditor.fields import DraceditorFormField

class PostFormDrace(forms.Form):
    title = forms.CharField(widget=forms.TextInput())
    content = DraceditorFormField()

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

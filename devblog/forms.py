from django import forms
from .models import Post
from draceditor.fields import DraceditorFormField

class PostFormDrace(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput())
    content = DraceditorFormField()

    class Meta:
        model = Post
        fields = ('title', 'content')

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

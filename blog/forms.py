from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model=Post
        #fileds=('title','text',)
        #fields='__all__'
        fields=('title','text',)
        
        
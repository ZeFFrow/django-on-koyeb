from django import forms
from .models import *


    

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    body = forms.CharField(max_length=245, label="Item Description.")

    class Meta:
        model = Article
        fields = ('title', 'body', )
 
 
class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    # class Meta:
    #     model = Images
    #     fields = ('image',)
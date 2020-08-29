from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'status', 'categoria')

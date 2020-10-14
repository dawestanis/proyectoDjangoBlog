from django.contrib.auth.forms import UserCreationForm
from django.forms import forms, ModelForm, TextInput, Select, ImageField, FileInput, Textarea

from blog_app.models import Post, Usuario


class PostForm(ModelForm):
    """
    Formulario para crear un post.
    """

    class Meta:
        model = Post
        fields = ('titulo', 'descripcion', 'contenido', 'categoria', 'image')
        widgets = {
            'titulo': TextInput(attrs={'class': 'form-control'}),
            'descripcion': TextInput(attrs={'class': 'form-control'}),
            'contenido': Textarea(),
            'categoria': Select(attrs={'class': 'form-control'}),
            'image': FileInput(attrs={'class': 'form-control-file', 'accept': 'image/*'}),
        }


class CrearUsuarioForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ["username", "password1", "password2"]
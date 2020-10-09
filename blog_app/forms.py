from django.forms import ModelForm, TextInput, Select, ImageField, FileInput, Textarea

from blog_app.models import Post


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

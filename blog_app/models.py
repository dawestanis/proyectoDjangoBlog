from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Usuario(AbstractUser):
    pass


class Categoria(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categorias"


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=125)
    fecha = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria, related_name='post_category',
                                  on_delete=models.CASCADE, default=1)
    image = models.ImageField("Image", blank=True, null=True, upload_to="media/post/imagenes")

    def __str__(self):
        return self.title + ' | ' + str(self.author)


class Comentario(models.Model):
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='post_comentario',
                             on_delete=models.CASCADE, default=1)

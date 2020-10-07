from django.contrib import admin

# Register your models here.
from blog_app.models import Usuario, Post, Categoria

admin.site.register(Post)
admin.site.register(Usuario)
admin.site.register(Categoria)
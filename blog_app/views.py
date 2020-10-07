from django.shortcuts import render
from django.views import View

from blog_app.models import Post


class index(View):

    def get(self, request):
        lista_post = Post.objects.all()
        return render(request, "index.html", {"lista": lista_post})

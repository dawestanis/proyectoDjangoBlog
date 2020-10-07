from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from blog_app.models import Post


class index(View):

    def get(self, request):
        lista_post = Post.objects.all()
        paginator = Paginator(lista_post, 1)  # Muestra 5 post por pagina.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, "index.html", {"page_obj": page_obj})

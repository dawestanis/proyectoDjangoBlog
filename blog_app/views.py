from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from blog_app.forms import PostForm
from blog_app.models import Post


class index(View):

    def get(self, request,**kwargs):
        lista_post = Post.objects.all()
        paginator = Paginator(lista_post, 5)  # Muestra 5 post por pagina.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, "index.html", {"page_obj": page_obj})


class CrearPostView(View):

    def get(self, request):
        post = PostForm()

        return render(request, "crearpost.html", {"form": post})

    def post(self, request):
        # Obtenemos el formulario con los datos del POST
        post_form = PostForm(request.POST, request.FILES)
        try:
            if post_form.is_valid():
                # Guardamos el post en memoria para asignarle luego el autor
                post = post_form.save(commit=False)
                # Asignamos el autor al usuario que manda la peticion
                post.autor = request.user
                # Guardamos en la base de datos
                post.save()

                # Vamos al index
                return HttpResponseRedirect(reverse_lazy('index'))


        except Exception as e:
            print(e)

        return render(request, "crearpost.html", {"form": post_form})

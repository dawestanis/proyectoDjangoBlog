from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View, generic
from blog_app.forms import PostForm, CrearUsuarioForm
from blog_app.mixin import AdminStaffRequiredMixin
from blog_app.models import Post, Categoria


class index(View):

    def get(self, request, **kwargs):
        # Post
        if 'categoria' in request.GET:
            lista_post = Post.objects.filter(categoria=Categoria.objects.get(pk=request.GET.get('categoria')))
        else:
            lista_post = Post.objects.all()

        paginator = Paginator(lista_post, 6)  # Muestra 6 post por pagina.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # Categorias
        lista_categorias = Categoria.objects.all()
        return render(request, "index.html", {
            "page_obj": page_obj,
            "lista_categorias": lista_categorias,
        })


# hay que poner el login required (solo los usuarios logeados)
class CrearPostView(AdminStaffRequiredMixin, View):
    # Crear los permisos de creacion de post (revisar)
    login_url = reverse_lazy('login')

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


# Debo crear un metodo que devuelva las categorias.

class UserRegisterView(generic.CreateView):
    form_class = CrearUsuarioForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(UserRegisterView, self).dispatch(request, *args, **kwargs)


class DetallesPostView(View):
    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            return render(request, "detalles_post.html", {"post": post})
        except Exception as e:
            print(e)
            return redirect('index')

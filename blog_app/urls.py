from django.urls import path
from .views import UserRegisterView, DetallesPostView, CrearPostView, index

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('registrar', UserRegisterView.as_view(), name='register'),
    path('post/crear', CrearPostView.as_view(), name='post-crear'),
    path('post/detalles/<int:pk>', DetallesPostView.as_view(), name='post-detalle'),
]

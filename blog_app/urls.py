from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('post/crear', views.CrearPostView.as_view(), name='post-crear'),

]

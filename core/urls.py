from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('animais/', views.animal_list, name='animal_list'),
    path('animais/novo/', views.animal_create, name='animal_create'),
    path('animais/<int:pk>/editar/', views.animal_edit, name='animal_edit'),
    path('animais/<int:pk>/excluir/', views.animal_delete, name='animal_delete'),
    path('animais/<int:pk>/foto/excluir/', views.animal_foto_delete, name='animal_foto_delete'),
    path('animais/<int:animal_pk>/imagens/<int:image_pk>/excluir/', views.animal_image_delete, name='animal_image_delete'),
    path('adotantes/', views.adotante_list, name='adotante_list'),
    path('adotantes/novo/', views.adotante_create, name='adotante_create'),
    path('adotantes/<int:pk>/editar/', views.adotante_edit, name='adotante_edit'),
    path('adotantes/<int:pk>/excluir/', views.adotante_delete, name='adotante_delete'),
]

from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:contato_id>', views.ver_contato, name = 'ver_contato')
]
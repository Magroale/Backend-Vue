from django.urls import re_path
from infoViajes import views

urlpatterns =[
    re_path(r'home_page', views.home_page),
    re_path(r'home_page/([0-9]+)$', views.home_page),
    re_path(r'vista_comentario', views.vista_comentario),
    re_path(r'vista_comentario/([0-9]+)$', views.vista_comentario)
]
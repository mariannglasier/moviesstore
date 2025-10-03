from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='petitions.index'),
    path('<int:petition_id>/edit/', views.edit_petition, name='petitions.edit_petition'),
    path('<int:petition_id>/delete/', views.delete_petition, name='petitions.delete_petition'),
    path('create/', views.create_petition, name='petitions.create_petition'),
    path('<int:petition_id>/vote/', views.vote_petition, name='petitions.vote_petition'),
]
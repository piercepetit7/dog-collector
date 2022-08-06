from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('dogs/', views.dogs_index, name='dogs_index'),
  path('dogs/<int:dog_id>/', views.dogs_detail, name='dogs_detail'),
  path('dogs/create/', views.dogCreate.as_view(), name="dogs_create"),
  path('dogs/<int:pk>/update/', views.dogUpdate.as_view(), name='dogs_update'),
  path('dogs/<int:pk>/delete/', views.dogDelete.as_view(), name='dogs_delete'),
  path('dogs/<int:dog_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/', views.ToyList.as_view(), name='toys_index'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
  path('dogs/<int:dog_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
  path('accounts/signup/', views.signup, name='signup')
]
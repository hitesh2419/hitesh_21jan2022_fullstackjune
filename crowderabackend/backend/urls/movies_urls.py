from django.urls import path
from backend.views import movies_views as views

urlpatterns=[
     path('', views.GetMovies.as_view()),
     path('create/',views.CreateMovies.as_view()),
     path('<str:pk>/', views.getMovies.as_view()),
]
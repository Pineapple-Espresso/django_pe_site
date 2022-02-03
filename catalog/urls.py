from django.urls import path
from . import views

urlpatterns = [
    path('',views.CoffeeListView.as_view()),
]
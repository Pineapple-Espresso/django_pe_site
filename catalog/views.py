from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

# Create your views here.
from .models import coffee_stock


class CoffeeListView(generic.ListView):
    model = coffee_stock
        
            


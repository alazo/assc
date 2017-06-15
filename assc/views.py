from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import F, Sum

from .models import Domain  
# Create your views here.

class HomeFEView(ListView):
    model = Domain
    template_name = 'assc/index_fe.html'
        
class HomeMPView(ListView):
    model = Domain
    template_name = 'assc/index_mp.html'
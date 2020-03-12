from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Participant, Interview
from .forms import ParticipantForm

"""
def home(request):
    return HttpResponse('Hello, World!')

def create(request):
    return render(request,'creation.html')
"""

class ParticipantListView(ListView):
    model = Participant
    context_object_name = 'participant'

class ParticipantCreateView(CreateView):
    model = Interview
    fields = ('participant', 'date_Start', 'date_End')
    success_url = reverse_lazy('interview_changelist')

class PartivipantUpdateView(UpdateView):
    model = Interview
    fields = ('participant', 'date_Start', 'date_End')
    success_url = reverse_lazy('interview_changelist')

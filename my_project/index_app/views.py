from django.shortcuts import render
from django.http import HttpResponse
# import logging

# logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'index_app/index.html')


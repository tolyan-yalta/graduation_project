from django.shortcuts import render
from django.http import HttpResponse
# import logging

# logger = logging.getLogger(__name__)


def index(request):
    html = """
    <h1>Главная страница.</h1>
    <p>Это главная страница дипломного проекта.</p>
    """
    # logger.info("The main page has been loaded.")
    return HttpResponse(html)

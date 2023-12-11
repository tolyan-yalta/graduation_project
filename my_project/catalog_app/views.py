from django.shortcuts import render
from django.http import HttpResponse
# import logging

# logger = logging.getLogger(__name__)


def catalog(request):
    html = """
    <h1>Страница каталога.</h1>
    <p>Это страница каталога проекта.</p>
    """
    # logger.info("The catalog page has been uploaded.")
    # return render(request, 'catalog_app/catalog.html')
    return HttpResponse(html)

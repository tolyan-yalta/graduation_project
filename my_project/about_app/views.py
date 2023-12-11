from django.shortcuts import render
from django.http import HttpResponse
# import logging

# logger = logging.getLogger(__name__)


def about(request):
    html = """
    <h1>Страница "О нас".</h1>
    <p>Это страница проекта "О нас".</p>
    """
    # logger.info("The about page has been uploaded.")
    # return render(request, 'about_app/about.html')
    return HttpResponse(html)


def contacts(request):
    html = """
    <h1>Страница "Контакты".</h1>
    <p>Это страница проекта "Контакты".</p>
    """
    # logger.info("The contacts page has been uploaded.")
    # return render(request, 'about_app/contacts.html')
    return HttpResponse(html)

def gallery(request):
    html = """
    <h1>Страница "Галерея".</h1>
    <p>Это страница проекта "Галерея".</p>
    """
    # logger.info("The gallery page has been uploaded.")
    # return render(request, 'about_app/gallery.html')
    return HttpResponse(html)
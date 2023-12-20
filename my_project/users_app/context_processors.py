from index_app.menu import menu

def get_menu_context(request):
    return {'mainmenu': menu}

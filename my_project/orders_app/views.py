from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from basket_app.basket import Basket

from django.template.loader import get_template
from xhtml2pdf import pisa
from xhtml2pdf.files import pisaFileObject
from django.http import HttpResponse

from .tasks import order_created


def order_create(request):
    basket = Basket(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in basket:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            
            context = {
                'order_id': f"{order.id}",
                'first_name': order.first_name,
                'last_name': order.last_name,
                'email': order.email,
                'address': order.address,
                'postal_code': order.postal_code,
                'city': order.city,
                'created': order.created,
                'items': basket,
            }
            # Получаем шаблон по указанному адресу
            template = get_template("orders_app/order/invoice.html")
            # Передаем в него какие-либо данные
            html  = template.render(context)
            pisaFileObject.getNamedFile = lambda self: self.uri
            # Формируем имя для конечного файла
            filename = f"Order_{order.id}.pdf"

            with open(f"../my_project/orders_app/static/pdf/{filename}", "w+b") as file:
                pdf_status = pisa.CreatePDF(html, dest=file, encoding="utf-8")
                if pdf_status.err:
                    return HttpResponse("Invalid PDF", status_code=400, content_type='text/plain')
            # применяем декорированную функцию
            email = order_created(order)
            # добавляем к 'email' файл PDF
            email.attach_file(f"../my_project/orders_app/static/pdf/{filename}")
            # отправляем почту
            email.send(fail_silently=True)
            # очистка корзины
            basket.clear()
            return render(request, 'orders_app/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders_app/order/create.html',
                  {'basket': basket, 'form': form})

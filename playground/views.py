from django.shortcuts import render
from django.core.mail import send_mail,BadHeaderError
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customer
# def say_hello(request):
#     # try:
#     send_mail('subject','message','shahil@gmail.com',['shahil2213@gmail.com'])
#     # except BadHeaderError:
#     #     pass  
#     return render(request, 'hello.html', {'name': 'Shahil'})



def say_hello(request):
    try:
       message = BaseEmailMessage(
           template_name='email/hello.html',
           context={'name': 'Shahil Khan'}
       )
       message.send(['shahil@gmail.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Shahil Khan'})


def cellerys(request):
    notify_customer.delay('hello')
    return render(request, 'celery.html')
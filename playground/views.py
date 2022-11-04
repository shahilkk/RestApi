from django.shortcuts import render
from django.core.cache import cache
from django.core.mail import send_mail,BadHeaderError
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customer
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
import requests

# def say_hello(request):
#     # try:
#     send_mail('subject','message','shahil@gmail.com',['shahil2213@gmail.com'])
#     # except BadHeaderError:
#     #     pass  
#     return render(request, 'hello.html', {'name': 'Shahil'})



# def say_hello(request):
#     try:
#        message = BaseEmailMessage(
#            template_name='email/hello.html',
#            context={'name': 'Shahil Khan'}
#        )
#        message.send(['shahil@gmail.com'])
#     except BadHeaderError:
#         pass
#     return render(request, 'hello.html', {'name': 'Shahil Khan'})


def cellerys(request):
    notify_customer.delay('hello')
    return render(request, 'celery.html')

# def say_hello(request):
#     key = 'httpbin_result'
#     if cache.get(key) is None:
#         # to delay 2sec
#         response = requests.get('https://httpbin.org/delay/2')
#         data = response.json()
#         cache.set(key,data,)
#     return render(request, 'hello.html', {'name': cache.get(key)})    






# @cache_page(5*60)
# def say_hello(request):
#     # to delay 2sec
#     response = requests.get('https://httpbin.org/delay/2')
#     data = response.json()
#     return render(request, 'hello.html', {'name': data})        

class HelloView(APIView):
    @method_decorator(cache_page(5*60))
    def get(self,request):
        response = requests.get('https://httpbin.org/delay/2')
        data = response.json()
        return render(request, 'hello.html', {'name': data})    



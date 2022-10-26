from time import sleep
from storefront.celery import celery




@celery.task
def notify_customer(message):
    print('sent 10k message')
    print(message)
    sleep(10)
    print('Email sented Succesfully!')
from django.http import HttpResponse
import paypalrestsdk
from paypalrestsdk import CreditCard


def payment(request):
    paypalrestsdk.configure({
        "mode": "sandbox",  # Cambia a "live" para producción
        "client_id": "AcZ95z3lENZzGD9ZU9rdwaQhxTpJDtCIoVlBWOWD-8xRlsNF2HtHtHBcFCgjG_sR2wNdZob1mKMrL0PW7k",
        "client_secret": "ECWcvObHa23d1PDd6o2_Nf9wyY1NNQigdXLB-K9rWHMczdzjVHq9awyK4xteD7Ve0j_o4ERsDuxI2r5F"
    })
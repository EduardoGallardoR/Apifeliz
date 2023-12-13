from django.shortcuts import render, redirect
from rest_framework.views import APIView
from api.models import Usuario
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.core.mail import send_mail


# Create your views here.
class Home (APIView):
    template_name="login.html"
    def get(self,request):
        return render(request,self.template_name)
class cancel (APIView):
    template_name="cancel.html"
    def get(self,request):
        return render(request,self.template_name)
class success (APIView):
    template_name="success.html"
    def get(self,request):
        return render(request,self.template_name)

class Inicio (APIView):
    template_name="index.html"
    def get(self,request):
        return render(request,self.template_name)
class power (APIView):
    template_name="dashboard.html"
    def get(self,request):
        return render(request,self.template_name)

    
class Listing (APIView):
    template_name="listing.html"
    def get(self,request):
        return render(request,self.template_name)
    
class Pag2 (APIView):
    template_name="pag2.html"
    def get(self,request):
        return render(request,self.template_name)

class Pag3 (APIView):
    template_name="pag3.html"
    def get(self,request):
        return render(request,self.template_name)


         
def registro (request):
    if request.method=='POST':
        nombre = request.POST.get('name')
        apellido = request.POST.get('ape')
        correo = request.POST.get('email')
        contraseña = request.POST.get('pass')

        # Verificar si el correo ya está registrado
        if Usuario.objects.filter(correou=correo).exists():
            messages.error(request, 'El correo ya está registrado')
            return render(request, 'registro.html')
        else:
        # Crear un nuevo objeto Usuario y guardarlo en la base de datos
            usuario_nuevo = Usuario(nombreu=nombre, apellidou=apellido, correou=correo, contraseñau=contraseña)
            usuario_nuevo.save()

        # Mostrar mensaje de éxito
        messages.success(request, 'Usuario registrado exitosamente')

        # Redirigir a la página de registro (o a donde desees)
        return render(request, 'registro.html')
    else:
        # Si la solicitud no es POST, simplemente renderiza la página de registro
        return render(request, 'registro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('emailForm')
        passPa = request.POST.get('passForm')

        try:
            user = Usuario.objects.get(correou=email, contraseñau=passPa)
            request.session['correou'] = user.correou

            return redirect('index')
        except Usuario.DoesNotExist:
            messages.error(request, 'User does not exist!')
        except Usuario.MultipleObjectsReturned:
            messages.error(request, 'Multiples users with the same name!')

    return render(request, 'login.html')

def form_verificado(request):
    if request.method == 'POST':
        nombre = request.POST['name']
        apellido = request.POST['ape']
        correo = request.POST['email']
        contraseña = request.POST['passForm']

        if Usuario.objects.filter(correou=correo).exists():
            messages.error(request, 'El correo ya está registrado')
            return render(request, 'registro.html')
        else:
            Usuario(nombreu=nombre, apellidou=apellido, correou=correo, contraseñau=contraseña).save()
            messages.success(request, 'Usuario registrado exitosamente')
            subject = 'Verficación del correo!'
            message = f"'!Gracias por unirte a nuestra página. Por favor haz click en el siguiente enlace para verificar tu correo! "
            from_email = "legara821@gmail.com"
            send_mail(subject, message, from_email, [correo])
            messages.success(request, "Usuario registrado correctamente, Por favor verifica tu correo!")
            return render(request, 'registro.html')
    else:
        return render(request, 'registro.html')
        
from django.shortcuts import render

from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid 

def CheckOut(request):

    

    host = request.get_host()

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '1',
        'item_name': 'Inflafeliz',
        'invoice': uuid.uuid4(),
        'currency_code': 'MXN',
        'return_url': "http://127.0.0.1:8000/payment/",
        'return_url': "http://127.0.0.1:8000/success/",
        'cancel_url': "http://127.0.0.1:8000/cancel/"
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    context = {
        'product': '1',
        'paypal': paypal_payment
    }
    return render(request,'pago.html', context)
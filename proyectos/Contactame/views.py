from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactoForm

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Guardar el formulario
            contacto = form.save()

            # Enviar el correo al usuario
            subject = 'Gracias por tu mensaje'
            message = f'Hola {contacto.nombre},\n\nGracias por contactarnos. Hemos recibido tu mensaje:\n\n"{contacto.mensaje}"\n\nNos pondremos en contacto contigo pronto.'
            from_email = settings.EMAIL_HOST_USER  # Usar el correo configurado en settings.py
            recipient_list = [contacto.email]  # Enviar el correo a la dirección ingresada

            # Enviar el correo al usuario
            send_mail(subject, message, from_email, recipient_list)
            return redirect('gracias')  # Redirige a la vista 'gracias'
    else:
        form = ContactoForm()

    return render(request, 'contactame/contacto.html', {'form': form})

def gracias_view(request):
    return render(request, 'contactame/gracias.html')

# Create your views here.

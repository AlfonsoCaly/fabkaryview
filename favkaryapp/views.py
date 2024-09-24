from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string
from .forms import ContactForm
from email.mime.image import MIMEImage


def index(request):
    return render(request, 'favkaryapp/index.html')

def portfolio(request):
    return render(request, 'favkaryapp/Portfolio.html')

def weddings(request):
    return render(request, 'favkaryapp/weddings.html')

def lifestyle(request):
    return render(request, 'favkaryapp/lifestyle.html')

def family(request):
    return render(request, 'favkaryapp/family.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extraer la información del formulario
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Incluir el correo del usuario en el cuerpo del mensaje
            full_message = f"Message from: {email}\n\n{message}"

            # Crear el mensaje usando EmailMessage para enviar al administrador
            email_message = EmailMessage(
                subject=f"Contact Form: {subject}",
                body=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.DEFAULT_FROM_EMAIL],
                reply_to=[email]
            )

            # Enviar el correo al administrador
            email_message.send(fail_silently=False)

            # Generar el contenido HTML usando la plantilla
            html_content = render_to_string('favkaryapp/email_confirmation.html', {
                'subject': subject,
                'message': message
            })

            # Crear el correo de confirmación al usuario con HTML
            confirmation_email = EmailMessage(
                subject="Thank you for contacting Fab Kary View!",
                body=html_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email]
            )
            confirmation_email.content_subtype = "html"  # Esto indica que el contenido es HTML

            # Adjuntar la imagen con un Content-ID (CID) usando MIMEImage
            logo_path = 'favkaryapp/static/img/logomail.png'  # Cambia esto a la ruta de tu imagen
            with open(logo_path, 'rb') as img:
                mime_image = MIMEImage(img.read())
                mime_image.add_header('Content-ID', '<logo_image>')
                confirmation_email.attach(mime_image)

            # Enviar el correo al usuario
            confirmation_email.send(fail_silently=False)

            # Mostrar mensaje de éxito
            messages.success(request, 'Your message has been sent successfully! A confirmation email has been sent to you.')
            form = ContactForm()  # Limpiar el formulario después de enviarlo
    else:
        form = ContactForm()

    return render(request, 'favkaryapp/contact.html', {'form': form})

from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage


def contact(request):
    send = False

    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        email = EmailMessage(
            'Mensagem do Blog Django',
            'De {} <{}> Escreveu: \n\n{}'.format(name, email, message),
            'não-responder@inbox.mailtrap.io',
            ['brenosouza49@gmail.com'],
            reply_to=[email]
        )
        try:
            email.send()
            send = True
        except:
            send = False

    context = {
        'form': ContactForm,
        'sucess': send
    }
    return render(request, 'contato/contact.html', context)

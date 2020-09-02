from django.shortcuts import render


def contact(request):
    send = False

    ''' form = ContactForm(request.POST or None)
     if form.is_valid():
         send = True
    
     context = {
         'form': ContactForm,
         'sucess': send
     }'''
    return render(request, 'contato/contact.html')

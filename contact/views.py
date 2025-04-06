from django.contrib.messages.api import success
from django.shortcuts import render
from contact.forms import ContactForm
# Create your views here.
def contact(request):
    form = ContactForm(request.POST or None)
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            context = {'name': form.cleaned_data['name'],'success': success}
            return  render(request, 'contact/contact.html', context)
    return render(request, 'contact/contact.html', {'form': form, 'success': success})




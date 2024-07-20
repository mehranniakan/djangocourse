from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
import json
from website.forms import ContactForm, NewsLetterForm
from website.models import Contact, news_letter


# Create your views here.

def index_page(request):
    return render(request, "web/index.html")


def about_page(request):
    return render(request, "web/about.html")


def contact_us(request):
    contact_form = ContactForm(request)
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            # if not bool(contact_form.data.get('Subject')):
            #     contact_form.instance.Subject = None
            contact_form.instance.Name = "Unknown"
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, "You're Request has Successfuly Submitted !")
        else:
            print(contact_form.errors)
            messages.add_message(request, messages.ERROR, "You're Request has not Submitted !")
    elif request.method == 'GET':
        print('Get Method')
    else:
        print('Invalid Method')
    return render(request, "web/contact.html", {'form': contact_form})


def Under_Maintenance(request):
    return render(request, 'web/under_maintenance.html')


def News_letter(request):

    form = None
    if request.method == 'POST':

        form = NewsLetterForm(request.POST)

        if form.is_valid():
            print('here')
            check_duplicate = news_letter.objects.filter(Email=form.cleaned_data['Email']).count()
            if check_duplicate == 0:
                form.save()
            else:
                messages.add_message(request, messages.ERROR, "Your Email previously Submited")

        else:
            print(form.errors)

    return render(request, 'web/index.html', {'form': form})

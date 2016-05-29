from django.shortcuts import render
from .forms import EmailForm
from .models import Main

# Create your views here.


def get_ip(request):
    ''' Fetch and store user IP address '''
    try:
        x_forwad = request.META.get("HTTP_X_FOWARDED_FOR")
        if x_forwad:
            ip = x_forwad.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip


def home(request):
    ''' A function that handles the learnmore submit button on homepage'''
    form = EmailForm(request.POST or None)
    if form.is_valid():
        view = form.save(commit=False)
        email = form.cleaned_data['email']
        view, created = Main.objects.get_or_create(email=email)
        if created:
            view.ip_address = get_ip(request)
            view.save()
    context = {"form": form}
    template = "home.html"
    return render(request, template, context)

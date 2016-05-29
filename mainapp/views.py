from django.shortcuts import render
from .forms import EmailForm
from .models import Main
# Create your views here.


def home(request):
    # form = EmailForm(request.POST or None)
    # if form.is_valid():
    #     view = form.save(commit=False)
    #     email = form.cleaned_data['email']
    #     view, created = Main.objects.get_or_create(email=email)
    #     view.save()
    form = EmailForm(request.POST or None)
    if form.is_valid():
        view = form.save(commit=False)
        email = form.cleaned_data['email']
        view, created = Main.objects.get_or_create(email=email)

    context = {"form": form}
    template = "home.html"
    return render(request, template, context)

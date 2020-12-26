from django.shortcuts import render
import random

# Create your views here.


def homepage(request):
    return render(request, 'homepage.html')


def generate_password(request):
    pw_length = int(request.GET.get('password_length'))
    choices = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('UpperCase'):
        choices += list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('Numbers'):
        choices += list('0123456789')
    if request.GET.get('Special'):
        choices += list('~!@#$%^&*()_+=-')

    gen_password = ''
    for ind in range(pw_length):
        gen_password += random.choices(choices)[0]

    return render(request, 'generated_password.html', {"gen_password": gen_password})


def about(request):
    return render(request, 'about.html')


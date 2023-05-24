from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_dj

# Create your views here.


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=nome).first()

        if user:
            return HttpResponse('Já existe um usuário com esse nome')

        user = User.objects.create_user(username=nome, first_name=nome, email=email, password=senha)
        user.save()

        return HttpResponse('Usuário cadastrado com sucesso')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        user = authenticate(username=nome, password=senha)
        if user:
            login_dj(request, user)
            return HttpResponse('Autenticado')
        else:
            return HttpResponse('Email ou senha inválidos'), href


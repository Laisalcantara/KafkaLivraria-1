from django.shortcuts import render

# Create your views here.

def home(request): #Função para chamar a home
    return render(request,
     'Kafka\home.html')

def ebook(request): #Função para chamar a página ebook
    return render(request,
     'Kafka\ebook.html')
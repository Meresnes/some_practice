from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'homePage.html')

def contact(request):
    return render(request,'basic.html',{'values':['Если у вас остались вопросы, то задавайте из по телефону','8-911-222-55-12']})

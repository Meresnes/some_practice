# from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def reverse(request):
    user_text = request.GET['usertext']
    words_len = len(user_text.split())
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html', {'words': words_len,
                                            'user_text': user_text,
                                           'reversed_text': reversed_text})
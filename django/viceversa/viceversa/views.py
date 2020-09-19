# from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def reverse(request):
    user_text = request.GET['usertext']
    words_len = 0
    k = 0
    for i in user_text:
        if i == ' ':
            words_len += 1
        k += 1
    if words_len > 0:
        words_len += 1
    elif k > 0:
        words_len = 1
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html', {'words': words_len,
                                            'user_text': user_text,
                                           'reversed_text': reversed_text})
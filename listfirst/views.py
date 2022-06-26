from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   # return HttpResponse("<h1>Home</h1>")
    p={'name':'hello','gre':'good afternoon'}
    return render(request,'index.html',p)

def analyze(request):
    #get the text value from user
    djtext=request.GET.get('text','default')
    #check the value of checkbox
    removepunc=request.GET.get('removepunc','off')

    # we will create punctuation list and write code to remove it
    result_text = ""
    pun='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    if removepunc=='off':
        result_text=djtext
    else:
        for char in djtext:
            if char not in pun:
                result_text=result_text + char

    #created dict to store the value
    dict={'purpose':'removed punctuations','result':result_text}

    #it will render the analyzer.html
    return render(request,'analyze.html',dict)

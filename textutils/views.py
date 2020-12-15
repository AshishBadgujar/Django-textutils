# i have created this file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    # return HttpResponse('''<h1>ashish</h1><a href=" http://127.0.0.1:8000/about">about</a>''')
def newlineremove(str):
            newstr=""
            for char in str:
                if char!="\n" and char!="\r":
                    newstr=newstr+char
            return newstr

def analyze(request):

    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    capitalize =request.POST.get('capital','off')
    removeline =request.POST.get('removeline','off')

    if removepunc =="on":
        punctuations = '''\|(){}[]-_;:'."/?<>,~`!@#$%^&*'''
        analyzed=""
        for char in djtext :
            if char not in punctuations:
                analyzed=analyzed + char
                
            
    if capitalize =="on":
        if removepunc=="off":
            analyzed=djtext.upper()
        else:
            analyzed=analyzed.upper()

    if removeline =="on":
        if removepunc=="off":
            analyzed=newlineremove(djtext)
        else:
            analyzed=newlineremove(analyzed)

    elif removepunc=="off" and capitalize=="off" and removeline=="off":
        return HttpResponse("Error")     

    params={'purpose':'Analyzed text','analyzed_text':analyzed}
    return render(request,'analyze.html',params)
        
  
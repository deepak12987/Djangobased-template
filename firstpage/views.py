#"coded my me"
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'one.html')
def analysis(request):
    djtext = request.POST.get("text","default")
    djtext1 = djtext
    resp = request.POST.get("removepunc","off")
    uppe = request.POST.get("uppercase","off")
    newline = request.POST.get("removenewline","off")
    extraspace = request.POST.get("extraspaceremove","off")

    if resp != "on" and extraspace != "on"  and newline != "on" and uppe != "on":
        return render(request,"alert.html")
        
    if resp == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        params = {'analyzed_text':analyzed}

    if uppe == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        djtext = analyzed
        params = {'analyzed_text':analyzed}
    
    if newline == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        djtext = analyzed
        params = {'analyzed_text':analyzed}

    if extraspace == "on":
        analyzed = ""
        for i,char in enumerate(djtext):
            if djtext[i] == " " and djtext[i+1] == " ":
                continue
            else:
                analyzed += char
        djtext = analyzed
    params = {'analyzed_text':analyzed,'Your_input':djtext1}
    return render(request,'analyze.html',params)
    

    
    

      


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')  
    



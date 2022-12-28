from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def index(request):
    #param = {'name' : 'punit', 'place' : 'delhi'}
    #params = {'navbar', render(request, 'navbar.html')}
    return render(request, 'index.html')
    #return HttpResponse("Home")

def removepun(request):
    text = request.POST.get('text', 'default')
    selectedOption = request.POST.get('selectOption', 'off')
    #print(text, checkRemovePunc)
    analyzed = text
    purpose = ""
    if selectedOption == "removePunc" :
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        purpose = "Remove Punctuation"
        for char in text:
            if char not in punctuation:
                analyzed += char

    elif selectedOption == "textCount" :
        analyzed = "total length of text is " + str(len(text))
        test = 1

    params = {'purpose' : purpose, 'text' : analyzed}

    print(params)
    return render(request, 'analyze.html', params)


def capitalize(request):
    return HttpResponse("Capitalize")

def about(request):
    return HttpResponse("About")
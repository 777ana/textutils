from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index2.html')

    # return HttpResponse("Home")


def contactMe(request):
    return render(request, 'contactMe.html')


def analyze(request):
    # Get the text

    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcap = request.POST.get('fullcap', 'off')
    charCount = request.POST.get('charCount', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    newLineRemover = request.POST.get('newLineRemover', 'off')
    print(removepunc)
    print(djtext)
    # analyzed = djtext
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        d = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed, 'char_count': 0}
        # return render(request, 'analyze.html', d)
        djtext = analyzed
    if fullcap == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        d = {'purpose': 'UPPERCASE', 'analyzed_text': analyzed, 'char_count': 0}
        # return render(request, 'analyze.html', d)
        djtext = analyzed

    if spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        d = {"purpose": "removing spaces", "analyzed_text": analyzed, 'char_count': 0}
        # return render(request, 'analyze.html', d)
        djtext = analyzed
    if newLineRemover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        print("pre", analyzed)
        d = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed, 'char_count': 0}
        # return render(request, 'analyze.html', d)
        djtext = analyzed
    if charCount == "on":
        c = 0
        for ele in djtext:
            c += 1
        d = {"purpose": "count characters", "analyzed_text": analyzed, "char_count": c}
        # return render(request, 'analyze2.html', d)

    if removepunc != 'on' and fullcap != "on" and spaceremover != "on" and newLineRemover != "on" and charCount != "on":
        return HttpResponse("Please select any operation and try again ")
    return render(request, 'analyze2.html', d)



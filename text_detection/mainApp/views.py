from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/index.html')

def contact(request):
    return render(request, 'mainApp/contacts.html', {'values':['Call me baybe', '87087749232']})

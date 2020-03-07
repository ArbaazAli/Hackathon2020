from django.shortcuts import render
from .models import Choice
import re
# Create your views here.


def home(request):
    if request.method == "POST":
        selection = request.POST['selections']
        #remove_sp = re.sub(" ", "", context )
        # choice = Choice(selections = context)
        # choice.save()
       # print(context)
        #print(remove_sp)
        #tags = remove_sp.lower().split(',')
       # print(tags) 
        #context = {'selection' : selection}
        return render(request, 'roadmap.html', context)

    else:
        return render(request, 'home.html')

def roadmap(request):
    return render(request, 'roadmap.html')  

def career(request):
    return render(request, 'career.html', {"engineer": 1, "doctor": 2})   

def faq(request):
    return render(request, 'faq.html')   
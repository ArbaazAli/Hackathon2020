from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Choice
import re
# Create your views here.


def home(request):
    if request.method == "POST":
        selection = request.POST['selections']
        context = Choice(selections = selection)
        context.save()
        print(selection)
        remove = re.sub(" ", "", selection)
        
        diction ={'actor': ['drama', 'acting', 'dancing'],
                 'manager': ['management', 'problemsolving', 'business'],
                 'engineer': ['programming', 'problemsolving', 'teamplay'],
                 'doctor': ['problemsolving', 'teamplay', 'decisionmaking'],
                 'cybersecurity': ['cryptography', 'networking', 'linux'],
                 'hotelmanagement': ['cooking', 'creativity', 'management'],
                 'datascientist': ['statistics', 'analysis', 'machinelearning'],
                 'robotics': ['maths', 'machinelearning', 'programming'],
                 'graphicsdesign': ['animation', 'uiuxdesign', 'creativity'],
                 'law': ['reasoning', 'legalresearch', 'communication'],
                 'teacher': ['communication', 'criticalthinking', 'technicalskills'],
                 'accountant': ['maths', 'finance', 'statistics']
                }

        print(diction.values())

        tags = remove.lower().split(',')
        career1 = set()

        for key in diction.keys():
            for skill in tags:
                if skill in diction[key]:
                    career1.add(key)
                    
        print(list(career1))
        
        
        #context = {'selection' : selection}
        return render(request, 'roadmap.html', {'key': career1})
    
    else :
        return render(request, 'home.html')

def roadmap(request):
    return render(request, 'roadmap.html')  

def career(request):
    return render(request, 'career.html', {"engineer": 1, "doctor": 2})   

def faq(request):
    return render(request, 'faq.html')   

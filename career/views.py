from django.shortcuts import render
from .models import Choice
import re
# Create your views here.


def home(request):
    if request.method == "POST":
        selection = request.POST['selections']
        print(selection)
        remove_sp = re.sub(" ", "", context )
        
       
        print(remove_sp)
        
        #context = {'selection' : selection}
        diction = {'actor': ['drama', 'acting', 'dancing'],
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
        tags = remove_sp.lower().split(',')
        print(tags) 
        career = set()
        
        for key in diction.keys():
            for skill in tags:
                if skill in diction[key]:
                    career.add(key)
                
        print(list(career))
        return render(request, 'roadmap.html', context)

    else:
        return render(request, 'home.html')

def roadmap(request):
    return render(request, 'roadmap.html')  

def career(request):
    return render(request, 'career.html', {"engineer": 1, "doctor": 2})   

def faq(request):
    return render(request, 'faq.html')   
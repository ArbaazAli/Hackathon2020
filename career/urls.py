from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name= "home"),
    path('roadmap/' , views.roadmap, name= "roadmap"),
    path('career/' , views.career, name= "career path"),
    path('faq/' , views.faq, name= "faq"),
]

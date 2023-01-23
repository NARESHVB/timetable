from django.shortcuts import render

# Create your views here.

def mytimetable(request):
    return render(request,'myapp/timetable.html')
from django.shortcuts import render
from .models import Archive
from django.template.loader import get_template
import datetime

# Create your views here.
def index(request):
    archive = Archive.objects.all()

    today = datetime.datetime.today()
    year = today.year
    week = today.isocalendar()[1]
    yw = f"{year}{week}"

    print(yw)

    question = ""
    for obj in archive:
        if obj.yearWeak == yw:
            question = obj


    context = {'question': question}

    return render(request, 'index.html', context)

def archive(request): 
    return render(request, "archive.html")

def leaderboard(request): 
    return render(request, "leaderboard.html")
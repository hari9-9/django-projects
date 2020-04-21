from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts=[
    {
        'author': 'Hari',
        'title':'Blog post 1',
        'content':'First post content',
        'date_posted':'aug 27,2018'

    },
    {
        'author': 'random dude',
        'title':'Blog post 2',
        'content':'secondpost content',
        'date_posted':'aug 27,2018'

    }
]
def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html')

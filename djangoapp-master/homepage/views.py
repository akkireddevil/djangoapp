from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index1(request):
    return HttpResponse("<h2>Welcome to my page</h2>"
                        "<h1>This is good</h1>"
                        "<p>Django is a high-level Python Web framework that encourages rapid development and"
                        "clean,pragmatic design."
                        "Built by experienced developers, it takes care of much of the hassle of Web development,"
                        "so you can focus on writing your app without needing to reinvent the wheel. It’s free and"
                        "open source.</p>"
                        "<a href='/music'>Click this link to go to the music section</a>")
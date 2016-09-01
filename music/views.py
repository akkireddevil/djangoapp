#from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Album
#from django.template import loader
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def index(request):
    all_albums=Album.objects.all()
    #template=loader.get_template('music/index.html')
    #The context(you can change the name of context to anything) is a dictionary passed onto the jinja
    context={'all_albums':all_albums}


    '''
       html=''
        for album in all_albums:
            url='/music/'+str(album.id)+'/'
            html=html+'<a href="'+url+'">'+album.album_title+'</a><br>'
    '''
    return render(request,'music/index.html',context)
    #return HttpResponse(template.render(context,request))

def detail(request,album_id):
    #return HttpResponse("<h2>Details for Album Id: "+str(album_id)+"</h2>")
    try:
        album=Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album Does not exist")
    return render(request,'music/detail.html',{'album':album} )
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import MovieInfo
from . forms import MovieForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login/')
def create(request):
    if request.method=="POST":
        fm=MovieForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect('list')
    else:
        fm=MovieForm()
      
    return render(request, "create.html",{'fm':fm})

@login_required(login_url='login/')
def list(request):
    recent_history=request.session.get('recent_history',[])

    count=(request.session.get('count',0))
    count=int(count)
    count=count+1
    request.session['count']=count
    recent_movies=MovieInfo.objects.filter(pk__in=recent_history)
    movie_set=MovieInfo.objects.all()
    print(movie_set)
    response=render(request, 'list.html',{
        'recent_movie':recent_movies,
        'movies':movie_set,'visits':count})
    return response

@login_required(login_url='login/')
def edit(request,pk):
    to_be_edited=MovieInfo.objects.get(pk=pk)
    if request.method=="POST":
        fm=MovieForm(request.POST,instance=to_be_edited)
        if fm.is_valid():
            to_be_edited.save()
    else:
        recent_history=request.session.get('recent_history',[])
        recent_history.insert(0,pk)
        request.session['recent_history']=recent_history
        fm=MovieForm(instance=to_be_edited)
    return render(request, "create.html",{'fm':fm})
    
@login_required(login_url='login/')
def delete(request,pk):
    instance=MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_set=MovieInfo.objects.all

    return render(request, "list.html",{'movies':movie_set})


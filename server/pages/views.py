from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Note

@login_required
def homePageView(request):
    user = request.user
    notes = Note.objects.filter(user=user)
    return render(request, 'pages/index.html', {'notes': notes})

def loginView(request):
    form = AuthenticationForm()
    return render(request, 'pages/login.html', {'form': form})



def addNoteView(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        user = request.user
        note = Note.objects.create(user=user, content=content)
        note.save()
        return redirect('home')
    else:
        return render(request, 'pages/index.html')
    
#def homePageView(request):
   # if request.user.is_authenticated:
      #  user = request.user
     #   blogs = Blog.objects.filter(user=user)
     #   return render(request, 'pages/index.html', {'blogs': blogs})
  #  else:
  #      return render(request, 'pages/index.html')
    



# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PetArticleForm

def add_article(request):
    """
    Handles the addition of a new article using PetArticleForm.
    """
    if request.method == 'POST':
    
        form = PetArticleForm(request.POST)
        if form.is_valid():
            
            form.save()
            messages.success(request, "Article added successfully!")
            return redirect('home')
        else:
    
            messages.error(request, "There was an error adding the article. Please try again.")
    else:
        form = PetArticleForm()

    return render(request, 'add_article.html', {'form': form})

def home(request):
    return render(request, 'petcare101/home.html')
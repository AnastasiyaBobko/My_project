from traceback import format_exception
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from .forms import FoodTracker
from .models import Food

def home(request):
    return render(request, 'home.html')

def articles(request):
    all_articles = Article.objects.all()
    
    return render(request, 'articles.html', {'articles':all_articles})

def article(request, article_id):
    article = Article.objects.get(id=article_id)
    
    return render(request, 'article.html', {'article':article})

def add_food(request):
   
    if request.method == 'POST':
        
        form = FoodTracker(request.POST)
               
        if form.is_valid():
            food = Food()
            food.name = form.cleaned_data['name']
            food.quantity = form.cleaned_data['quantity']
            food.calorie = form.cleaned_data['calorie']
            
            food.save()
            
            return redirect('personal_page')
    else:
        form = FoodTracker()
            
    return render(request, 'add_food.html', {'form': form})

def personal_page(request):
    all_food = Food.objects.all()
    return render(request, 'personal_page.html', {'personal_page':all_food})


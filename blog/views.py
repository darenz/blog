from django.shortcuts import render
from blog.models import Article
from django.views import generic

# Create your views here.

def index(request):
    return render(request,'index.html')

class ArticleListView(generic.ListView):
    model = Article

class ArticleDetailView(generic.DetailView):
    model = Article


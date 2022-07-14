from django.shortcuts import render
from .models import Article,Product,Food
from django.utils import timezone
from django.views.generic import DetailView,ListView

class FoodDetailView(DetailView):

    model = Food
    

class FoodListView(ListView):

    model = Food
    paginate_by = 100  # if pagination is desired

class home(ListView):

    model = Article
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ProductListView(ListView):

    model = Product
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ArticleDetailView(DetailView):

    model = Article



    # if model.title=='What is Autophagy?':
    #     template_name='tracker/article_detail2.html'

    def get_context_data(self, **kwargs):
        print(self.object.title)
        if self.object.title=='What is Intermittent fasting?':
            print('fast')
            self.template_name='tracker/fasting.html'
        if self.object.title=='What is Autophagy?':
            self.template_name='tracker/autophagy.html'
        if self.object.title== "What is a Ketogenic Diet?":
            print('test')
            self.template_name='tracker/keto.html'
       

        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['Products'] = Product.objects.filter(articles=self.get_object())
        return context

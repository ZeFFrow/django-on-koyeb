from typing import Any
from django import http
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, FormView, CreateView, DetailView
from django.http import JsonResponse
from django.forms import modelformset_factory
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from .forms import *

# Create your views here.

def test2(request):
    return render(request, 'tele/test2.html')

def telegraph(request):
    return render(request, 'tele/Telegraph.html')
                  
def index(request):
    return render(request, 'tele/index2.html') 


def pageNotFound(request,exeption):
	return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# def get_name_by_id(request, slug):
#     split_slug = slug.split('-')
#     # return HttpResponse(f"Эта страница под id { ' '.join(slug.split('-'))}")
#     return render(request, 'Telegraph.html')
    
class get_name_by_id(TemplateView):
    template_name = 'tele/Telegraph.html'
    
    def post(self, request, *args: Any, **kwargs: Any) -> HttpResponse:
        print(args, kwargs)
        return super().post(request, *args, **kwargs)
        
class ArticleCreate(CreateView):
    model = Article
    fields = ['name','msg','img']
    template_name = "tele/CreateArticle.html"
    
    
class ShowArticle(DetailView):
    # pk_url_kwarg = "title"
    model = Article
    template_name = "tele/ShowArticle.html"
    
    def get_context_data(self, **kwargs):
        context = super(ShowArticle, self).get_context_data(**kwargs)
        
        context['article'] = self.model.objects.get(pk=self.kwargs['pk'])
        context['imgs'] = Images.objects.all().filter(post = self.kwargs['pk']) 
        
        return context
    
@csrf_exempt
def check(request):
    return JsonResponse()

def post(request):
 
    # ImageFormSet = modelformset_factory(Images,
    #                                     form=ImageForm, extra=3)
    #'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':
        imgs = request.FILES.getlist('pro-image[]')

        print(request.POST)
        postForm = PostForm(request.POST)
        # formset = ImageFormSet(request.POST, request.FILES,
        #                        queryset=Images.objects.none())
    
    
        if postForm.is_valid():
            post_form = postForm.save(commit=False)
            post_form.save()
    
            for image in imgs:
                Images.objects.create(
                    post = post_form,
                    image = image
                )
            # use django messages framework
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect(f"/{post_form.pk}")
        else:
            print(postForm.errors)
    else:
        postForm = PostForm()
        # formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'tele/index2.html',
                  {'postForm': postForm, })            
from django.shortcuts import render
from .models import Destination
from django.core.paginator import Paginator

# Create your views here.
def index(request):
	
	dests = Destination.objects.all()
	page = request.GET.get('page','1')

	paginator = Paginator(dests, 4)
	page_obj = paginator.get_page(page)
	 
	return render(request, 'index.html',{'dests':page_obj})

#def index(request): 
    #dests = Destination.objects.all()
    #return render(request, 'home.html',{'question_list':question_list})	
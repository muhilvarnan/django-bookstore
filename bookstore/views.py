from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from models import get_top_selling_books, get_top_authors 

# Create your views here.

def top_selling_books(request):
	"""
	get top selling book
	"""
	try:
		return JsonResponse(get_top_selling_books(), safe=False)
	except Exception, e:
		print e
		return JsonResponse([], safe=False)

def top_authors(request):
	"""
	get top authors book
	"""
	try:
		return JsonResponse(get_top_authors(), safe=False)
	except Exception, e:
		print e
		return JsonResponse([], safe=False)
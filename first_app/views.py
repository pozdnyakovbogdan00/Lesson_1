from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def about(request):
	return HttpResponse("<h2>Тут будет информация о фирме</h2>")

def catalog(request):
	return HttpResponse("<h2>Тут будет каталог товаров</h2>")

def contacts(request):
	return HttpResponse("<h2>Тут будут контакты компании</h2>")	

def team(request):
	return HttpResponse("<h2>Тут будет информация о самых топовых сотрудников</h2>")	

def trash(request):
	return HttpResponse("<h2>Тут будет информация допустим о выбранных покупках</h2>")
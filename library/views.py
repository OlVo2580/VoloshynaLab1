from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from .models import *



menu = ['Фонд кафедральної бібліотеки', 'Обрати видання', 'Увійти']


def index(request):
    return render(request, 'library/index.html', {'menu': menu, 'title': 'Кафедральна бібліотека'})


def about(request):
    editions = Edition.objects.all()
    abstract = Edition.objects.all()
    status = Status.objects.all()
    return render(request, 'library/about.html', {'editions': editions, 'menu': menu, 'title': 'Фонд кафедральної бібліотеки:'})


def author(request):
     author = Author.objects.all()  
     return render(request, 'library/author.html', {'authors': author, 'menu' : menu, 'title' : 'Автори'})


def author_edition(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    editions = EditionsAuthors.objects.filter(author=author)
    return render(request, 'library/works.html', {'title': 'Твори автора', 'author': author, 'works': editions})


def subject(request):
     subject = Subject.objects.all()
     return render(request, 'library/subject.html', {'subjects': subject, 'menu' : menu, 'title' : 'За тематиками'})


def abstract(request, edition_id):
    edition = get_object_or_404(Edition, pk=edition_id)
    return render(request, 'library/abstract.html', {'edition': edition})

def editions(request, editionsid):
     if(request.POST):
          print(request.POST)
     return HttpResponse (f"<h1>Видання наявні в бібліотеці</h1><p>{editionsid}</p>")


def test(request):
     return render(request, 'library/test.html')


def pageNotFound(request, exception):
     print("404 Сторінку не знайдено")
     return HttpResponseNotFound('<h1>Сторінку не знайдено</h1>')

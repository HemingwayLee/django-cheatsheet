from django.views.generic import TemplateView, ListView, View
from django.http import HttpResponse
from .models import Book

class AboutView(TemplateView):
    template_name = "about.html"

class BookListView(ListView):
    template_name = 'book.html'
    model = Book

    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest('publication_date')
        response = HttpResponse('')
        # RFC 1123 date format
        response['Last-Modified'] = last_book.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response

class GenericView(View):
    def get(self, request):
        return HttpResponse('hello, generic')
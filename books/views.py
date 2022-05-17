from django.shortcuts import render, redirect

from .models import Author, Book
from .forms import BookForm, BookFormSet

# Create your views here.
def create_book(request, pk):
    author = Author.objects.get(pk=pk)
    formset = BookFormSet(request.POST or None)

    if request.method == "POST":
         if formset.is_valid():
            formset.instance = author
            formset.save()
            return redirect("create-book", pk=author.id)


    context = {
        "formset":formset,
        "author":author
    }

    return render(request, "create_book.html", context)


def create_book_form(request):
    form = BookForm()
    context = {
        "form":form
    }
    return render(request, "partials/book_form.html", context)


from django.shortcuts import render, redirect
from .forms import BookForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Assuming you have a view named book_list for listing books
    else:
        form = BookForm()
    return render(request, 'bookstore/add_book.html', {'form': form})

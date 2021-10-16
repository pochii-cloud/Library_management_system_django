import os.path
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import path

from core.forms import AddBook
from core.models import Book, Contact, Profile
import PyPDF2
from django.views.static import serve


def baseone(request):
    return render(request, 'baseone.html')


def base(request):
    if not request.user.is_authenticated:
        return redirect("loginview")
    book = Book.objects.all()
    contact = Contact()
    if request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        contact.username = username
        contact.email = email
        contact.feedback = feedback
        contact.save()
        return HttpResponse('feedback received thankyou')
    return render(request, 'base.html', {'book': book})


def contact(request):
    contact = Contact()
    if request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        contact.username = username
        contact.email = email
        contact.feedback = feedback
        contact.save()
        messages.info(request, 'feedback received thankyou')
    return render(request, 'contact.html')


def detail(request, book_id):
    if not request.user.is_authenticated:
        messages.info(request, 'login to access book features')
        return redirect("loginview")
    book = Book.objects.get(pk=book_id)
    return render(request, 'detail.html', {'book': book})


def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        book = Book.objects.all().filter(title__icontains=search).order_by('title')
        return render(request, 'search.html', {'book': book})


def download(request):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response = HttpResponse(fh.read(), content_type='application/Book')
            response['content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
    raise Http404


def borrow_view(request, book_id):
    book = Book.objects.get(pk=book_id)
    if not book.borrowed:
        book = Book.objects.get(pk=book_id)
        book.borrowed = True
        book.quantity -= 1
        book.date = datetime.today()
        book.date2 = book.date + timedelta(days=10)
        if book.date <= book.date2:
            book.penalty = 0
            book.save()
        elif datetime.today() > book.date2:
            total_days = datetime.today() - book.date2
            book.penalty = total_days * 5
            book.save()
        return redirect("borrowpage")
    if book.borrowed and book.quantity > 0:
        book.borrowed = True
        book.quantity -= 1
        book.save()
        return redirect("borrowpage")
    elif book.borrowed and book.quantity == 0:
        book.borrowed = False
        return HttpResponse('all copies borrowed.check back later!!')
    else:
        return render(request, 'base.html')


def return_view(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.borrowed = False
    book.quantity += 1
    book.save()
    messages.success(request, 'book returned successfully')
    return redirect('borrowpage')


def borrowpage(request):
    if not request.user.is_authenticated:
        return redirect("loginview")
    book = Book.objects.all()
    profile = Profile.objects.all()
    return render(request, 'borrow.html', {'book': book, 'profile': profile})


def home2(request):
    return render(request, 'intro.html')


def adminview(request):
    if not request.user.is_superuser:
        return redirect("loginview")
    book = Book.objects.all()
    book.date = datetime.today()
    book.date2 = book.date + timedelta(days=10)
    return render(request, 'administator.html', {'book': book})


def delete(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    messages.info(request, 'book deleted successfully!!')
    return redirect('adminview')


def addview(request):
    form = AddBook()
    if request.POST:
        form = AddBook(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'upload successfull')

    return render(request, 'add.html', {'form': form})


def penalty_view(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.date = datetime.today()
    book.date2 = book.date + timedelta(days=10)
    if book.date <= book.date2:
        book.penalty = 0
    elif datetime.today() > book.date2:
        total_days = datetime.today() - book.date2
        book.penalty = total_days * 5
        book.save()
    else:
        return render(request, 'borrow.html')

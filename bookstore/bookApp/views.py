from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate 
from .models import Subscriber


def home(request):
   
    books = Book.objects.all()
    categories = Category.objects.all()
    context = {'books': books,'categories': categories}
    return render(request, 'home.html', context)


def book(request, id):
    book = Book.objects.get(book_id=id)
    author = Author.objects.all()
    categories = Category.objects.all()
    context = {"book": book,"author":author,'categories': categories}
    return render(request, 'book.html', context)

def category(request, id):
    categories = Category.objects.all().order_by("-category_id")
    selected_category = Category.objects.get(category_id=id)
    bookcategory = Book.objects.filter(book_category=selected_category).order_by("-book_id")
    context = {"selected_category": selected_category, "categories": categories, "bookcategory": bookcategory}
    return render(request, 'category.html', context)

def books(request):
    categories = Category.objects.all().order_by("-category_id")
    books = Book.objects.all().order_by("-book_id")
    context = {"books": books, "categories":categories}
    return render(request, 'books.html', context)

def contact(request):
    categories = Category.objects.all().order_by("-category_id")
    if request.method == "POST":
        emri = request.POST['firstName']
        mbiemri = request.POST['lastName']
        email = request.POST['email']
        komenti = request.POST['comment']
        
        if emri!='' and mbiemri != '' and email !='' and komenti !='':
            Contact(contact_name=emri, contact_surname=mbiemri, contact_email=email,
                    contact_comment=komenti).save()
            messages.success(request, "Message send!")
        else:
            messages.error(request, "Message not send!")
        # return redirect('/')
    context = {"categories":categories}
    return render(request, 'contact.html', context)




def aboutus(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    context = {'books': books,'categories': categories}
    return render(request, 'aboutus.html',context)
    

def search(request):
    book = Book.objects.all()
    categories = Category.objects.all()
    query = request.GET.get('q')
    
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.none()
    context = {'books': books,'categories': categories,'query': query,'books': books}
    return render(request, 'search.html', context)


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if Subscriber.objects.filter(email=email).exists():
                messages.warning(request, 'You are already subscribed!')
            else:
                subscriber = Subscriber(email=email)
                subscriber.save()
                messages.success(request, 'Thank you for subscribing!')
        else:
            messages.error(request, 'Please provide a valid email.')

    return render(request, 'index.html')  
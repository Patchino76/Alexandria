from django.shortcuts import render

# Create your views here.

def sample(request):
    books = [
        {
            'title': 'The Great Gatsby',
            'author': 'F. Scott Fitzgerald',
            'recommendation': True
        },
        {
            'title': 'To Kill a Mockingbird',
            'author': 'Harper Lee',
            'recommendation': True
        },
        {
            'title': '1984',
            'author': 'George Orwell',
            'recommendation': False
        }
    ] 
    return render(request, 'sample.html', {'books': books})


def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')
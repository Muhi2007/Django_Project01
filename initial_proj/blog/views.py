from django.shortcuts import render

posts = [
    {
        'username': 'Muhi',
        'title': 'Blog Post 1',
        'date': '30 December 2025',
        'text': 'This is the first dummy post'
    },
    {
        'username': 'Muhammad',
        'title': 'Blog Post 2',
        'date': '30 December 2025',
        'text': 'This is the second dummy post'
    },
    {
        'username': 'Eli',
        'title': 'Blog Post 3',
        'date': '30 December 2025',
        'text': 'This is the third dummy post'
    },
]

# Create your views here.
def home(request):
    context = {'posts': posts}

    return render(request, "blog/home.html", context)
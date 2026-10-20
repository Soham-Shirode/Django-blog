from django.shortcuts import render

posts = [
    {
        'author': 'Kurien M',
        'title': 'Blog post 1',
        'content': 'first post content',
        'date_posted': 'August 27, 2025'
    },
    
        {
        'author': 'Avdhoot B',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'August 27, 2015'
    },
    
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


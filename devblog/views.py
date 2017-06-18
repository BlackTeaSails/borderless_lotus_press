from django.shortcuts import render
from devblog.models import Post # el modelo a tratar
from django.core.paginator import Paginator # Para paginar los posts
from devblog.forms import PostFormDrace # para añadir un post nuevo o editarlo
from django.contrib import messages # error and success messages

def allpostsview(request, page_number):
    prefix = '/blog/page-'
    posts = Post.objects.order_by('published_date')
    paginator = Paginator(posts, 5)
    last_page = int(paginator.num_pages)
    posts = paginator.page(page_number)
    # si page_number > last_page toma o last_page == 0, toma 404
    pages = calculate_pages(int(page_number), last_page)
    return render(request, 'blog/page.html', {'range':pages, 'page':page_number, 'last_page':last_page, 'prefix':prefix, 'posts':posts})

def postsbyauthor(request, author_id, page_number):
    prefix = '/blog/author-' + author_id + '/page-'
    posts = Post.objects.filter(author_id=int(author_id)).order_by('published_date')
    paginator = Paginator(posts, 5)
    last_page = int(paginator.num_pages)
    posts = paginator.page(page_number)

    # si page_number > last_page toma o last_page == 0, toma 404
    pages = calculate_pages(int(page_number), last_page)
    return render(request, 'blog/page.html', {'range':pages, 'page':page_number, 'last_page':last_page, 'prefix':prefix, 'posts':posts})

def newpost_view(request):
    form = PostFormDrace()
    if request.method == 'POST':
        form = PostFormDrace(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Se ha añadido el post nuevo.')
        else:
            messages.error(request, 'Fallo al crear el post.', extra_tags='danger')
    return render(request, 'blog/newpost.html', {'form':form})

def post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post.html', { 'post':post})

def calculate_pages(current_page, last_page):
    # decidimos las paginas que añadir abajo segun las paginas totales y la pagina actual
    # se añaden las dos primeras, las dos ultimas, la actual y las dos de alrededor
    pages = [1]
    if last_page > 1:
        pages.append(2)
    if current_page>3:
        pages.append(current_page-1)
    if current_page>2:
        pages.append(current_page)
    if current_page<last_page-1 and current_page>1:
        pages.append(current_page+1)
    if current_page<last_page-1 and last_page > 3:
        pages.append(last_page-1)
    if current_page<last_page:
        pages.append(last_page)
    return pages

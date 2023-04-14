from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods,require_POST,require_safe
from .models import Movies,Comment
from .forms import MoviesForm,CommentForm

# Create your views here.
def index(request):
    movies = Movies.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)


def detail(request, pk):
    movies = Movies.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = movies.comment_set.all()
    context = {
        'movies': movies,
        'comment_form':comment_form,
        'comments':comments,}
    return render(request, 'movies/detail.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MoviesForm(request.POST, request.FILES)
        if form.is_valid():
            movies = form.save(commit=False)
            movies.user = request.user
            movies.save()
            return redirect('movies:detail', movies.pk)
    else:
        form = MoviesForm()

    context = {'form': form}
    return render(request, 'movies/create.html', context)


def delete(request, pk):
    movies = Movies.objects.get(pk=pk)
    movies.delete()
    return redirect('movies:index')


def update(request, pk):
    movies = Movies.objects.get(pk=pk)

    if request.method == 'POST':
        form = MoviesForm(request.POST, request.FILES, instance=movies)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', pk=movies.pk)
    else:
        form = MoviesForm(instance=movies)

    context = {'form': form, 'movies': movies}
    return render(request, 'movies/update.html', context)


def comments_create(request,pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    movie = Movies.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment.save()
    return redirect('movies:detail',movie.pk)

def comments_delete(request, pk, comment_pk):
    if not request.user.is_authenticated:
        return redirect('account:login')
    comment = Comment.objects.get(pk=pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('movies:detail',pk)

def likes(request,movie_pk):
    if request.user.is_authenticated:
        movie = Movies.objects.get(pk=movie_pk)
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
        else:
            movie.like_users.add(request.user)
        return redirect('movies:index')
    return redirect('accounts:login')

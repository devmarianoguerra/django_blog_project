from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post


def inicio(request):
    return render(request, 'posts/inicio.html')


def acerca(request):
    return render(request, 'posts/acerca.html')


def lista_posts(request):
    posts = Post.objects.filter(estado='publicado').order_by('-fecha_creacion')
    context = {
        'posts': posts,
    }
    return render(request, 'posts/lista_posts.html', context)


def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/detalle_post.html', {'post': post})


def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})


def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form})


def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')
    return render(request, 'posts/post_confirm_delete.html', {'post': post})

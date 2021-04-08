from django.shortcuts import render, redirect
from django.views.generic import FormView, DetailView, ListView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from .forms import SignupForm, CreateCommentForm
from django.http import HttpResponse
from core.blog.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
class SignupView(FormView):
    """Users sign up view."""

    template_name = 'registerBlog.html'
    form_class = SignupForm
    success_url = reverse_lazy('blog:registerok')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)

class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'loginBlog.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    template_name = 'logged_out.html'

class PostsFeedView(ListView):
    """Index."""
    template_name = 'indexBlog.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 10
    context_object_name = 'posts'
    queryset = Post.objects.filter(is_draft=False)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    
class PostDetailView(DetailView):
    """Detail post."""
    template_name = 'detailBlog.html'
    model = Post
    context_object_name = 'post'
    slug_field = 'url'
    slug_url_kwarg = 'url'


    def get_queryset(self):
        return Post.objects.filter(is_draft=False)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['comments'] = Comment.objects.filter(post=self.get_object()).all()
        context['form_comments'] = CreateCommentForm()
        return context


@login_required
def save_comment(request):
    if request.method == 'POST':
        url = request.POST['url']
        post = {
            'user': request.user.id,
            'profile': request.user.id,
            'comment': request.POST['comment'],
            'post': request.POST['post']
        }
        form = CreateCommentForm(post)
        if form.is_valid():
            form.save()
            return redirect('posts:detail_post', url=url)
    else:
        return HttpResponse(status=405)
    return HttpResponse(status=500)


from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from blog.models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.forms import PostForm,CommentForm
from django.urls import reverse_lazy
# Create your views here.

'''
TemplateView:
Renders a given template, with the context containing parameters captured in the URL.
'''
class AboutView(TemplateView):
    template_name = "about.html"

'''
ListView, which will render a list of objects, typically from a queryset, and optionally paginate them
get_queryset()
Used by ListViews - it determines the list of objects that you want to display.
By default it will just give you all for the model you specify. By overriding
this method you can extend or completely replace this logic.
https://docs.djangoproject.com/en/2.0/topics/class-based-views/generic-display/#generic-views-of-objects
'''
class PostListView(ListView):
    model=Post
    def get_queryset(self):
        #https://docs.djangoproject.com/en/2.1/topics/db/queries/  to check __lte
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

'''
DetailView
While this view is executing, self.object will contain the object that the view is operating upon.
'''
class PostDetailView(DetailView):
    model=Post

'''
CreateView
A view that displays a form for creating an object, redisplaying the form with
validation errors (if there are any) and saving the object.
'''

'''
class LoginRequiredMixin¶
If a view is using this mixin, all requests by non-authenticated users will be
redirected to the login page or shown an HTTP 403 Forbidden error, depending
on the raise_exception parameter.
You can set any of the parameters of AccessMixin to customize the handling of unauthorized users:
from django.contrib.auth.mixins import LoginRequiredMixin
class MyView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
'''
class CreatePostView(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name='blog/post_detail.html'
    form_class=PostForm
    model=Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name='blog/post_detail.html'
    form_class=PostForm
    model=Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    success_url= reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name='blog/post_list.html'
    model=Post
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')



##########################################################################
##########################################################################
@login_required
def post_pulish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish
    return redirect('post_detail',pk=pk)


@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            commnet.post=post
            comment.save()
            return redirect('post_detail',pk=post.pk)
        else:
            form=CommentForm()
        return render(request,'blog/comment_form.html',{'form':form})
'''
get_object_or_404:
Calls get() on a given model manager, but it raises Http404 instead of the
model’s DoesNotExist exception.
pk:
primary key
'''

@login_required
def  comment_approve(request,pk):
    comment=get_object_or_404(Commentm,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def commnet_remove(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)

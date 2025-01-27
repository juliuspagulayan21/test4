from django.views.generic import (
    CreateView, UpdateView, DetailView, ListView, DeleteView, TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.urls import reverse_lazy
from .models import Category, Post, Comment, Alert
from .forms import AlertForm




class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class ContactPageView(TemplateView):
    template_name = 'app/contact.html'

# CATEGORY VIEWS
class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context['posts'] = Post.objects.filter(category=category)
        return context

# CATEGORY VIEWS
class CategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Category
    fields = ['category_image', 'name', 'description']
    template_name = 'category/category_create.html'

    def test_func(self):
        # Only LGU Members can create categories
        if self.request.user.role == 'LGU Member':
            return True
        raise Http404("You are not authorized to create a category.")


class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    fields = ['category_image', 'name', 'description']
    template_name = 'category/category_update.html'

    def test_func(self):
        # Only LGU Members can update categories
        if self.request.user.role == 'LGU Member':
            return True
        raise Http404("You are not authorized to update this category.")


class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    template_name = 'category/category_delete.html'
    success_url = reverse_lazy('category_list')

    def test_func(self):
        # Only LGU Members can delete categories
        if self.request.user.role == 'LGU Member':
            return True
        raise Http404("You are not authorized to delete this category.")


# POST VIEWS
class PostListView(ListView):
    model = Post
    template_name = 'app/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'app/post_detail.html'
    context_object_name = 'post'

# POST VIEWS
class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'post_image', 'content', 'category']
    template_name = 'app/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        # Only LGU Members can create posts
        if self.request.user.role == 'LGU Member':
            return True
        raise Http404("You are not authorized to create a post.")


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'post_image', 'content', 'category']
    template_name = 'app/post_update.html'

    def test_func(self):
        # Only LGU Members can update posts
        if self.request.user.role == 'LGU Member':
            return True
        raise Http404("You are not authorized to update this post.")


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'app/post_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        # Only LGU Members can delete posts
        if self.request.user.role == 'LGU Member':
            return True
        raise Http404("You are not authorized to delete this post.")



# COMMENT VIEWS
class CommentListView(ListView):
    model = Comment
    template_name = 'comments/comment_list.html'
    context_object_name = 'comments'

class CommentDetailView(DetailView):
    model = Comment
    template_name = 'comments/comment_detail.html'
    context_object_name = 'comment'

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    template_name = 'comments/comment_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(pk=self.kwargs['pk'])
        context['post'] = post
        return context


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'comments/comment_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.object.post
        return context

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})

    def dispatch(self, request, *args, **kwargs):
        comment = self.get_object()
        if request.user.role != 'LGU Member' and comment.author != request.user:
            raise Http404("You are not authorized to edit this comment.")

        return super().dispatch(request, *args, **kwargs)


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comments/comment_delete.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})

    def dispatch(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user:
            raise Http404("You are not authorized to delete this comment.")
        return super().dispatch(request, *args, **kwargs)

# ALERT VIEWS
class AlertListView(ListView):
    model = Alert
    template_name = 'alerts/alert_list.html'
    context_object_name = 'alerts'

class AlertDetailView(DetailView):
    model = Alert
    template_name = 'alerts/alert_detail.html'
    context_object_name = 'alert'

class AlertCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Alert
    fields = ['title', 'alert_image', 'message', 'valid_until']
    template_name = 'alerts/alert_create.html'

    def form_valid(self, form):
        form.instance.issued_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.role == 'LGU Member':
            return True
        raise Http404("You are not authorized to create an alert.")


class AlertUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Alert
    form_class = AlertForm  # Use the customized form
    template_name = 'alerts/alert_update.html'

    def test_func(self):
        if self.request.user.role == 'LGU Member':
            return True
        raise Http404("You are not authorized to update this alert.")


class AlertDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Alert
    template_name = 'alerts/alert_delete.html'
    success_url = reverse_lazy('alert_list')

    def test_func(self):
        if self.request.user.role == 'LGU Member':
            return True
        raise Http404("You are not authorized to delete this alert.")




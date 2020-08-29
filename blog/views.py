from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .models import Post
from django.contrib.messages.views import SuccessMessageMixin
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'
    form_class = PostForm
    success_message = "%(field)s - criado com sucesso"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super(BlogCreateView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.title,
        )


class BlogUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'
    success_message = "%(field)s - alterado com sucesso"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super(BlogUpdateView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.title,
        )


class BlogDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
    success_message = "Deletado com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BlogDeleteView, self).delete(request, *args, **kwargs)

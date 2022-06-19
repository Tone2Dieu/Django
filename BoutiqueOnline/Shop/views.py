
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class BlogPostLister(ListView):
    model = BlogPost
    template_name = "formation/accueil.html"
    context_object_name = "formations"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)


class BlogPostDetail(DetailView):
    model = BlogPost
    template_name = "formation/formation.html"
    context_object_name = "b"


class CreateBlogPost(CreateView):
    model = BlogPost
    template_name = "formulaire/form.html"
    fields = ["title", "author", "published", "content"]
    success_url = reverse_lazy("accueil")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_text"] = "valider"
        return  context


# @method_decorator(login_required, name='dispatch')
class ModifBlogPost(UpdateView):
    model = BlogPost
    template_name = "formulaire/form.html"
    fields = ["title", "author","published", "content"]
    success_url = reverse_lazy("accueil")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["submit_text"] = "Modifier"
        return  context


class DeleteBlogPost(DeleteView):
    model = BlogPost
    template_name = "formulaire/deletefrom.html"
    success_url = reverse_lazy("accueil")


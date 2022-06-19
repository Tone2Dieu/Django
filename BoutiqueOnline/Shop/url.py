from django.urls import path

from Boutique import settings
from .views import BlogPostLister, BlogPostDetail, CreateBlogPost, ModifBlogPost, DeleteBlogPost
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static


urlpatterns = [
    path("", BlogPostLister.as_view(), name="accueil"),
    path("formulaire", CreateBlogPost.as_view(), name="createform"),
    path("update/<str:slug>", login_required(ModifBlogPost.as_view()), name="updateform"),
    path("article/<str:slug>", BlogPostDetail.as_view(), name="formation"),
    path("deleteform/<str:slug>", DeleteBlogPost.as_view(), name="delete")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
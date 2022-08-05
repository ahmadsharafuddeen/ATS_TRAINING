from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.IndexPageView.as_view(), name='starting-page'),
    path('blogs/', views.BlogListView.as_view(), name="blog-list-page"),
    path('profile/', views.ProfileUpdateView.as_view(), name="profile_edit"),
    path('blogger/<int:pk>', views.BlogAuthorDetailView.as_view(), name="author-detail"),
    path('bloggers/', views.BloggersListView.as_view(), name="bloggers-list"),
    path('<slug:slug>', views.BlogPostDetailPage.as_view(), name="blog-detail"),
    path('<slug:slug>/edit', views.UpdateBlogView.as_view(), name="update-blog"),
    path('<slug:slug>/<int:pk>/', views.ToggleComment.as_view(), name="toggle-comment"),
    path('password_change/', views.ChangePasswordView.as_view(), name="password_change"),
]
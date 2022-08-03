from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from django.views.generic import UpdateView
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.models import User, AnonymousUser
from .models import Blog, Comment, Profile
from .forms import CommentForm, ProfileForm, UserForm


# Create your views here.
class IndexPageView(View):
    def get(self, request):
        num_blogs = Blog.objects.all().count()
        num_comments = Comment.objects.all().count()
        num_bloggers = User.objects.all().count()
        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1

        user = self.request.user
        if user != AnonymousUser:
            current_user = user
        else:
            current_user = None

        context = {
            "num_blogs": num_blogs,
            "num_comments": num_comments,
            "num_bloggers": num_bloggers,
            "num_visits": num_visits,
            "current_user": current_user
        }
        return render(request, "blog/index.html", context)


class BlogListView(ListView):
    model = Blog
    ordering = ["-id"]


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = "blog/change_password.html"
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy("author-detail")

    def get_success_url(self):
        user_id = self.request.user.id
        return reverse_lazy("blog:author-detail", kwargs={"pk": user_id})


class BlogAuthorDetailView(View):
    def get(self, request, pk):
        profile = Profile.objects.get(author_id=pk)
        current_user = User.objects.get(id=pk)
        profile_form = ProfileForm(instance=profile)
        user_form = UserForm(instance=current_user)

        comments_for_blogger = Comment.objects.filter(blog__author=self.kwargs['pk']).count()
        context = {
            "user_detail": profile.author,
            "total_comments": comments_for_blogger,
            "user_form": user_form,
            "profile": profile,
            "profile_form": profile_form,
        }
        return render(request, "blog/user_detail.html", context)

    def post(self, request, pk, *args, **kwargs):
        user = User.objects.get(id=pk)
        user_profile = Profile.objects.get(author_id=pk)

        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse("blog:author-detail", args=[pk]))

        comments_for_blogger = Comment.objects.filter(blog__author=self.kwargs['pk']).count()
        context = {
            'user_detail': user_profile.author,
            'total_comments': comments_for_blogger,
            'profile_form': profile_form
        }
        return render(request, "blog/user_detail.html", context)


class BlogPostDetailPage(View):
    def get(self, request, slug):
        blog = Blog.objects.get(slug=slug)

        context = {
            "blog": blog,
            "comment_form": CommentForm(),
            "comments": blog.comments.all().order_by("-post_date")
        }
        return render(request, "blog/blog_detail.html", context)

    @method_decorator(login_required)
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        blog = Blog.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blog = blog
            comment.comment_owner = self.request.user
            comment.save()
            return HttpResponseRedirect(reverse("blog:blog-detail", args=[slug]))

        context = {
            "blog": blog,
            "comment_form": comment_form,
            "comments": blog.comments.all().order_by("-post_date")
        }
        return render(request, "blog/blog_detail.html", context)


class BloggersListView(ListView):
    model = User
    template_name = "blog/user_list.html"
    ordering = ["first_name"]


# class ProfileUpdateView(UpdateView):
#     model = Profile
#     fields = "__all__"
#     template_name = "blog/profile.html"
#     success_url = "/"

# logging in, logging out
# admin site

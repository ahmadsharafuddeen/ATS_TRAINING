from django.shortcuts import render
from django.views import View
from django.views.generic import UpdateView
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q

from django.contrib.auth.models import User
from .models import Blog, Comment, Profile
from .forms import CommentForm, ProfileForm, UserForm, BlogUpdateForm


# Create your views here.
class IndexPageView(TemplateView):
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexPageView, self).get_context_data(**kwargs)
        context["num_blogs"] = Blog.objects.all().count()
        context["num_comments"] = Comment.objects.all().count()
        context["num_bloggers"] = User.objects.all().count()
        context["num_visits"] = self.request.session.get('num_visits', 0)
        self.request.session['num_visits'] = context["num_visits"] + 1
        return context


class BlogListView(ListView):
    model = Blog
    ordering = ["-id"]

    def get_queryset(self):
        return Blog.active_objects.all()


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = "blog/change_password.html"
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy("author-detail")

    def get_success_url(self):
        user_id = self.request.user.id
        return reverse_lazy("blog:author-detail", kwargs={"pk": user_id})


class BlogAuthorDetailView(DetailView):
    model = User
    template_name = "blog/user_detail.html"
    context_object_name = "user_detail"

    def get_context_data(self, **kwargs):
        context = super(BlogAuthorDetailView, self).get_context_data(**kwargs)
        profile = Profile.objects.get(author_id=self.kwargs["pk"])
        current_user = User.objects.get(id=self.kwargs["pk"])
        logged_in_user_id = self.request.user.id

        if logged_in_user_id and logged_in_user_id == self.kwargs["pk"]:
            user_blogs = Blog.objects.filter(
                Q(author_id=self.kwargs.get("pk"))
                & Q(author=self.request.user))
        else:
            user_blogs = Blog.active_objects.filter(author_id=self.kwargs.get("pk"))
        context["user_detail"] = profile.author
        context["total_comments"] = Comment.objects.filter(blog__author=self.kwargs['pk']).count()
        context["user_form"] = UserForm(instance=current_user)
        context["profile"] = profile
        context["user_blogs"] = user_blogs
        context["profile_form"] = ProfileForm(instance=profile)
        return context


class BlogPostDetailPage(View):
    def get(self, request, slug):
        blog = Blog.objects.get(slug=slug)
        current_user = self.request.user

        if self.request.user != blog.author:
            comments = Comment.active_comments.filter(blog=blog).order_by("-post_date")
        else:
            comments = Comment.objects.filter(blog=blog).order_by("-post_date")

        context = {
            "blog": blog,
            "comment_form": CommentForm(),
            "comments": comments,
            "current_user": current_user,
            "slug": slug
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


class UpdateBlogView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    form_class = BlogUpdateForm
    template_name = "blog/blog_edit.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(UpdateBlogView, self).form_valid(form)

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False


class BloggersListView(ListView):
    model = User
    template_name = "blog/user_list.html"
    ordering = ["first_name"]


class ProfileUpdateView(View):
    def get(self, request):
        profile = Profile.objects.get(author_id=self.request.user.id)
        current_user = User.objects.get(id=self.request.user.id)
        profile_form = ProfileForm(instance=profile)
        user_form = UserForm(instance=current_user)

        context = {
            "user_form": user_form,
            "profile_form": profile_form,
        }
        return render(request, "blog/profile_edit.html", context)

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=self.request.user.id)
        user_profile = Profile.objects.get(author_id=self.request.user.id)

        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse("blog:author-detail", args=[self.request.user.id]))

        context = {
            'profile_form': profile_form,
            'user_form': user_form
        }
        return render(request, "blog/user_detail.html", context)


class ToggleComment(View):
    def post(self, request, pk, slug):
        comment = Comment.objects.get(pk=pk)
        
        if comment.is_delete:
            comment.is_delete = False
        elif not comment.is_delete:
            comment.is_delete = True
        comment.save()
        return HttpResponseRedirect(reverse("blog:blog-detail", args=[slug]))

# logging in, logging out
# admin site

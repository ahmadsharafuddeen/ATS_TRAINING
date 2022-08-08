from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image


class ActiveObjects(models.Manager):
    def get_queryset(self):
        return super(ActiveObjects, self).get_queryset().filter(is_delete=False)


class AllObjects(models.Manager):
    def get_queryset(self):
        return super(AllObjects, self).get_queryset()


class Profile(models.Model):
    passport = models.ImageField(upload_to="profiles", null=True, blank=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)

    def save(self, *args, **kwargs):
        super().save()
        if self.passport:
            img = Image.open(self.passport.path)

            if img.height > 200 or img.width > 200:
                new_img = (200, 200)
                img.thumbnail(new_img)
                img.save(self.passport.path)

    def __str__(self):
        return self.author.username


@receiver(post_save, sender=User)
def profile_save(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(author=instance)


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="articles", null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, max_length=100, blank=True)
    content = models.TextField(validators=[MinLengthValidator(10)])

    objects = AllObjects()
    active_objects = ActiveObjects()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="blogs")

    class Meta:
        ordering = ["title", "author"]

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("blog:blog-detail", args=[str(self.slug)])


class Comment(models.Model):
    text = models.TextField(max_length=400)
    post_date = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)
    comment_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null="True", related_name="comments", editable=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments", editable=False)

    objects = AllObjects()
    active_comments = ActiveObjects()

    class Meta:
        ordering = ["post_date"]

    def get_absolute_url(self):
        return reverse("blog:toggle-comment", args=[])

    def __str__(self):
        return f"{self.text} {self.comment_owner.username}"

from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator


class MyProfile(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    status = models.CharField(max_length=20, default="single", choices=(("single","single"),
            ("married","married"),("committed","committed"),("divorced","divorced"),("widow","widow")))
    gender = models.CharField(max_length=20, default="male", choices=(("male", "male"),
                                                                        ("female", "female")))
    age = models.IntegerField(default=18, validators=[MinValueValidator(18), MaxValueValidator(100)])
    address = models.TextField(null=True, blank=True)
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=15, null=True, blank=True)
    pic = models.ImageField(upload_to="images\\", null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "%s (%s)" % (self.user, self.age)


class MyPost(models.Model):
    pic = models.ImageField(upload_to="images\\", null=True)
    subject = models.CharField(max_length=200)
    msg = models.TextField(null=True, blank=True)
    cr_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(to=User, on_delete=CASCADE)

    def __str__(self):
        return "%s " % self.subject


class PostComment(models.Model):
    post = models.ForeignKey(to=MyPost, on_delete=CASCADE)
    msg = models.TextField()
    cr_date = models.DateTimeField(auto_now_add=True)
    commented_by = models.ForeignKey(to=User, on_delete=CASCADE)
    flag = models.CharField(max_length=20,null=True, blank=True, choices=(("racist", "racist"),
                                                                      ("abusive", "abusive")))

    def __str__(self):
        return "%s " % self.msg


class PostLike(models.Model):
    post = models.ForeignKey(to=MyPost, on_delete=CASCADE)
    liked_by = models.ForeignKey(to=User, on_delete=CASCADE)
    cr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s " % self.liked_by


class FollowUser(models.Model):
    profile = models.ForeignKey(to=MyProfile, on_delete=CASCADE)
    followed_by = models.ForeignKey(to=User, on_delete=CASCADE)

    def __str__(self):
        return "%s " % self.followed_by
from django.db import models
import datetime

# Create your models here.

class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)
    truename =models.CharField(max_length=128, default='')
    birthday = models.DateTimeField(default=datetime.datetime.now())
    job = models.CharField(max_length=128, default='无')
    jianjie = models.TextField(max_length=2000, default='')
    diqu = models.CharField(max_length=128, default='')
    touxiang = models.CharField(max_length=128,default='1.jpg')


    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:

        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"

class Follow(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    follow = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follows')
    status = models.BooleanField()
    c_time = models.DateTimeField(auto_now_add=True)
    ch_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name + '关注' + self.follow.name
    class Meta:
        verbose_name_plural = '关注'
        verbose_name = '关注'

class Fan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fans = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fans')
    status = models.BooleanField()
    c_time = models.DateTimeField(auto_now_add=True)
    ch_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fans.name + '粉'+self.user.name

    class Meta:
        verbose_name = '粉丝'
        verbose_name_plural = '粉丝'

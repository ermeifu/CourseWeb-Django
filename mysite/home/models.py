from django.db import models

# Create your models here.


class Menu(models.Model):
    pattern = models.CharField(max_length=50)
    parentId = models.IntegerField(null=True)
    enabled = models.BooleanField(default=True)
    name = models.CharField(max_length=20)
    component = models.CharField(max_length=20, null=True)

    class Meta:
        verbose_name_plural = "菜单管理"

    def __str__(self):
        return self.name


class Home(models.Model):
    pattern = models.CharField(max_length=50)
    parentId = models.IntegerField(null=True)
    enabled = models.IntegerField()
    name = models.CharField(max_length=20)
    component = models.CharField(max_length=20, null=True)

    class Meta:
        verbose_name_plural = ""

    def __str__(self):
        return self.name


class CourseMessage(models.Model):
    name = models.CharField(max_length=30)
    courseIntro = models.CharField(max_length=255)
    introImg = models.URLField()
    recommendedBookIntro = models.CharField(max_length=255)
    recommendedTextbook = models.URLField()

    class Meta:
        verbose_name_plural = "课程信息"

    def __str__(self):
        return self.name


class HomeImages(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()

    class Meta:
        verbose_name_plural = "首页图片"

    def __str__(self):
        return self.name


class TeachingResources(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    class Meta:
        verbose_name_plural = "教学资源"

    def __str__(self):
        return self.name


class ReferenceBooks(models.Model):
    name = models.CharField(max_length=100)
    img = models.URLField()

    class Meta:
        verbose_name_plural = "参考书"

    def __str__(self):
        return self.name

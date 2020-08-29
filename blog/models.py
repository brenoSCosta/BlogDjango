from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe


class Category(models.Model):
    name = models.CharField(max_length=100)
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Post(models.Model):
    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado')
    )
    title = models.CharField(max_length=250, verbose_name='Título')
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    content = RichTextField(verbose_name='Conteúdo')
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS,
                              default='rascunho')
    categoria = models.ManyToManyField(Category, related_name="get_posts")
    image = models.ImageField(upload_to='blog', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def get_absolute_url_update(self):
        return reverse('post_edit', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def view_image(self):
        return mark_safe("<img src='%s' width='400px' />" % self.image.url)

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

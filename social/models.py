from django.db import models


class Link(models.Model):
    key = models.SlugField(verbose_name='Identificação Rede', max_length=100, unique=True)
    description = models.CharField(max_length=100, verbose_name='Descrição')
    url = models.URLField(max_length=200, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
        ordering = ['key']

    def __str__(self):
        return self.key

from django.db import models
from django.utils.text import slugify
from django.urls import reverse



class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    image = models.CharField(max_length=150)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # автоматическое заполнение SLUG
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('phone', args=[self.slug])

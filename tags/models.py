from django.db import models
from product.utils import upload_image_path, unique_slug_generator
from django.db.models.signals import pre_save, post_save
from product.models import Product
# Create your models here.


class SearchTags(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Search Tags'


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=SearchTags)

from django.db import models

# Create your models here.







class Category(models.Model):
    title=models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Chocolate(models.Model):
    title=models.CharField(max_length=200)
    category=models.ForeignKey(Category,related_name='chocolates',on_delete=models.CASCADE)
    descriprion=models.CharField(max_length=500)
    price=models.FloatField(null=True,blank=True)
    image_url=models.URLField(max_length=2083)
    choco_available=models.BooleanField()
    is_deleted=models.BooleanField()
    cart = models.ForeignKey('Cart', related_name='chocolate_items', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def name(self):
        return self.title

# cart add
class Cart(models.Model):
    chocolates = models.ManyToManyField(Chocolate, related_name='carts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id}"
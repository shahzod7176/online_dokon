from django.db.models import Model, CharField, SlugField, ImageField, ForeignKey, CASCADE, TextField, IntegerField, \
    EmailField
from django.utils.text import slugify


class Category(Model):
    name = CharField(max_length=255)
    slug = SlugField(unique=True, blank=True)
    image = ImageField(upload_to='images/')
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Shoes(Model):
    name = CharField(max_length=255)
    slug = SlugField(unique=True, blank=True)
    type = ForeignKey(Category, CASCADE)
    character = TextField()
    Uz = 'som'
    Ru = '&'
    En = '$'
    the_price = (
        (Uz, 'som'),
        (Ru, '&'),
        (En, '$'),
    )
    price_type = CharField(max_length=10, choices=the_price, default='som')
    price = IntegerField()
    image = ImageField()

class Buy(Model):
    name = CharField(max_length=255)
    phone = CharField(max_length=255)
    product = ForeignKey(Shoes, CASCADE, null=True)
    ALL_SIZES = (
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        ('45', '45'),
    )
    size = CharField(max_length=100, choices=ALL_SIZES)
    ALL_VALUES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
    )
    how = CharField(max_length=100, choices=ALL_VALUES)
    map = TextField()
    email = EmailField(blank=True)

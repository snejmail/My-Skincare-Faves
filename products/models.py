from django.db import models


class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('cleanser', 'Cleanser'),
        ('moisturizer', 'Moisturizer'),
        ('night cream', 'Night Cream'),
        ('serum', 'Serum'),
        ('toner', 'Toner'),
        ('mask', 'Mask'),
        ('sunscreen', 'Sunscreen'),
        ('eye cream', 'Eye Cream'),
        ('other', 'Other'),
    ]
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    product_type = models.CharField(
        max_length=20,
        choices=PRODUCT_TYPE_CHOICES,
        null=False,
        blank=False,
    )
    package_size_in_milliliters = models.IntegerField(
        blank=False,
        null=False,
        default=0,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    key_ingredients = models.TextField(
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Like(models.Model):
    pass


class Review(models.Model):
    pass

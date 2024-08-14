from django.db import models
from django.utils import timezone

from users.models import User


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
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='likes',
    )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='likes',
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'


class Review(models.Model):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )
    text = models.TextField()
    created_at = models.DateTimeField(
        default=timezone.now,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'product'], name='unique_review'
            )
        ]

    def __str__(self):
        return f"Review by {self.user} on {self.product.name}"

# Generated by Django 4.2.2 on 2024-07-10 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='key_ingredients',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('cleanser', 'Cleanser'), ('moisturizer', 'Moisturizer'), ('night cream', 'Night Cream'), ('serum', 'Serum'), ('toner', 'Toner'), ('mask', 'Mask'), ('sunscreen', 'Sunscreen'), ('eye cream', 'Eye Cream'), ('other', 'Other')], default='', max_length=20),
        ),
    ]

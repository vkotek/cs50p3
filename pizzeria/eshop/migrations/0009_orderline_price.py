# Generated by Django 3.0.4 on 2020-05-11 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0008_auto_20200511_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderline',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
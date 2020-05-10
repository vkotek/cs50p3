# Generated by Django 3.0.4 on 2020-05-02 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0005_auto_20200502_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemtopping',
            name='allowed_category',
        ),
        migrations.RemoveField(
            model_name='orderline',
            name='price',
        ),
        migrations.AddField(
            model_name='itemtopping',
            name='allowed_parent',
            field=models.ManyToManyField(to='eshop.Category'),
        ),
        migrations.AlterField(
            model_name='orderline',
            name='toppings',
            field=models.ManyToManyField(blank=True, to='eshop.ItemTopping'),
        ),
    ]
# Generated by Django 3.0.4 on 2020-05-02 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0004_auto_20200502_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemtopping',
            name='allowed_parents',
        ),
        migrations.AddField(
            model_name='itemtopping',
            name='allowed_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eshop.Category'),
        ),
    ]

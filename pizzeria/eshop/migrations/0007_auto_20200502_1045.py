# Generated by Django 3.0.4 on 2020-05-02 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0006_auto_20200502_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemtopping',
            name='allowed_parent',
        ),
        migrations.AddField(
            model_name='itemtopping',
            name='allowed_category',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='eshop.Category'),
        ),
    ]

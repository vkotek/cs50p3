# Generated by Django 3.0.4 on 2020-05-01 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='order_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='eshop.Order'),
        ),
    ]

# Generated by Django 2.1.1 on 2018-11-05 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0003_payment_noted'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sale',
            name='saleprofit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

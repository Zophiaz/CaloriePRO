# Generated by Django 3.0.6 on 2020-07-28 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CaloriePRO', '0008_userfooditem'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfooditem',
            name='customer',
            field=models.ManyToManyField(blank=True, null=True, to='CaloriePRO.Customer'),
        ),
    ]

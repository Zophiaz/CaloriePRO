# Generated by Django 3.0.6 on 2020-07-25 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CaloriePRO', '0006_auto_20200725_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='calorie',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
    ]

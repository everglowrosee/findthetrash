# Generated by Django 2.2.5 on 2021-12-07 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='coupon',
            field=models.IntegerField(blank=True, null=True, verbose_name='쿠폰'),
        ),
    ]

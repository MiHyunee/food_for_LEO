# Generated by Django 2.2.9 on 2020-02-21 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200221_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='like', to='mypage.Profile'),
        ),
    ]

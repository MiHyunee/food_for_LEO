# Generated by Django 2.2.9 on 2020-02-17 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0005_auto_20200217_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mypage.Profile'),
        ),
    ]

# Generated by Django 2.2.1 on 2019-05-03 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djuc', '0003_auto_20190503_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0013_auto_20200418_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcontactinfo',
            name='message',
            field=models.TextField(max_length=700),
        ),
    ]

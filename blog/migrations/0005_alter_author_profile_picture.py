# Generated by Django 4.1.6 on 2023-02-08 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_author_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_picture',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]

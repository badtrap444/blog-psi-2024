# Generated by Django 5.1.2 on 2024-10-12 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['id'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]

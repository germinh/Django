# Generated by Django 4.2.5 on 2023-09-15 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_rename_author_name_blog_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='End_Date',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='Start_Date',
        ),
    ]
# Generated by Django 5.0.3 on 2024-04-27 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0004_rename_c1_detail_category_remove_detail_c2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='Category',
        ),
    ]
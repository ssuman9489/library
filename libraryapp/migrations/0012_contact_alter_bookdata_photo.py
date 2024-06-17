# Generated by Django 5.0.3 on 2024-05-27 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0011_alter_details_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('message', models.CharField(max_length=50000)),
            ],
        ),
        migrations.AlterField(
            model_name='bookdata',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='book_photos/'),
        ),
    ]
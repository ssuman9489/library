# Generated by Django 5.0.3 on 2024-04-28 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0005_remove_detail_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Username', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=20)),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=20)),
                ('Language', models.CharField(max_length=50)),
                ('Aadhar', models.IntegerField()),
                ('Phone', models.IntegerField()),
                ('Profilepic', models.ImageField(blank=True, upload_to='profile_pics')),
            ],
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
    ]

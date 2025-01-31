# Generated by Django 5.0.6 on 2024-06-06 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('image_url', models.URLField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('type', models.CharField(max_length=60)),
                ('brand', models.CharField(max_length=15)),
                ('price', models.FloatField(max_length=15)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]

# Generated by Django 4.2.9 on 2024-01-09 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='photos/product')),
                ('stock', models.IntegerField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Passive', 'Passive'), ('Modified', 'Modified')], default='Active', max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.subcategory')),
            ],
        ),
    ]

# Generated by Django 3.1 on 2022-01-18 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=55, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='images')),
                ('kkal', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('in stock', 'В наличии'), ('out of stock', 'Нет в наличии')], max_length=15)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='menu.category')),
            ],
        ),
    ]

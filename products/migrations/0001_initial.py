# Generated by Django 4.0.3 on 2022-03-10 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('weight', models.FloatField()),
                ('price', models.PositiveIntegerField()),
                ('is_stock', models.BooleanField(default=True)),
                ('valid_until', models.DateField()),
            ],
        ),
    ]

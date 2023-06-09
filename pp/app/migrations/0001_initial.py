# Generated by Django 4.2 on 2023-05-02 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('prodapp', models.TextField(default='')),
                ('category', models.TextField(choices=[('AR', 'ART'), ('RP', 'Realistic Picture'), ('O', 'Other')], max_length=2)),
                ('image', models.ImageField(upload_to='product')),
            ],
        ),
    ]

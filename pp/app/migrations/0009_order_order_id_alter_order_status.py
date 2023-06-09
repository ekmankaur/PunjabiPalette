# Generated by Django 4.2 on 2023-06-05 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('IN_PROGRESS', 'In Progress'), ('DELIVERED', 'Delivered')], default='IN_PROGRESS', max_length=20),
        ),
    ]

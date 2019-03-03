# Generated by Django 2.1.3 on 2019-03-03 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('PUB', 'Published'), ('PEN', 'Pending')], default='PUB', max_length=3),
        ),
    ]
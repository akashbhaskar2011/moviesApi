# Generated by Django 4.2.6 on 2024-08-01 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviedata_typ'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='image',
            field=models.ImageField(default='images/none/noimage.jpg', upload_to='images/'),
        ),
    ]
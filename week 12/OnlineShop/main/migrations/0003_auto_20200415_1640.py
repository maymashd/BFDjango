# Generated by Django 2.0 on 2020-04-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200415_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, default='https://webstore.iea.org/content/images/thumbs/default-image_450.png', null=True, upload_to='user_photos/'),
        ),
    ]
# Generated by Django 2.0 on 2020-04-14 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='logo',
            field=models.ImageField(default='https://lh3.googleusercontent.com/proxy/YjOBOYr3TkjLILcZrpoxJuFb1Qxcbnp31MwHqb4t2AI8gOf1GM3KXdEXn50FXjXRanoo_P-aU1q26AyuGGflMNVyQQJGSyuzu9YHFfir8_Jp7pGBTikouXuSnobauyoSQubJBo7-LL84dszGp-IwSZgzTfz6PoG3BucQulijXLBTuHK1g9extlCN8T1NbEP0b_i-rNl94m8C4s6cd0HguiIBzL1E7qRR8wvGVvZeuy5dtXMqjNCEy40', upload_to='photos/'),
        ),
    ]

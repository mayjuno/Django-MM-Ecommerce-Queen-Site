# Generated by Django 3.2.8 on 2021-10-27 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20211027_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='myanmar_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]

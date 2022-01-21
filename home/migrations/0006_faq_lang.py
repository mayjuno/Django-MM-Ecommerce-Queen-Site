# Generated by Django 3.2.8 on 2021-10-30 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_settinglang'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='lang',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('my', 'Myanmar')], max_length=6, null=True),
        ),
    ]
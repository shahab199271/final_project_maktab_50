# Generated by Django 3.2.5 on 2021-08-05 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quote',
            options={'ordering': ['registration_date']},
        ),
        migrations.AlterModelOptions(
            name='quoteitem',
            options={'ordering': ['price_after_tax']},
        ),
    ]

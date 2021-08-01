# Generated by Django 3.2.5 on 2021-07-29 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pdf_file',
            field=models.FileField(upload_to='files/pdf_files/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic_file',
            field=models.FileField(upload_to='files/pic_files/%Y/%m/%d'),
        ),
    ]
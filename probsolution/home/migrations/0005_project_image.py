# Generated by Django 3.2.20 on 2023-11-17 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_taskitem_project_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default='D:\\Projects\\socialmedia\\socialmedia\\media\\NoneImage.jpg', null=True, upload_to='posts/'),
        ),
    ]

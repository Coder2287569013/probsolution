# Generated by Django 3.2.20 on 2023-10-27 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_taskitem_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='project_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.project'),
        ),
    ]

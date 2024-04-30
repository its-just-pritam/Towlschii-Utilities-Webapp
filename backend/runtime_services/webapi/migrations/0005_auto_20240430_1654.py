# Generated by Django 3.2.12 on 2024-04-30 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0004_auto_20240427_1358'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Companies',
            new_name='Company',
        ),
        migrations.AlterModelOptions(
            name='applicationstatus',
            options={'verbose_name_plural': 'ApplicationStatuses'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='jobapplication',
            options={'verbose_name_plural': 'JobApplications'},
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='ctc',
            field=models.IntegerField(),
        ),
    ]
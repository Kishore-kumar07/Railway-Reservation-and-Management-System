# Generated by Django 4.1.1 on 2022-10-15 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addtrn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='traindetails',
            name='fare',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='traindetails',
            name='trno',
            field=models.IntegerField(null=True),
        ),
    ]

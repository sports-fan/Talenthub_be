# Generated by Django 2.2.7 on 2021-03-22 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0014_auto_20210322_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='created_at',
            field=models.DateField(null=True),
        ),
    ]

# Generated by Django 2.2.7 on 2021-01-31 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0007_auto_20210131_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='related_financial',
            new_name='financial_request',
        ),
        migrations.AlterField(
            model_name='client',
            name='started_at',
            field=models.DateField(),
        ),
    ]

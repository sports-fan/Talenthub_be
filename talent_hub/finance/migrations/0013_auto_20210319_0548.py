# Generated by Django 2.2.7 on 2021-03-19 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0012_auto_20210318_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='payment_platform',
            field=models.CharField(choices=[('paypal', 'Paypal'), ('payoneer', 'Payoneer'), ('upwork', 'Upwork'), ('freelancer', 'Freelancer'), ('toptal', 'Toptal'), ('bitcoin', 'Bitcoin')], max_length=10),
        ),
    ]

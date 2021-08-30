# Generated by Django 2.2.7 on 2021-08-30 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.TextField(null=True)),
                ('achievements', models.TextField(null=True)),
                ('log_type', models.CharField(choices=[('plan', 'Plan'), ('report', 'Report')], max_length=20)),
                ('created_at', models.DateField(verbose_name='Created Date of Log')),
                ('interval', models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 2.2.7 on 2021-01-22 23:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Individual'), (2, 'Company')])),
                ('full_name', models.CharField(max_length=50)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('started_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinancialRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Send Invoice'), (2, 'Send Payment'), (3, 'Direct Invoice')])),
                ('status', models.IntegerField(choices=[(1, 'Pending'), (2, 'Approved'), (3, 'Declined'), (4, 'Canceled')], default=1)),
                ('amount', models.FloatField(null=True)),
                ('counter_party', models.CharField(max_length=50)),
                ('requested_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('dob', models.DateField()),
                ('phone_num', models.CharField(max_length=50, null=True)),
                ('contact_method', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('type', models.IntegerField(choices=[(1, 'Budget'), (2, 'Hourly FT'), (3, 'Hourly PT'), (4, 'Contract')])),
                ('price', models.FloatField(null=True)),
                ('started_at', models.DateField(null=True)),
                ('ended_at', models.DateField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Ongoing'), (2, 'Paused'), (3, 'Ended')])),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Client')),
                ('participants', models.ManyToManyField(related_name='related_participants', to=settings.AUTH_USER_MODEL)),
                ('project_starter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_project_starter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('gross_amount', models.FloatField()),
                ('net_amount', models.FloatField()),
                ('payment_platform', models.CharField(choices=[('paypal', 'Paypal'), ('payoneer', 'Payoneer'), ('upwork', 'Upwork'), ('freelancer', 'Freelancer'), ('toptal', 'Toptal')], max_length=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Client')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.Project')),
                ('related_financial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.FinancialRequest')),
            ],
        ),
    ]

# Generated by Django 2.2.7 on 2021-12-16 16:39

from django.db import migrations, models
from django.db.models import Subquery, OuterRef
import django.db.models.deletion


def forward_func(apps, schema_editor):
    Transaction = apps.get_model('finance', 'Transaction')
    Transaction.objects.all().update(
        address=Subquery(Transaction.objects.filter(pk=OuterRef('pk')).values('financial_request__address')[:1])
    )
    Transaction.objects.all().update(
        owner=Subquery(Transaction.objects.filter(pk=OuterRef('pk')).values('financial_request__requester')[:1])
    )
    Transaction.objects.all().update(
        project=Subquery(Transaction.objects.filter(pk=OuterRef('pk')).values('financial_request__project')[:1])
    )

class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0018_auto_20211216_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='address',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='owner',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='project',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.RunPython(forward_func),
    ]

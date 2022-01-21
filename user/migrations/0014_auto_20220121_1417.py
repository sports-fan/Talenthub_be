# Generated by Django 2.2.7 on 2022-01-21 14:17

from django.db import migrations

from ..constants import PLATFORM_TYPES_DICT, PLATFORM_TYPES, PLATFORM_TYPES_TUPLE


def fill_account_platform(apps, schema_editor):
    Account = apps.get_model('user', 'Account')
    AccountPlatform = apps.get_model('user', 'AccountPlatform')
    for account in Account.objects.all():
        account.account_platform, created = AccountPlatform.objects.get_or_create(name=PLATFORM_TYPES_DICT[account.platform_type])
        account.save()

    for platform in PLATFORM_TYPES_TUPLE:
        AccountPlatform.objects.get_or_create(name=platform)


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20220121_1049'),
    ]

    operations = [
        migrations.RunPython(fill_account_platform, migrations.RunPython.noop),
    ]

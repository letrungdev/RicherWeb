# Generated by Django 3.2.9 on 2022-07-12 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0011_auto_20220611_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='kind',
            field=models.CharField(max_length=40, null=True),
        ),
    ]

# Generated by Django 3.2.9 on 2022-07-17 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0013_alter_transaction_amount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Expenditureplan',
        ),
        migrations.RemoveField(
            model_name='analysis',
            name='content',
        ),
        migrations.RemoveField(
            model_name='analysis',
            name='type',
        ),
        migrations.AddField(
            model_name='analysis',
            name='interval',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='analysis',
            name='ratio',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='analysis',
            name='user',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
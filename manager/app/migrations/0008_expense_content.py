# Generated by Django 4.2.2 on 2023-06-25 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_expense_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='content',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-23 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_book_created_at_alter_rate_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Description'),
        ),
    ]

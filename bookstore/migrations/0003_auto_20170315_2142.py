# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 21:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_remove_books_isbn_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='publication_year',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='purchase_items',
        ),
        migrations.AddField(
            model_name='orders',
            name='book',
            field=models.ManyToManyField(to='bookstore.Books'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.Customers'),
        ),
    ]

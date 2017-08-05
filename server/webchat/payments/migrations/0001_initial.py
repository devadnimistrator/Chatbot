# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 17:08
from __future__ import unicode_literals

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=1, default=Decimal('0.00'), max_digits=20)),
                ('trx_id', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_account', models.CharField(blank=True, max_length=255, null=True)),
                ('recipient_id', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('transferred', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('1', 'Failed'), ('2', 'Success'), ('3', 'Pending')], default='1', max_length=1)),
                ('history', jsonfield.fields.JSONField(default={}, help_text='JSON containing response Card from stripe', verbose_name='Response')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('widget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_widget', to='portal.Widget')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
    ]
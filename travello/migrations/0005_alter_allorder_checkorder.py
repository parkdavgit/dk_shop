# Generated by Django 3.2.25 on 2025-04-15 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_allorder_checkorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allorder',
            name='checkorder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Allorder_checkorder', to='travello.checkorder'),
        ),
    ]

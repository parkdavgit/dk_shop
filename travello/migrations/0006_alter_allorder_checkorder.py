# Generated by Django 3.2.25 on 2025-04-26 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0005_alter_allorder_checkorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allorder',
            name='checkorder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travello.checkorder'),
        ),
    ]

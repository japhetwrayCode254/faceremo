# Generated by Django 4.0.5 on 2024-03-22 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_recordadditionalinfo_record_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordadditionalinfo',
            name='record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_info', to='webapp.record'),
        ),
    ]
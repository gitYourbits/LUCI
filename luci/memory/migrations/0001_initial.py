# Generated by Django 5.1.4 on 2024-12-19 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectMemory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=255)),
                ('projectPath', models.CharField(max_length=1024)),
                ('lastUpdated', models.DateTimeField(auto_now=True)),
                ('memoryData', models.JSONField(default=dict)),
            ],
        ),
    ]

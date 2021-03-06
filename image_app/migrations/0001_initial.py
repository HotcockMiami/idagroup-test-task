# Generated by Django 3.1.2 on 2020-10-07 08:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_orig', models.ImageField(blank=True, null=True, upload_to='images_orig/')),
                ('image_resized', models.ImageField(blank=True, null=True, upload_to='images_resized')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]

# Generated by Django 3.2.7 on 2021-10-04 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_houses_photo_preview'),
    ]

    operations = [
        migrations.RenameField(
            model_name='houses',
            old_name='photo_preview',
            new_name='photo',
        ),
        migrations.AddField(
            model_name='houses',
            name='central_heat',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='houses',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='houses',
            name='pets_allow',
            field=models.BooleanField(default=False, null=True),
        ),
    ]

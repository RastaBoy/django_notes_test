# Generated by Django 4.2.7 on 2023-11-16 15:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_user_note_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['dt_create'], 'verbose_name': 'Заметки', 'verbose_name_plural': 'Заметки'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователи', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AddField(
            model_name='user',
            name='dt_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.2.7 on 2023-11-29 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.CharField(auto_created=True, default='YHIOLYHTPDJP', max_length=15, primary_key=True, serialize=False)),
                ('device_type', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=15)),
                ('message_type', models.CharField(choices=[('SWITCH_ON', 'SWITCH_ON'), ('SWITCH_OFF', 'SWITCH_OFF'), ('CHANGE_COLOR', 'CHANGE_COLOR'), ('PLAY_SONG', 'PLAY_SONG'), ('OPEN', 'OPEN'), ('CLOSE', 'CLOSE')], max_length=15)),
                ('message', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

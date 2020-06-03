# Generated by Django 3.0.4 on 2020-06-03 20:32

import channels_app.models
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_identifier', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('storedprocedure_file', models.FileField(null=True, upload_to='channels')),
                ('channel_status', models.CharField(choices=[('ACTIVE', 'Channel is open and active, currently sending events out'), ('INACTIVE', 'Channel has been created, but is not active')], default='INACTIVE', max_length=16)),
                ('json_payload', django.contrib.postgres.fields.jsonb.JSONField(default=channels_app.models.default_channels_json_payload)),
            ],
        ),
    ]

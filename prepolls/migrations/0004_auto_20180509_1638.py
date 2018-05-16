# Generated by Django 2.0.2 on 2018-05-09 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prepolls', '0003_auto_20180509_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainuser',
            name='user',
        ),
        migrations.AddField(
            model_name='prevoter',
            name='iscorrect',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='prevoter',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='TrainUser',
        ),
    ]

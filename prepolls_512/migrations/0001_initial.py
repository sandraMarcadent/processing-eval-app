# Generated by Django 2.0.2 on 2018-05-10 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PreVoter512',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(default='unknown', max_length=200)),
                ('iscorrect', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('is_last', models.BooleanField(default=True)),
                ('image_class', models.CharField(default='unknown', max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('image', models.ImageField(upload_to='prepolls_512')),
            ],
        ),
        migrations.AddField(
            model_name='prevoter512',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prepolls_512.Question'),
        ),
        migrations.AddField(
            model_name='prevoter512',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prepolls_512.Question'),
        ),
    ]
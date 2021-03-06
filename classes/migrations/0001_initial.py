# Generated by Django 2.0.7 on 2018-07-19 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('title', models.CharField(default='', max_length=30, primary_key=True, serialize=False)),
                ('description', models.CharField(default='', max_length=500)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='teachers.Teacher')),
            ],
            options={
                'verbose_name': 'предмет',
                'verbose_name_plural': 'Предметы',
                'ordering': ['title'],
            },
        ),
    ]

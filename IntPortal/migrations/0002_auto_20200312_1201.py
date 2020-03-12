# Generated by Django 3.0.4 on 2020-03-12 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IntPortal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='date_Time_End',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='date_Time_Start',
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_Time_Start', models.DateTimeField()),
                ('date_Time_End', models.DateTimeField()),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='participants', to='IntPortal.Participant')),
            ],
        ),
    ]
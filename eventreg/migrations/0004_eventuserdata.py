# Generated by Django 3.1.3 on 2021-01-23 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventreg', '0003_eventdata_eventurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventUserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentName', models.CharField(max_length=264, unique=True)),
                ('studentReg', models.CharField(max_length=10, unique=True)),
                ('studentEmail', models.EmailField(max_length=254, unique=True)),
                ('studentRegistered', models.BooleanField(default=False)),
                ('studentCheckedIn', models.BooleanField(default=False)),
                ('eventName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventreg.eventdata')),
            ],
        ),
    ]

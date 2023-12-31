from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('srmsApp', '0002_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=250)),
                ('first_name', models.CharField(max_length=250)),
                ('middle_name', models.CharField(blank=True, max_length=250, null=True)),
                ('last_name', models.CharField(max_length=250)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=1, max_length=20)),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'Inactive')], default=1, max_length=2)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('classI', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srmsApp.class')),
            ],
        ),
    ]

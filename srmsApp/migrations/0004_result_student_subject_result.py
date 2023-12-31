from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('srmsApp', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srmsApp.student')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Subject_Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField(default=0)),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srmsApp.result')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='srmsApp.subject')),
            ],
        ),
    ]

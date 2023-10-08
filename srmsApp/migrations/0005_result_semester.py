from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srmsApp', '0004_result_student_subject_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='semester',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]

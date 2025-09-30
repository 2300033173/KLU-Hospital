

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointmentTime',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='appointment_images/'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointmentDate',
            field=models.DateField(null=True),
        ),
    ]

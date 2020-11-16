from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True)),
                ('firstname', models.TextField()),
                ('surname', models.TextField()),
                ('birthday', models.DateField()),
                ('photo', models.TextField())
            ]
        )
    ]
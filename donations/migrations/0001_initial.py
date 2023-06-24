# Generated by Django 4.2.1 on 2023-06-23 13:11

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
            name='Donation',
            fields=[
                ('d_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=200)),
                ('item_desc', models.CharField(max_length=500, null=True)),
                ('item_picture', models.ImageField(null=True, upload_to='item_pictures')),
                ('Location', models.TextField()),
                ('posted_date', models.DateField(blank=True, verbose_name='startdate(mm/dd/yyyy)')),
                ('createdby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
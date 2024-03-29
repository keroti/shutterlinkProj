# Generated by Django 4.2.5 on 2023-09-26 06:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shutterlinkApp', '0002_photographerprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographerprofile',
            name='bio',
            field=models.TextField(blank=True, default='Your default bio text'),
        ),
        migrations.AddField(
            model_name='photographerprofile',
            name='birth_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='photographerprofile',
            name='city',
            field=models.CharField(default='Your default city', max_length=255),
        ),
        migrations.AddField(
            model_name='photographerprofile',
            name='country',
            field=models.CharField(default='Your default country', max_length=255),
        ),
        migrations.AddField(
            model_name='photographerprofile',
            name='email',
            field=models.EmailField(default='yourdefault@email.com', max_length=254),
        ),
        migrations.AddField(
            model_name='photographerprofile',
            name='facebook',
            field=models.CharField(default='Your default Facebook', max_length=255),
        ),
        migrations.AddField(
            model_name='photographerprofile',
            name='instagram',
            field=models.CharField(default='Your default Instagram', max_length=255),
        ),
        migrations.AddField(
            model_name='photographerprofile',
            name='linkedin',
            field=models.CharField(default='Your default LinkedIn', max_length=255),
        ),
        migrations.AddField(
            model_name='photographerprofile',
            name='occupation',
            field=models.CharField(default='Your default occupation', max_length=255),
        ),
        migrations.AddField(
            model_name='photographerprofile',
            name='service_details',
            field=models.TextField(default='Your default service details'),
        ),
        migrations.AddField(
            model_name='photographerprofile',
            name='service_name',
            field=models.CharField(default='Your default service name', max_length=255),
        ),
        migrations.AddField(
            model_name='photographerprofile',
            name='twitter',
            field=models.CharField(default='Your default Twitter', max_length=255),
        ),
        migrations.AddField(
            model_name='photographerprofile',
            name='website',
            field=models.CharField(default='Your default website', max_length=255),
        ),
        migrations.AlterField(
            model_name='photographerprofile',
            name='brief_description',
            field=models.TextField(default='Your default brief description'),
        ),
        migrations.AlterField(
            model_name='photographerprofile',
            name='contact_information',
            field=models.CharField(default='Your default contact information', max_length=255),
        ),
        migrations.AlterField(
            model_name='photographerprofile',
            name='name',
            field=models.CharField(default='Your default name', max_length=255),
        ),
        migrations.AlterField(
            model_name='photographerprofile',
            name='profile_pic',
            field=models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pic/'),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-26 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shutterlinkApp', '0003_photographerprofile_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographerprofile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='photographerprofile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='photographerprofile',
            name='brief_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='photographerprofile',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='photographerprofile',
            name='contact_information',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='photographerprofile',
            name='country',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='photographerprofile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='photographerprofile',
            name='facebook',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='photographerprofile',
            name='instagram',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='photographerprofile',
            name='linkedin',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='photographerprofile',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='photographerprofile',
            name='occupation',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='photographerprofile',
            name='profile_pic',
            field=models.ImageField(upload_to='profile_pic/'),
        ),
        migrations.AlterField(
            model_name='photographerprofile',
            name='service_details',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='photographerprofile',
            name='service_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='photographerprofile',
            name='twitter',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='photographerprofile',
            name='website',
            field=models.CharField(max_length=255),
        ),
    ]

# Generated by Django 2.2.5 on 2019-09-12 06:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bulletinBoard', '0002_comment_remark_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='board',
            name='pub_date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 9, 12, 6, 47, 1, 275251, tzinfo=utc), verbose_name='dete published'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='remark_date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2019, 9, 12, 6, 47, 1, 275583, tzinfo=utc), verbose_name='date remarked'),
        ),
    ]

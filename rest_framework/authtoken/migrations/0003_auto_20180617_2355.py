# Generated by Django 2.0.6 on 2018-06-18 04:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
        ('authtoken', '0002_auto_20160226_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='business',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auth_token_business', to=settings.AUTH_USER_MODEL, verbose_name='Business'),
        ),
        migrations.AddField(
            model_name='token',
            name='contact',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auth_token_contact', to='category.Contacts', verbose_name='Contact'),
        ),
        migrations.AlterField(
            model_name='token',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auth_token_user', to='account.User', verbose_name='User'),
        ),
    ]
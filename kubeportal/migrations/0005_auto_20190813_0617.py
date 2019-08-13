# Generated by Django 2.2.4 on 2019-08-13 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('kubeportal', '0004_user_approval_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Approved by'),
        ),
        migrations.AlterField(
            model_name='user',
            name='service_account',
            field=models.ForeignKey(blank=True, help_text='Kubernetes namespace + service account of this user.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='kubeportal.KubernetesServiceAccount', verbose_name='Kubernetes account'),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=django_fsm.FSMField(default='not requested', help_text='The state of the cluster access approval workflow.', max_length=50, verbose_name='Cluster access'),
        ),
    ]

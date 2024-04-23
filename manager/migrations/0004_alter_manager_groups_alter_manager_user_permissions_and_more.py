# Generated by Django 5.0.4 on 2024-04-22 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('manager', '0003_manager_employee_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_number', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this manager belongs to. A manager will get all permissions granted to each of their groups.', related_name='manager_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this manager.', related_name='manager_user_permissions', to='auth.permission')),
            ],
        ),
    ]

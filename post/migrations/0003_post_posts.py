# Generated by Django 4.1.1 on 2022-09-13 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='posts',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.categories'),
            preserve_default=False,
        ),
    ]

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vegetables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('calories', models.IntegerField(default=0)),
                ('price', models.PositiveIntegerField(default=1)),
                ('is_avialable', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
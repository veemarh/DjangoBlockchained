
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_teacher_price_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='interests',
            field=models.ManyToManyField(related_name='interests_teacher', to='accounts.subject'),
        ),
    ]

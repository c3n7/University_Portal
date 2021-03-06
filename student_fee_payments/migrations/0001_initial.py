# Generated by Django 2.2.7 on 2019-11-26 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0002_auto_20191126_0241'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentFeePayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('learning_year', models.IntegerField(default=2019, verbose_name='Year of Study')),
                ('learning_semester', models.CharField(choices=[('Jan-Apr', 'Jan - Apr'), ('May-Aug', 'May - Aug'), ('Sept-Dec', 'Sept - Dec')], max_length=15, verbose_name='Semester of Study')),
                ('fee_amount', models.IntegerField(verbose_name='Amount Paid')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
            ],
        ),
    ]

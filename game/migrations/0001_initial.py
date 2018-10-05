# Generated by Django 2.1.1 on 2018-10-05 07:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator', models.CharField(max_length=20, unique=True, verbose_name='Developer')),
                ('parse', models.CharField(blank=True, max_length=20)),
                ('is_active', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Game Developer',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=12, unique=True, verbose_name='kode')),
                ('product_name', models.CharField(blank=True, help_text='Nama produk on website', max_length=200, verbose_name='produk')),
                ('nominal', models.PositiveIntegerField(default=0)),
                ('price', models.PositiveIntegerField(verbose_name='harga')),
                ('title', models.CharField(help_text='Nama produk on telegram / apps', max_length=200, verbose_name='title app')),
                ('description', models.TextField(blank=True, help_text='Deskripsi produk', max_length=500, verbose_name='deskripsi produk')),
                ('additional_info', models.TextField(blank=True, help_text='Optional', max_length=500)),
                ('is_active', models.BooleanField(default=False, verbose_name='aktif?')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Operator', verbose_name='developer')),
            ],
            options={
                'ordering': ['operator', 'nominal'],
                'verbose_name_plural': 'Produk Game',
            },
        ),
        migrations.CreateModel(
            name='ResponseTrx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_produk', models.CharField(max_length=200)),
                ('waktu', models.CharField(max_length=200)),
                ('no_hp', models.CharField(max_length=200)),
                ('sn', models.CharField(max_length=200)),
                ('ref1', models.CharField(max_length=200)),
                ('ref2', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('ket', models.CharField(max_length=200)),
                ('saldo_terpotong', models.PositiveIntegerField(default=0)),
                ('sisa_saldo', models.PositiveIntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Kode H2H Game', max_length=12, verbose_name='Kode')),
                ('product_name', models.CharField(blank=True, max_length=200, verbose_name='produk')),
                ('price', models.PositiveIntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Rajabiller Game',
            },
        ),
        migrations.CreateModel(
            name='StatusTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('IN', 'IN PROCESS'), ('PE', 'PENDING'), ('SS', 'SUCCESS'), ('FA', 'FAILED'), ('CA', 'CANCELED')], default='IN', max_length=2)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
                'get_latest_by': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trx_code', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(max_length=18)),
                ('price', models.PositiveIntegerField(default=0)),
                ('closed', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyergame', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Product')),
                ('record', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='salegame', to='sale.Sale')),
            ],
        ),
        migrations.AddField(
            model_name='statustransaction',
            name='trx',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Transaction'),
        ),
        migrations.AddField(
            model_name='responsetrx',
            name='trx',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game.Transaction'),
        ),
        migrations.AddField(
            model_name='product',
            name='server',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game.Server', verbose_name='raja biller'),
        ),
    ]

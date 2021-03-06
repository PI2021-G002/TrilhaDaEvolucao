# Generated by Django 3.2.8 on 2021-10-28 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaPrograma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=255)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AreaVoluntarioParceiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=15)),
                ('ano', models.IntegerField()),
                ('nro_membros', models.IntegerField()),
                ('acomp_concluido', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='VoluntarioParceiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=15)),
                ('disponibilidade', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AreaAtuacaoVoluntarioParceiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_area_vol_par', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='TrilhaDaEvolucao.areavoluntarioparceiro')),
                ('id_vol_par', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='TrilhaDaEvolucao.voluntarioparceiro')),
            ],
        ),
        migrations.CreateModel(
            name='AreaAcompanhamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concluido', models.BooleanField(default=False)),
                ('data_inicio', models.DateField(auto_now_add=True)),
                ('data_termino', models.DateField(blank=True, null=True)),
                ('observacao', models.CharField(max_length=255)),
                ('completude', models.FloatField(blank=True, null=True)),
                ('id_area_programa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='TrilhaDaEvolucao.areaprograma')),
                ('id_familia', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='TrilhaDaEvolucao.familia')),
            ],
        ),
        migrations.CreateModel(
            name='Agendamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateField()),
                ('tipo', models.CharField(max_length=1)),
                ('id_tipo', models.BigIntegerField()),
                ('id_familia', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='TrilhaDaEvolucao.familia')),
            ],
        ),
    ]

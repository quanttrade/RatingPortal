# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-14 08:34
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_auto_20171206_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='CRRecord_Bond1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime(2017, 12, 14, 8, 34, 49, 924042))),
                ('bond_code', models.CharField(max_length=20)),
                ('bond_type', models.CharField(max_length=20)),
                ('bond_name', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=30)),
                ('base_year', models.CharField(max_length=10)),
                ('intermediate_data_file', models.CharField(max_length=50)),
                ('internal_score_debt', models.FloatField()),
                ('internal_rating_debt', models.CharField(max_length=5)),
                ('internal_score_company', models.FloatField()),
                ('internal_rating_company', models.CharField(max_length=5)),
                ('external_rating_debt', models.CharField(max_length=5, null=True)),
                ('external_rating_company', models.CharField(max_length=5, null=True)),
                ('background', models.IntegerField()),
                ('background_remarks', models.CharField(max_length=50, null=True)),
                ('industry', models.IntegerField()),
                ('industry_remarks', models.CharField(max_length=50, null=True)),
                ('external_warranty', models.IntegerField()),
                ('external_warranty_remarks', models.CharField(max_length=50, null=True)),
                ('asset_warranty', models.IntegerField()),
                ('asset_warranty_remarks', models.CharField(max_length=50, null=True)),
                ('industry_boom', models.IntegerField()),
                ('industry_boom_remarks', models.CharField(max_length=50, null=True)),
                ('industry_prospects', models.IntegerField()),
                ('industry_prospects_remarks', models.CharField(max_length=50, null=True)),
                ('industry_rank', models.IntegerField()),
                ('industry_rank_remarks', models.CharField(max_length=50, null=True)),
                ('fund_usage', models.IntegerField()),
                ('fund_usage_remarks', models.CharField(max_length=50, null=True)),
                ('future_expenditure', models.IntegerField()),
                ('future_expenditure_remarks', models.CharField(max_length=50, null=True)),
                ('pct_major_shareholders', models.FloatField()),
                ('pct_profit_of_parent', models.FloatField()),
                ('total_asset', models.FloatField()),
                ('net_asset', models.FloatField()),
                ('net_asset_chg', models.FloatField()),
                ('revenue', models.FloatField()),
                ('net_profit', models.FloatField()),
                ('operating_profit', models.FloatField()),
                ('EBITDA', models.FloatField()),
                ('operating_cashflow', models.FloatField()),
                ('gross_margin', models.FloatField()),
                ('profit_margin', models.FloatField()),
                ('gross_margin_std', models.FloatField()),
                ('gross_margin_chg', models.FloatField()),
                ('roe', models.FloatField()),
                ('short_solvency_1', models.FloatField()),
                ('short_solvency_2', models.FloatField()),
                ('debt_ratio_with_interest', models.FloatField()),
                ('debt_ratio_with_interest_chg', models.FloatField()),
                ('debt_ratio', models.FloatField()),
                ('cost_ratio', models.FloatField()),
                ('fixed_asset_ratio', models.FloatField()),
                ('operating_cf_to_debt', models.FloatField()),
                ('operating_cf_std', models.FloatField()),
                ('ebitda_to_debt', models.FloatField()),
                ('fixed_asset_turnover', models.FloatField()),
                ('inventory_turnover_days', models.FloatField()),
                ('receivable_turnover_days', models.FloatField()),
                ('rest_credit_to_debt', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CRRecord_Bond2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime(2017, 12, 14, 8, 34, 49, 926042))),
                ('bond_code', models.CharField(max_length=20)),
                ('bond_type', models.CharField(max_length=20)),
                ('bond_name', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=30)),
                ('base_year', models.CharField(max_length=10)),
                ('intermediate_data_file', models.CharField(max_length=50)),
                ('internal_score_debt', models.FloatField()),
                ('internal_rating_debt', models.CharField(max_length=5)),
                ('internal_score_company', models.FloatField()),
                ('internal_rating_company', models.CharField(max_length=5)),
                ('external_rating_debt', models.CharField(max_length=5, null=True)),
                ('external_rating_company', models.CharField(max_length=5, null=True)),
                ('platform_status', models.IntegerField()),
                ('platform_status_remarks', models.CharField(max_length=50, null=True)),
                ('main_business', models.IntegerField()),
                ('main_business_remarks', models.CharField(max_length=50, null=True)),
                ('external_warranty', models.IntegerField()),
                ('external_warranty_remarks', models.CharField(max_length=50, null=True)),
                ('asset_warranty', models.IntegerField()),
                ('asset_warranty_remarks', models.CharField(max_length=50, null=True)),
                ('gov_fund_stability', models.IntegerField()),
                ('gov_fund_stability_remarks', models.CharField(max_length=50, null=True)),
                ('manual_adj', models.FloatField()),
                ('manual_adj_remarks', models.CharField(max_length=50, null=True)),
                ('GDP_amount', models.FloatField()),
                ('GDP_amount_remarks', models.CharField(max_length=50, null=True)),
                ('GDP_growth', models.FloatField()),
                ('GDP_growth_remarks', models.CharField(max_length=50, null=True)),
                ('public_revenue', models.FloatField()),
                ('public_revenue_remarks', models.CharField(max_length=50, null=True)),
                ('tax_to_revenue', models.FloatField()),
                ('tax_to_revenue_remarks', models.CharField(max_length=50, null=True)),
                ('total_asset', models.FloatField()),
                ('net_asset', models.FloatField()),
                ('net_asset_chg', models.FloatField()),
                ('revenue', models.FloatField()),
                ('net_profit', models.FloatField()),
                ('operating_profit', models.FloatField()),
                ('debt_ratio_with_interest', models.FloatField()),
                ('operating_cf_to_debt', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CRRecord_Bond3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime(2017, 12, 14, 8, 34, 49, 927044))),
                ('bond_code', models.CharField(max_length=20)),
                ('bond_type', models.CharField(max_length=20)),
                ('bond_name', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=30)),
                ('base_year', models.CharField(max_length=10)),
                ('intermediate_data_file', models.CharField(max_length=50)),
                ('internal_score_debt', models.FloatField()),
                ('internal_rating_debt', models.CharField(max_length=5)),
                ('internal_score_company', models.FloatField()),
                ('internal_rating_company', models.CharField(max_length=5)),
                ('external_rating_debt', models.CharField(max_length=5, null=True)),
                ('external_rating_company', models.CharField(max_length=5, null=True)),
                ('background', models.IntegerField()),
                ('background_remarks', models.CharField(max_length=50, null=True)),
                ('industry', models.IntegerField()),
                ('industry_remarks', models.CharField(max_length=50, null=True)),
                ('external_warranty', models.IntegerField()),
                ('external_warranty_remarks', models.CharField(max_length=50, null=True)),
                ('asset_warranty', models.IntegerField()),
                ('asset_warranty_remarks', models.CharField(max_length=50, null=True)),
                ('industry_boom', models.IntegerField()),
                ('industry_boom_remarks', models.CharField(max_length=50, null=True)),
                ('industry_prospects', models.IntegerField()),
                ('industry_prospects_remarks', models.CharField(max_length=50, null=True)),
                ('industry_rank', models.IntegerField()),
                ('industry_rank_remarks', models.CharField(max_length=50, null=True)),
                ('land_reserve', models.IntegerField()),
                ('land_reserve_remarks', models.CharField(max_length=50, null=True)),
                ('future_expenditure', models.IntegerField()),
                ('future_expenditure_remarks', models.CharField(max_length=50, null=True)),
                ('pct_major_shareholders', models.FloatField()),
                ('pct_profit_of_parent', models.FloatField()),
                ('total_asset', models.FloatField()),
                ('net_asset', models.FloatField()),
                ('net_asset_chg', models.FloatField()),
                ('revenue', models.FloatField()),
                ('net_profit', models.FloatField()),
                ('operating_profit', models.FloatField()),
                ('EBITDA', models.FloatField()),
                ('operating_cashflow', models.FloatField()),
                ('gross_margin', models.FloatField()),
                ('profit_margin', models.FloatField()),
                ('gross_margin_std', models.FloatField()),
                ('gross_margin_chg', models.FloatField()),
                ('roe', models.FloatField()),
                ('short_surplus', models.FloatField()),
                ('cash_to_short_debt', models.FloatField()),
                ('net_debt_ratio', models.FloatField()),
                ('net_debt_ratio_chg', models.FloatField()),
                ('debt_ratio', models.FloatField()),
                ('cost_ratio', models.FloatField()),
                ('fixed_asset_ratio', models.FloatField()),
                ('operating_cf_to_debt', models.FloatField()),
                ('operating_cf_std', models.FloatField()),
                ('ebitda_to_debt', models.FloatField()),
                ('fixed_asset_turnover', models.FloatField()),
                ('inventory_turnover_days', models.FloatField()),
                ('receivable_turnover_days', models.FloatField()),
                ('rest_credit_to_debt', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='crresult',
            name='record',
        ),
        migrations.AlterField(
            model_name='crrecord',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 14, 8, 34, 49, 922043)),
        ),
        migrations.AlterField(
            model_name='crresult',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 14, 8, 34, 49, 928036)),
        ),
        migrations.AddField(
            model_name='crresult',
            name='record_bond1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='record_bond1_id', to='account.CRRecord_Bond1'),
        ),
        migrations.AddField(
            model_name='crresult',
            name='record_bond2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='record_bond2_id', to='account.CRRecord_Bond2'),
        ),
        migrations.AddField(
            model_name='crresult',
            name='record_bond3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='record_bond3_id', to='account.CRRecord_Bond3'),
        ),
    ]

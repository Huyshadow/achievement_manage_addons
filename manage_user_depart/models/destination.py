from odoo import models, fields, api
import requests
import json
import os


class UserProvinceInfo(models.Model):
    _name = 'user.province.info'
    _description = 'User Province Info'

    name = fields.Char('Name', required=True)
    code = fields.Integer('Code', required=True)
    division_type = fields.Char('Division Type')
    codename = fields.Char('Codename')
    phone_code = fields.Integer('Phone Code')
    districts = fields.One2many(
        'user.district.info', 'province_id', 'Districts')


class UserDistrictInfo(models.Model):
    _name = 'user.district.info'
    _description = 'User District Info'

    name = fields.Char('Name', required=True)
    code = fields.Integer('Code', required=True)
    division_type = fields.Char('Division Type')
    codename = fields.Char('Codename')
    province_id = fields.Many2one('user.province.info', 'Province')
    wards = fields.One2many('user.ward.info', 'district_id', 'Wards')


class UserWardInfo(models.Model):
    _name = 'user.ward.info'
    _description = 'User Ward Info'

    name = fields.Char('Name', required=True)
    code = fields.Integer('Code', required=True)
    division_type = fields.Char('Division Type')
    codename = fields.Char('Codename')
    district_id = fields.Many2one('user.district.info', 'District')
    province_id = fields.Many2one('user.province.info', 'Province')

    @api.model
    def import_location_data(self):
        response = requests.get("https://provinces.open-api.vn/api/p/")
        response.raise_for_status()
        province_datas = response.json()

        for province_data in province_datas:
            response = requests.get(
                f"https://provinces.open-api.vn/api/p/{province_data['code']}?depth=3")
            response.raise_for_status()
            data = response.json()
            province_code = province_data['code']
            existing_province = self.env['user.province.info'].search(
                [('code', '=', province_code)], limit=1)

            if not existing_province:
                province = self.env['user.province.info'].create({
                    'name': province_data['name'],
                    'code': province_data['code'],
                    'division_type': province_data['division_type'],
                    'codename': province_data['codename'],
                    'phone_code': province_data['phone_code'],
                })
                for district_data in data['districts']:
                    district = self.env['user.district.info'].create({
                        'name': district_data['name'],
                        'code': district_data['code'],
                        'division_type': district_data['division_type'],
                        'codename': district_data['codename'],
                        'province_id': province.id,
                    })
                    for ward_data in district_data['wards']:
                        self.env['user.ward.info'].create({
                            'name': ward_data['name'],
                            'code': ward_data['code'],
                            'division_type': ward_data['division_type'],
                            'codename': ward_data['codename'],
                            'district_id': district.id,
                            'province_id': province.id,
                        })

from odoo import models, fields, api
import requests
import json
import os


class User(models.Model):
    _inherit = 'res.users'

    mssv_mscb = fields.Char(string="MSSV/MSCB", required=True)
    canhan_email = fields.Char(string="Email cá nhân", required=True)
    gioi_tinh = fields.Selection([
        ('nam', 'Nam'),
        ('nu', 'Nữ'),
        ('khac', 'Khác')
    ], default="nam", string="Giới tính")
    sdt = fields.Char(string="Điện thoại", required=True)
    birthday = fields.Datetime(string="Ngày sinh")
    cmnd_cccd = fields.Char(string="CMND/CCCD")
    dantoc = fields.Char(string="Dân tộc")
    tongiao = fields.Char(string="Tôn Giáo")
    # ------------------------------------------------
    province = fields.Selection(
        string='Tỉnh/thành', selection='_get_selection_options', default="")

    @api.model
    def _get_selection_options(self):
        file_path = "/opt/odoo/achievement_manage_addons/manage_user_depart/data/province.json"
        with open(file_path, 'r') as file:
            data = json.load(file)
            options = [(item['code'], item['name']) for item in data]
        return options
    # ------------------------------------------------
    district = fields.Char(
        string='Quận/huyện', selection='_get_district'
    )
    ward = fields.Char(
        string='Phường/ấp'
    )
    thuongtru = fields.Char(string="Địa chỉ thường trú")

    @api.depends('province')
    def _get_district(self):
        if self.province != "":
            file_path = "/opt/odoo/achievement_manage_addons/manage_user_depart/data/district.json"
            with open(file_path, 'r') as file:
                data = json.load(file)
                options = []
                for item in data:
                    if item['province_code'] == self.province:
                        options.append((item['code'], item['name']))
            return options
        else:
            return []

    # -----------------------------------------------
    # @api.model
    # def _get_ward(self):
    #     return

    thuongtru = fields.Char(string="Địa chỉ thường trú")
    donvi = fields.Many2one('manage_user_depart.department',
                            string="Đơn vị", required=True)
    nghenghiep = fields.Char(string="Nghề nghiệp")

    @api.model
    def create(self, vals):
        print('check')
        vals['lang'] = 'vi_VN'
        return super(User, self).create(vals)

    def save_success(self):
        return

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

    # --- Test
    quequan = fields.Selection(
        string='Quê quán', selection='_get_selection_options')

    @api.model
    def _get_selection_options(self):
        module_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(module_path, 'province.json')
        with open(file_path, 'r') as file:
            data = json.load(file)
            options = [(item['code'], item['name']) for item in data]
        return options

    thuongtru = fields.Char(string="Thường trú")
    donvi = fields.Many2one('manage_user_depart.department',
                            string="Đơn vị", required=True)
    nghenghiep = fields.Char(string="Nghề nghiệp")

    @api.model
    def create(self, vals):
        print('check')
        vals['lang'] = 'vi_VN'
        return super(User, self).create(vals)

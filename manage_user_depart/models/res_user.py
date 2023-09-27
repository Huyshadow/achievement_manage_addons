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


    # ------------------------------------------------province
    # province = fields.Selection(
    #     string='Tỉnh/thành', selection='_get_province', default="")

    # @api.model
    # def _get_province(self):
    #     province_model = self.env['user.province.info']
    #     province_records = province_model.search([])
    #     options = [(item['code'], item['name']) for item in province_records]
    #     return options
    # ------------------------------------------------district
    province = fields.Many2one('user.province.info',  string ='Tinh/Thanh')
    district = fields.Many2one('user.district.info', string = 'Quan/Huyen')
    ward = fields.Many2one('user.ward.info', string='Phuong')

    thuongtru = fields.Char(string="Địa chỉ thường trú")

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


 
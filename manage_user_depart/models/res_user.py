from odoo import models, fields, api


class User(models.Model):
    _inherit = 'res.users'

    mssv_mscb = fields.Char(string="MSSV/MSCB", required=True)
    canhan_email = fields.Char(string="Email cá nhân", required=True)
    gioi_tinh = fields.Selection([
        ('nam', 'Nam'),
        ('nu', 'Nữ'),
        ('khac', 'Khác')
    ], default="nam"  ,string = "Giới tính" , nonull= "1")
    sdt =  fields.Char(string = "Điện thoại",required=True)
    birthday = fields.Datetime(string = "Ngày sinh")
    cmnd_cccd = fields.Char(string = "CMND/CCCD")
    dantoc = fields.Char(string = "Dân tộc")
    tongiao = fields.Char(string = "Tôn Giáo")
    quequan = fields.Char(string = "Quê quán")
    thuongtru = fields.Char(string = "Thường trú")
    donvi = fields.Many2one('manage_user_depart.department',string = "Đơn vị",required=True)
    nghenghiep = fields.Char(string = "Nghề nghiệp")

    @api.model
    def create(self, vals):
        # Set the default language for the user
        vals['lang'] = 'vi_VN'
        return super(User, self).create(vals)

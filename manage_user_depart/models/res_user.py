from odoo import models, fields, api


class User(models.Model):
    _inherit = 'res.users'
  
    mssv_mscb = fields.Char(string = "MSSV/MSCB",required=True)
    # role = fields.Selection([
    #     ('participant', 'Participant'),
    #     ('other_type', 'Other_type')
    # ], default='participant', required=True , string = "Vai rò")
    canhan_email = fields.Char(string = "Email cá nhân",required=True)
    gioi_tinh = fields.Selection([
        ('nam', 'Nam'),
        ('nu', 'Nữ'),
        ('khac', 'Khác')
    ], default="nam"  ,string = "Giới tính")
    sdt =  fields.Char(string = "Điện thoại",required=True)
    birthday = fields.Datetime(string = "Ngày sinh")
    cmnd_cccd = fields.Char(string = "CMND/CCCD")
    dantoc = fields.Char(string = "Dân tộc")
    tongiao = fields.Char(string = "Tôn Giáo")
    quequan = fields.Char(string = "Quê quán")
    thuongtru = fields.Char(string = "Thường trú")
    donvi = fields.Many2one('manage_user_depart.department',string = "Đơn vị",required=True)
    nghenghiep = fields.Char(string = "Nghề nghiệp")
    # role = 
    # isRegisteredWithGoogle = fields.Boolean(required=True, default=False)
    # isUpdatedInformation = fields.Boolean(required=True, default=False)
    # hasContactInfo = fields.Boolean(required=True, default=False)
    # currentHashedRefreshToken = fields.Char()
    # updateAt = fields.Datetime()
    # deleteAt = fields.Datetime()
    # departmentId = fields.Many2one(
    #     'database_manage.department', string="Department")
    # achievementId = fields.Many2one(
    #     'database_manage.achievement', string='Achievement')  # Many2one with department

    # sql_constraints = [
    #     ('user_unique_email', 'UNIQUE (email)', 'Email must be unique')
    # ]

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AchievementUser(models.Model):
    _name = 'achievement.user.list'
    _description = 'Achievement User Submit List'

    user_id = fields.Many2one(
        'res.users', 'Created By', default=lambda self: self.env.user)
    achievement_id = fields.Many2one(
        'create_achievement.achievement', string="ID danh hiệu")
    donvi_id = fields.Many2one('manage_user_depart.department', string="ID đơn vị")
    appraise_status = fields.Selection('Tình trạng danh hiệu', related='achievement_id.appraise_status')
    submit_list = fields.One2many(
        'achievement.submit', 'parent_id', string='Danh sách hồ sơ nộp')

    user_name = fields.Char(string="Tên người nộp", related='user_id.name')
    mssv_mscb = fields.Char(string="Mã số sinh viên/ cán bộ", related='user_id.mssv_mscb',store = True)
    achievement_name = fields.Char(
        string="Tên danh hiệu", related='achievement_id.name')
    donvi_code = fields.Char(string="Mã đơn vị", related='donvi_id.code')
    donvi_name = fields.Char(string="Tên đơn vị", related='donvi_id.name', store = True)    
    submit_at = fields.Datetime()
    user_approve = fields.Boolean(string="Duyệt thành viên", default=False)
    
    def import_donvi_id(self):
        submit_list = self.env['achievement.user.list'].search([])
        for submit in submit_list:
            if not submit.donvi_id:
                id = submit.user_id.donvi.id
                submit.write({
                    'donvi_id': id  
                })
    
    @api.model
    def import_parent_id_for_achievement_submit(self):
        submit_list = self.env['achievement.submit'].search([])
        for submit in submit_list:
            if not submit.parent_id:
                parent = self.env['achievement.user.list'].search([
                    ('user_id', '=', submit.user_id.id),
                    ('achievement_id', '=', submit.criteria.parent_id.parent_id.parent_id.id)
                ])
                submit.write({
                    'parent_id': parent.id
                })

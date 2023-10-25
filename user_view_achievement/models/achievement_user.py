from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AchievementUser(models.Model):
    _name = 'achievement.user.list'
    _description = 'Achievement User Submit List'

    user_id = fields.Many2one(
        'res.users', 'Created By', default=lambda self: self.env.user)
    achievement_id = fields.Many2one(
        'create_achievement.achievement', string="ID danh hiệu")
    submit_list = fields.One2many(
        'achievement.submit', 'parent_id', string='Danh sách hồ sơ nộp')

    user_name = fields.Char(string="Tên người nộp", related='user_id.name')
    achievement_name = fields.Char(
        string="Tên danh hiệu", related='achievement_id.name')
    donvi_code = fields.Char(string="Mã đơn vị", related='user_id.donvi.code')
    donvi_name = fields.Char(string="Tên đơn vị", related='user_id.donvi.name')
    submit_at = fields.Datetime()

    # criteria_submited_list = fields.Char(string="ID tiêu chuẩn đã nộp", compute ='_compute_criteria_submited_list', store = True)
    # type_submited_list = fields.Char(string="ID loại tiêu chí đã nộp đủ", compute ='_compute_type_submited_list', store = True)
    # group_submited_list = fields.Char(string="ID tập tiêu chí đã nộp đủ", compute ='_compute_group_submited_list', store = True)

    full_submit = fields.Boolean(
        string="Đã nộp đủ tất cả tiêu chí", default=False)
    user_approve = fields.Boolean(string="Duyệt thành viên", default=False)
    expertise = fields.Boolean(
        string="Thẩm định", default=False, compute='_compute_expertise', store=True)
    approve = fields.Boolean(string="Thông qua", default=False)
    sum_expertise = fields.Selection([
        ('passed', 'Đã đạt(A)'),
        ('need_evidence', 'Thiếu minh chứng(B)'),
        ('not_passed', 'Không đạt(C)'),
        ('not_expertise', 'Chưa thẩm định')
    ], string="Kết quả thẩm định", default='not_expertise')

    @api.model
    def import_parent_id_for_achievement_submit(self):
        submit_list = self.env['achievement.submit'].search([])
        for submit in submit_list:
            if not submit.parent_id:
                parent = self.env['achievement.user.list'].search([
                    ('user_id', '=', submit.user_id.id),
                    ('achievement_id', '=',
                     submit.criteria.parent_id.parent_id.parent_id.id)
                ])
                submit.write({
                    'parent_id': parent.id
                })

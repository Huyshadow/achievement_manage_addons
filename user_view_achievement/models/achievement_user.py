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

<<<<<<< HEAD
    user_name = fields.Char(string="Tên người nộp", related='user_id.name')
    achievement_name = fields.Char(
        string="Tên danh hiệu", related='achievement_id.name')
    donvi_code = fields.Char(string="Mã đơn vị", related='user_id.donvi.code')
    donvi_name = fields.Char(string="Tên đơn vị", related='user_id.donvi.name')
=======
    user_name = fields.Char(string="Tên người nộp", related = 'user_id.name')
    achievement_name = fields.Char(string="Tên danh hiệu", related = 'achievement_id.name')
    donvi_code = fields.Char(string="Mã đơn vị", related = 'user_id.donvi.code')
    donvi_name=  fields.Char(string="Tên đơn vị", related = 'user_id.donvi.name')
>>>>>>> b98347a (Rebase 2)
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

    # @api.depends()

    # @api.depends('submit_at')
    # def _compute_criteria_submited_list(self):
    #     for record in self:
    #         if record.criteria_submited_list:
    #             current_criteria_list = [int(id) for id in record.criteria_submited_list.split(',')]
    #             criteria_submit = self.env['achievement.submit'].search([
    #                 ('user_id', '=',record.user_id),
    #                 ('criteria.parent_id.parent_id.parent_id.id','=',record.achievement_id),
    #                 ('criteria_id', 'not in', current_criteria_list)
    #             ])
    #             if criteria_submit and criteria_submit.submit:
    #                 record.criteria_submited_list += ',' + str(criteria_submit_id)
    #         else:
    #             criteria_submit_id = self.env['achievement.submit'].search([
    #                 ('user_id', '=',record.user_id),
    #                 ('criteria.parent_id.parent_id.parent_id.id','=',record.achievement_id),
    #             ])
    #             record.criteria_submited_list = str(criteria_submit_id)

    # @api.depends('criteria_submited_list')
    # def _compute_type_submited_list(self):
    #     for record in self:
    #         if record.type_submited_list:
    #             current_type_list = [int(id) for id in record.type_submited_list.split(',')]
    #             temp_type_list = self.env['create_achievement.type_criterias'].search([
    #                 ('parent_id.parent_id.id','=',record.achievement_id),
    #                 ('id', 'not in', current_type_list)
    #             ])
    #             for type_criteria in temp_type_list:
    #                 submit_criteria_list = [int(id) for id in record.criteria_submited_list.split(',')]

    #                 temp_criteria_list = []
    #                 for criteria in type_criteria.criteria_ids:
    #                     temp_criteria_list.append(criteria.id)

    #                 if type_criteria.constraint == 'all':

    #                 elif type_criteria.constraint == 'some':

    #                 else:
    #                     continue

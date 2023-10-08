from odoo import models, fields, api


class TypeCriterias(models.Model):
    _name = 'create_achievement.type_criterias'
    _description = 'Group_Criteria for Tuyen duong Website'

    parent_id = fields.Many2one(
        "create_achievement.group_criterias", string="Dạng tiêu chí")
    criteria_ids = fields.One2many(
        'create_achievement.criteria', 'parent_id', string="Danh sách tiêu chí")
    name = fields.Char(string="Tên Loại tiêu chí", required=True)
    constraint = fields.Selection(
        [("all", "Tất cả"), ("some", 'Tự chọn')], string="Số tiêu chí thõa mãn", required=True)
    nums_of_option = fields.Integer(string="Số tiêu chí phải thỏa", default=0)

    nums_current_option = fields.Integer(string="Số tiêu chí đang có", compute = "_compute_nums_current_option", store=True)

    @api.depends('criteria_ids')
    def _compute_nums_current_option(self):
        for record in self:
            nums_current_option = len(record.criteria_ids)

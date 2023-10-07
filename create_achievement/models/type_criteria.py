from odoo import models, fields, api


class TypeCriterias(models.Model):
    _name = 'create_achievement.type_criterias'
    _description = 'Group_Criteria for Tuyen duong Website'

    parent_id = fields.Many2one(
        "create_achievement.group_criterias", string="Dạng tiêu chí")
    criteria_ids = fields.One2many(
        'create_achievement.criteria', 'parent_id', string="Danh sách tiêu chí")
    name = fields.Char(string="Tên Dạng tiêu chí", required=True)
    constraint = fields.Boolean(string="Bắt buộc", default=True)
    nums_of_option = fields.Integer(string="Số tiêu chí phải thỏa", default=0)

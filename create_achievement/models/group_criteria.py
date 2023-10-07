from odoo import models, fields, api


class GroupCriterias(models.Model):
    _name = 'create_achievement.group_criterias'
    _description = 'Group_Criteria for Tuyen duong Website'

    parent_id = fields.Many2one(
        "create_achievement.achievement", string="Danh hiệu")
    type_criteria_ids = fields.One2many(
        'create_achievement.type_criterias', 'parent_id', string="Loại tiêu chí")
    name = fields.Char(string="Tên tập tiêu chí", required=True)
    description = fields.Text(
        string="Mô tả", default="Không"
    )

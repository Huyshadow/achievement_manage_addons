from odoo import models, fields, api


class GroupCriterias(models.Model):
    _name = 'create_achievement.group_criterias'
    _description = 'Group_Criteria for Tuyen duong Website'

    parent_id = fields.Many2one(
        "create_achievement.achievement", string="Danh hiệu")

    name = fields.Char(string="Tên tập tiêu chí")

    constrait_criterias = fields.One2many(
        "create_achievement.criteria", "parent_id_constraint", string="Danh sách tiêu chí bắt buộc")

    option_criterias = fields.One2many(
        "create_achievement.criteria", "parent_id_option", string="Danh sách tiêu chí tự chọn")
    # just have 1 of this criteria

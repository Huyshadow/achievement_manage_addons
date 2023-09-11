""" from odoo import models, fields, api


class GroupCriteria(models.Model):
    _name = 'create_achievement.group_criteria'
    _description = ' Group_Criteria for Tuyen duong Website'

    parent_id = fields.Many2one(
        'create_achievement.achievement', string="Group Criterias for Achievement", required=True)
    child_id = fields.One2many(
        'create_achievement.criteria', 'id', string="Achivement's Criteria")
    self_1_id = fields.Many2one(
        'create_achievement.group_criteria', string="Group Criterias of Group Criteria")
    self_2_id = fields.One2many(
        'create_achievement.group_criteria', 'id', string="Group Criterias of Group Criteria"
    )

    id = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code(
        'create.achievement.group.crieria'), required=True, copy=True, readonly=True)
    type = fields.Selection([
        ('tiêu chí', 'Tiêu chí'),
        ('tập tiêu chí', 'Tập tiêu chí')
    ], default='tiêu chí', required=True)
    name = fields.Char(required=True)
    note = fields.Char(required=True, default='')
    deleteAt = fields.Datetime()
 """

from odoo import models, fields, api


class Achievement(models.Model):
    _name = 'create_achievement.achievement'
    _description = 'Achievement Model of Create-Achievement Module'

    parent_id = fields.Many2one(
        'create_achievement.achievement', string="Root Model")

    id = fields.Integer(string="ID", default=lambda self: self.env['ir.sequence'].next_by_code(
        'create.achievement.achievement'))
    criteria_ids = fields.One2many(
        'create_achievement.criteria', 'id', string="Achivement's Criteria")
    name = fields.Char(default="Achievement", required=True)
    soft_criteria = fields.Integer(string="Soft Criteria")
    description = fields.Text(string="Description")
    end_at = fields.Datetime()
    start_at = fields.Datetime()
    end_submit_at = fields.Datetime()
    lock = fields.Selection([
        ('unavailable', 'Unavailable'),
        ('available', 'Available')
    ], default='unavailable', required=True)
    type = fields.Selection([
        ('achievement', 'Achievement'),
        ('other_type', 'Other_type')
    ], default='achievement', required=True)
    manage_unit = fields.Text(default='{}')
    delete_at = fields.Datetime()

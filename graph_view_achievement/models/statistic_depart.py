from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Statistic_Depart(models.Model):
    _name = "achievement.department.statistic"

    achievement_id = fields.Many2one(
        'create_achievement.achievement', string="ID danh hiệu")
    num_of_submit = fields.Char()
    num_of_accept = fields.Char()
    depart_name = fields.Char()
    depart_id = fields.Char()

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Statistic_Depart(models.Model):
    _name = "achievement.department.statistic"

    achievement_id = fields.Many2one(
        'create_achievement.achievement', string="ID danh hiệu")
    num_of_submit = fields.Char(default="0")
    submit_nums = fields.Integer(compute="_compute_submit", store=True)
    num_of_accept = fields.Char(default="0")
    accept_nums = fields.Integer(compute="_compute_accept", store=True)
    depart_name = fields.Char(string="Danh sách đơn vị")
    depart_id = fields.Char()

    @api.depends('num_of_submit')
    def _compute_submit(self):
        for record in self:
            record.submit_nums = int(record.num_of_submit)

    @api.depends('num_of_accept')
    def _compute_accept(self):
        for record in self:
            record.accept_nums = int(record.num_of_accept)

    # ----------------Appraise Statistic------------------
    num_of_A = fields.Char(default="0")

    num_of_B = fields.Char(default="0")

    num_of_C = fields.Char(default="0")

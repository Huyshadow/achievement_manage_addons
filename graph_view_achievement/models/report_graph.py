from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Statistic_Report(models.Model):
    _name = "achievement.graph.report"

    achievement_id = fields.Many2one(
        'create_achievement.achievement', string="ID danh hiệu")
    depart_name = fields.Char(string="Danh sách đơn vị")
    type = fields.Selection(
        [("a_submit", "Đã nộp"), ("b_accepted", "Đã duyệt")])
    num = fields.Char(default="0")
    display_nums = fields.Integer(compute="_compute_submit", store=True)

    @api.depends('num')
    def _compute_submit(self):
        for record in self:
            record.display_nums = int(record.num)

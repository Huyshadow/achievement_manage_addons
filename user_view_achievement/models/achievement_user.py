from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AchievementUser(models.Model):
    _name = 'achievement.user.list'
    _description = 'Achievement User Submit List'

    user_name = fields.Char(string="Tên người nộp")
    achievement_id = fields.Integer(string="ID danh hiệu")
    achievement_name = fields.Char(string="Tên danh hiệu", compute ="_compute_achievement_name",store=True)
    donvi_name=  fields.Char(string="Tên đơn vị")
    submit_at = fields.Datetime()

    @api.depends('achievement_id')
    def _compute_achievement_name(self):
        for record in self:
            record.achievement_name = record.env['manage_user_depart.department'].browse(record.achievement_id).name
    
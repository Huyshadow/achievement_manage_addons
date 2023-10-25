from odoo import models, fields, api


class Appraise(models.Model):
    _name = 'create_achievement.appraise'

    user_id = fields.Many2one('res.users')
    achievement_id = fields.Many2one('create_achievement.achievement')
    donvis = fields.Many2many('manage_user_depart.department')
    donvis_names = fields.Char(
        string='Đơn vị phụ trách', compute='_compute_donvis_names', store=True)

    @api.depends('donvis')
    def _compute_donvis_names(self):
        for record in self:
            department_names = ', '.join(record.donvis.mapped('code'))
            record.donvis_names = department_names

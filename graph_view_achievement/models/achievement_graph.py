from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Achievement(models.Model):
    _inherit = 'create_achievement.achievement'

    # user_list_ids = fields.One2many(
    #     'achievement.user.list', 'achievement_id', string="Danh sách người nộp")
    # num_of_user = fields.Char(string="Số lượng đã duyệt/đã nộp", compute = "_compute_num_of_user")
    num_of_submit = fields.Integer(default=0, compute="_compute_num_of_submit")
    num_of_accept = fields.Integer(default=0, compute="_compute_num_of_accept")
    donvi_depart = fields.Many2many('manage_user_depart.department')

    @api.depends('donvi_depart')
    def _compute_num_of_submit(self):
        for record in self:
            total_list = self.env['achievement.user.list'].search([
                ('achievement_id.id', '=', record.id),
                ('donvi_name', '=', record.donvi_depart),
            ])
            total = len(total_list)
            record.num_of_submit = total

    @api.depends('user_list_ids.user_approve')
    def _compute_num_of_accept(self):
        for record in self:
            current_list = self.env['achievement.user.list'].search([
                ('achievement_id.id', '=', record.id),
                ('donvi_name', '=', record.donvi_depart)
                ('user_approve', '=', True),
            ])
            current = len(current_list)
            record.num_of_accept = current

    def action_view_user_list(self):
        return {
            'name': self.name,
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'view_id': self.env.ref('view_submit.view_achievement_user_list').id,
            'res_model': 'achievement.user.list',
            # 'res_id': self.id,
            'target': 'current',
            'flags': {'hasSelectors': False},
            'domain': [('achievement_id', '=', self.id), ('donvi_name', '=', self.env.user.donvi.name)],
        }

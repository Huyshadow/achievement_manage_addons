from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Achievement(models.Model):
    _inherit = 'create_achievement.achievement'

    user_list_ids = fields.One2many(
        'achievement.user.list', 'achievement_id', string="Danh sách người nộp")
    num_of_user = fields.Char(string="Số lượng đã duyệt/đã nộp", compute = "_compute_num_of_user")

    @api.depends('user_list_ids.user_approve')
    def _compute_num_of_user(self):
        for record in self:
            total_list = self.env['achievement.user.list'].search([
                ('achievement_id.id' ,'=', record.id),
                ('donvi_name','=',self.env.user.donvi.name),
            ])
            total = len(total_list)
            current_list = self.env['achievement.user.list'].search([
                ('achievement_id.id' ,'=', record.id),
                ('user_approve','=',True),
                ('donvi_name','=',self.env.user.donvi.name),
            ])
            current = len(current_list)
            result = str(current) + "/" + str(total)
            record.num_of_user = result

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
        'domain': [('achievement_id', '=', self.id),('donvi_name','=',self.env.user.donvi.name)],
    }

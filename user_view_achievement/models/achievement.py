from odoo import models, fields, api

class Achievement(models.Model):
    _inherit = 'create_achievement.achievement'

    
    def action_view_achievement_detail(self):
        return {
            'name': 'Thông tin danh hieu',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': self.env.ref('user_view_achievement.view_achievement_detail').id,
            'views': [(False, 'form')],
            'res_model': 'create_achievement.achievement',
            'res_id': self.id,
            'target': 'current',
        }
        # action = self.env['ir.actions.actions'].with_context(active_id=self.id)._for_xml_id('user_view_achievement.action_view_achievement_detail')
        # return action

    # def get_name(self):
    #     return {
    #         'name': self.name,
    #         'status': self.status,
    #     }



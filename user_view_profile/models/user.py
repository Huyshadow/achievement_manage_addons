from odoo import models, fields, api


class User(models.Model):
    _inherit = 'res.users'

    @api.model
    def open_user_profile(self):
        return {
            'name': 'Thông tin cá nhân',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'views': [(False, 'form')],
            'res_model': 'res.users',
            'res_id': self.env.user.id,
            'target': 'current',
        }


from odoo import models, fields, api


class Department(models.Model):
    _name = 'manage_user_depart.department'
    _description = 'Department of Tuyen duong Website'

    code = fields.Char(default=lambda self: self.env['ir.sequence'].next_by_code(
        'manage.user.depart.department'))
    name = fields.Char(string="Name")
    user_count = fields.Integer(
        string="Số lượng người dùng", compute="_compute_user_count")

    def _compute_user_count(self):
        for department in self:
            department.user_count = self.env['res.users'].search_count(
                [('donvi', '=', department.id)])

    def nothing(self):
        return {
            'name': 'Danh sách đơn vị',
            'res_model': 'manage_user_depart.department',
            'view_mode': 'tree,form',
            'view_type': 'tree',
            # 'view_id': self.env.ref('manage_user_depart.list_depart').id,
            'type': 'ir.actions.act_window',
            'target': 'current',
            'context': {
                'create': True,
            }
        }
        # url = "/web#active_id=1&model=manage_user_depart.department&view_type=list&id=1&menu_id=70"
        # return request.redirect(url)

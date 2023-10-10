
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

    def save_and_redirect(self):
        text = """Tạo đơn vị thành công"""
        query = 'delete from display_dialog_box'
        self.env.cr.execute(query)
        value = self.env['display.dialog.box'].sudo().create({'text': text})
        return {
            'type': 'ir.actions.act_window',
            'name': 'Thông báo',
            'res_model': 'display.dialog.box',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            'res_id': value.id
        }

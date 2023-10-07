from odoo import models, fields, api


class display_dialog_box(models.Model):
    _name = "display.dialog.box"

    _description = "Message popup"

    text = fields.Text()

    def cancel(self):
        return {
            'name': 'Danh sách đơn vị',
            'res_model': 'display.dialog.box',
            'view_mode': 'form',
            'view_type': 'form',
            'type': 'ir.actions.act_window_close',
            'target': 'current',
        }

from odoo import models, fields, api


class display_dialog_box(models.Model):
    _name = "display.dialog.box"

    _description = "Message popup"

    text = fields.Text()

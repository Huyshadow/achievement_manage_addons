from odoo import models, fields, api


class AchievementManager(models.Model):
    _name = "access_right_user.achievement_manager"
    _description = "Achievement Manager Role for user"

    name = fields.Char('Name')
    module_ids = fields.Many2many('ir.module.module', string='Modules')

    @api.model
    def set_access_rights(self):
        # Get the modules associated with the role
        modules = self.module_ids

        # Set access rights for each module
        for module in modules:
            model_name = module.model
            self.env[model_name].sudo().set_access_rights(
                perm_read=True, perm_write=True, perm_create=True, perm_unlink=True)

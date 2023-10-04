from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AchievementSubmit(models.Model):
    _inherit = 'achievement.submit'
    

    def action_expertise_submit(self):
        self.env['achievement.submit'].write({
            
        })
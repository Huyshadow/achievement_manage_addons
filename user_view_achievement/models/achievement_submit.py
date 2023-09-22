from odoo import models, fields, api


class AchievementSubmit(models.Model):
    _name = 'achievement.submit'
    _description = 'Achievement Submit'

    user_id = fields.Many2one('res.users', 'Created By', default=lambda self: self.env.user)
    criteria_id = fields.Many2one('create_achievement.criteria', 'Tieu chi')
    criteria_name = fields.Char('Name', related='criteria_id.name')
    criteria_content = fields.Char('Mo ta', related ='criteria_id.content')
    criteria_method = fields.Selection('Phuong thuc', related='criteria_id.method')
    grade = fields.Integer('Grade')
    is_passed = fields.Boolean('Is Passed?')
    comment = fields.Text('Comment')
    evidence = fields.Binary('Evidence')

from odoo import models, fields, api


class AchievementSubmit(models.Model):
    _name = 'achievement.submit'
    _description = 'Achievement Submit'

    user_id = fields.Many2one('res.users', 'Created By', default=lambda self: self.env.user)
    criteria_id = fields.Many2one('create_achievement.criteria', 'Tieu chi')
    criteria_name = fields.Char('Name', related='criteria_id.name')
    criteria_content = fields.Char('Mo ta', related='criteria_id.content')
    criteria_method = fields.Selection('Phuong thuc',related='criteria_id.method', related_sudo=False)
    criteria_method_display = fields.Selection('Phuong thuc',related='criteria_id.method')
    
    grade = fields.Integer('Grade')
    is_passed = fields.Boolean('Đã đạt')
    comment = fields.Text('Comment')
    evidence = fields.Binary('Evidence')
    submit = fields.Boolean('Đã nộp', compute="_check_submit", store=True)

    @api.depends('grade', 'is_passed', 'comment')
    def _check_submit(self):
        for record in self:
            if record.criteria_method == "thangdiem":
                if record.grade:
                    record.submit = True
            elif record.criteria_method == "nhiphan":
                if record.is_passed == True:
                    record.submit = True
            elif record.criteria_method == "nhanxet":
                if record.comment:
                    record.submit = True
            else:
                record.submit = False
            # if criteria_method = "danhsach":
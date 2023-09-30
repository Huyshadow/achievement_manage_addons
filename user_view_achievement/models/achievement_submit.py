from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AchievementSubmit(models.Model):
    _name = 'achievement.submit'
    _description = 'Achievement Submit'

    user_id = fields.Many2one(
        'res.users', 'Created By', default=lambda self: self.env.user)
    criteria_id = fields.Many2one('create_achievement.criteria', 'Tieu chi')
    criteria_name = fields.Char('Tên tiêu chí', related='criteria_id.name')
    criteria_content = fields.Char('Mô tả', related='criteria_id.content')
    criteria_method = fields.Selection(
        'Phương thức', related='criteria_id.method', related_sudo=False)
    criteria_method_display = fields.Selection(
        'Phương thức hiển thị', related='criteria_id.method')

    grade = fields.Integer('Điểm')
    is_passed = fields.Boolean('Đã đạt')
    comment = fields.Text(string='Tự nhận xét')
    evidence = fields.Binary(string='Minh Chứng(file .pdf)')
    pdf_name = fields.Char(string='Tên file pdf')

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

    @api.constrains('evidence')
    def _check_file(self):
        if str(self.pdf_name.split(".")[1]) != 'pdf':
            raise ValidationError("Chỉ nhận file PDF")

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import os

class AchievementSubmit(models.Model):
    _name = 'achievement.submit'
    _description = 'Achievement Submit'

    parent_id = fields.Many2one('achievement.user.list', 'Thuộc user')
    parent_name = fields.Char('Tên user', store= True, related='parent_id.user_name')
    user_id = fields.Many2one(
        'res.users', 'Created By', default=lambda self: self.env.user)
    criteria = fields.Many2one('create_achievement.criteria', 'Tieu chi')
    criteria_id = fields.Integer('ID tiêu chí', related='criteria.id')
    criteria_name = fields.Char('Tên tiêu chí', related='criteria.name')
    criteria_content = fields.Char('Nội dung', related='criteria.content')
    criteria_method = fields.Selection(
        'Phương thức', related='criteria.method', related_sudo=False)
    required_evidence = fields.Boolean(
        'Cần minh chứng', related='criteria.evidence', store=True)
    group_criteria_name = fields.Char(
        'Tên tập tiêu chí', related='criteria.parent_id.parent_id.name', store=True)
    type_criteria_name = fields.Char(
        'Tên loại tiêu chí', related='criteria.parent_id.name', store=True)
    expertise = fields.Selection([
        ('passed', 'Đã đạt (A)'),
        ('need_evidence', 'Cần bổ sung (B)'),
        ('not_passed', 'Không đạt (C)'),
    ], string="Kết quả thẩm định", default='')
    depart_manage_comment = fields.Text('Nhận xét')

    grade = fields.Float('Điểm')
    is_passed = fields.Boolean('Đã đạt')
    comment = fields.Text(string='Tự nhận xét')
    evidence = fields.Binary(string='Minh Chứng(file .pdf)')
    pdf_name = fields.Char(string='Tên file pdf')
    submit = fields.Boolean('Đã nộp', compute="_check_submit", store=True)
    submit_content = fields.Char(string='Nội dung nộp')

    have_evidence = fields.Boolean("Minh chứng", default = False, compute = "_compute_evidence")

    @api.depends('evidence')
    def _compute_evidence(self):
        for record in self:
            if record.evidence:
                record.have_evidence = True
            else:
                record.have_evidence = False

    @api.depends('grade', 'is_passed', 'comment')
    def _check_submit(self):
        for record in self:
            if record.criteria_method == "thangdiem":
                if record.grade:
                    record.submit = True
                    record.submit_content = str(record.grade)
            elif record.criteria_method == "nhiphan":
                if record.is_passed == True:
                    record.submit = True
                    record.submit_content = "Đã đạt"
            elif record.criteria_method == "nhanxet":
                if record.comment:
                    record.submit = True
                    record.submit_content = record.comment

    @api.constrains('evidence')
    def _check_file(self):
        if os.path.splitext(str(self.pdf_name))[1] != '.pdf':
            raise ValidationError("Chỉ nhận file PDF")

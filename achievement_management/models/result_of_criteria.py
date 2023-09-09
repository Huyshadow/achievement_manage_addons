from odoo import models, fields, api


class ResultOfCriteria(models.Model):
    _name = 'database_manage.result_of_criteria'
    _description = 'Result of criteria from Tuyen duong Website'

    id = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code(
        'database.manage.result_of_crieria'), required=True, copy=True, readonly=True)
    result = fields.Integer()
    description = fields.Text()
    typeResult = fields.Selection([
        ('ACHIEVEMENT', 'Achivement'),
        ('other_type', 'Other_type')
    ], default='ACHIEVEMENT', required=True)
    updateAt = fields.Datetime(default=fields.Datetime.now, required=True)
    userId = fields.Many2one('database_manage.user', string="User")
    resultAchievementId = fields.Many2one(
        'database_manage.result', string="Result")  # manytoone result
    submissionId = fields.Many2one(
        'database_manage.submission', string="Submission")

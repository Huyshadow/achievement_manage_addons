from odoo import models, fields, api


class Submission(models.Model):
    _name = 'database_manage.submission'
    _description = ' User from Tuyen duong Website'
    _inherit= []

    id = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code('database.manage.submission'), required=True, copy=True, readonly=True)
    file = fields.Char(required=True)
    point = fields.Float(required=True, default=0)
    binary = fields.Boolean()
    description = fields.Char(required=True)
    name = fields.Char()
    studentComment= fields.Char(required=True, default='')
    studentSelect =fields.Char(required=True, default='')
    isVerified = fields.Boolean(required=True, default=False)
    updateAt = fields.Datetime()
    endAt = fields.Datetime()
    startAt = fields.Datetime()
    userId = fields.Many2one('database_manage.user', string="User")#manytoone user
    achievementId =fields.Many2one('database_manage.achievement', string="Achievement")
    criteriaId = fields.Many2one('database_manage.criteria', string="Criteria")

    sql_constraints = [
        ('submission_pk', 'PRIMARY KEY (id)', '''ID must be Primary Key'''),
    ]
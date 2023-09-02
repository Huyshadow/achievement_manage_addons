from odoo import models, fields, api


class Result(models.Model):
    _name = 'database_manage.result'
    _description = 'Result of Tuyen duong Website'

    resultId = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code('database.manage.result'), required=True, copy=True, readonly=True)
    result = fields.Integer()
    final = fields.Boolean(required=True, default=False)
    
    updateAt = fields.Datetime()
    achievementId = fields.Many2one('database_manage.achievement', string="Achievement")
    examerId = fields.Many2one('database_manage.user', string="Examer")
    auditorId = fields.Many2one('database_manage.user', string="Auditor")

    _sql_constraints = [
        ('result_pk', 'PRIMARY KEY (resultId)', 'Result ID must be Primary Key')
    ]

    # @api.model
    # def create(self, vals):
    #     vals['departmentId'] = self.env['ir.sequence'].next_by_code('database.manage.department')
    #     return super(Department, self).create(vals)
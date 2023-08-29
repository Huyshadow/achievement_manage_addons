from odoo import models, fields, api


class Result(models.Model):
    _name = 'database_manage.result'
    _description = 'Result of Tuyen duong Website'
    _inherit= ['database_manage.achievement']

    resultId = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code('database.manage.result'), required=True, copy=True, readonly=True)
    result = fields.Integer(tracking=True)
    final = fields.Boolean(required=True, default=False)
    createAt = fields.Datetime(default=fields.Datetime.now, required=True)
    updateAt = fields.Datetime(default=fields.Datetime.now, required=True)
    achievementRelated = fields.Many2one('database_manage.achievement', string="Achievement")
    achievementId = fields.Integer(related='achievementRelated.id', store=True)
    examerId = fields.Integer(tracking=True)
    auditorId = fields.Integer(tracking=True)

    _sql_constraints = [
        ('result_pk', 'PRIMARY KEY (resultId)', 'Result ID must be Primary Key')
    ]

    # @api.model
    # def create(self, vals):
    #     vals['departmentId'] = self.env['ir.sequence'].next_by_code('database.manage.department')
    #     return super(Department, self).create(vals)
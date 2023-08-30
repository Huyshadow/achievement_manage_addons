from odoo import models, fields, api


class ResultOfCriteria(models.Model):
    _name = 'database_manage.result_of_criteria'
    _description = 'Result of criteria from Tuyen duong Website'
    _inherit= ['database_manage.achievement']

    id = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code('database.manage.result_of_crieria'), required=True, copy=True, readonly=True)
    result = fields.Integer(tracking=True)
    description = fields.Text()
    typeResult = fields.Selection([
        ('ACHIEVEMENT', 'Achivement'),
        ('other_type','Other_type')
    ], default='ACHIEVEMENT', required=True)
    createAt = fields.Datetime(default=fields.Datetime.now, required=True)
    updateAt = fields.Datetime(default=fields.Datetime.now, required=True)
    userId = fields.Integer(tracking=True) #manytoone user
    resultAchievementId = fields.Integer(tracking=True) #manytoone result
    submissionId = fields.Integer(tracking=True) #manytoone submission

    _sql_constraints = [
        ('result_of_criteria_pk', 'PRIMARY KEY (id)', 'ID must be Primary Key')
    ]

    # @api.model
    # def create(self, vals):
    #     vals['departmentId'] = self.env['ir.sequence'].next_by_code('database.manage.department')
    #     return super(Department, self).create(vals)
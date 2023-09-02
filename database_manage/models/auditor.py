from odoo import models, fields, api


class Auditor(models.Model):
    _name = 'database_manage.auditor'
    _description = 'Auditor from Tuyen duong Website'
    _inherit= []

    id = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code('database.manage.auditor'), required=True, copy=True, readonly=True)
    achivementId = fields.Integer()
    createAt = fields.Datetime(default=fields.Datetime.now, required=True)
    updateAt = fields.Datetime(default=fields.Datetime.now, required=True)
    deleteAt= fields.Datetime()
    departmentId = fields.Many2one('database_manage.department',string='Department')
    userId = fields.Many2one('database_manage.user',string='User') 
    achievementId = fields.Many2one('database_manage.achievement', string='Achievement')

    sql_constraints = [
        ('auditor_pk', 'PRIMARY KEY (id)', '''auditor's ID must be Primary Key'''),
        ('user_unique_email', 'UNIQUE (email)','''User's email must be unique''')
    ]
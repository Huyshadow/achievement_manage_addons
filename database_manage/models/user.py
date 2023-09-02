from odoo import models, fields, api

class User(models.Model):
    _name = 'database_manage.user'
    _description = 'User from Tuyen duong Website'

    id = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code('database.manage.user'), required=True, copy=True, readonly=True)
    email = fields.Char(default='', required=True)
    name = fields.Char()
    surName = fields.Char()
    mssv = fields.Char()
    role = fields.Selection([
        ('participant', 'Participant'),
        ('other_type', 'Other_type')
    ], default='participant', required = True)
    isRegisteredWithGoogle = fields.Boolean(required=True, default=False)
    isUpdatedInformation = fields.Boolean(required=True, default=False)
    hasContactInfo = fields.Boolean(required=True, default=False)
    currentHashedRefreshToken = fields.Char()
    createAt = fields.Datetime(default=fields.Datetime.now, required=True)
    updateAt = fields.Datetime()
    deleteAt= fields.Datetime()
    departmentId = fields.Many2one('database_manage.department', string="Department")
    achievementId = fields.Many2one('database_manage.achievement',string='Achievement') #Many2one with department

    sql_constraints = [
        ('user_pk', 'PRIMARY KEY (id)', 'ID must be Primary Key'),
        ('user_unique_email', 'UNIQUE (email)','Email must be unique')
    ]
from odoo import models, fields, api


class Auditor(models.Model):
    _name = 'database_manage.auditor'
    _description = 'Auditor from Tuyen duong Website'
    _inherit= []

    id = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code('database.manage.auditor'), required=True, copy=True, readonly=True)
    userID = fields.Integer() #manytoone voi user
    departmentId = fields.Integer() #manytoone voi department
    achivementId = fields.Integer()
    createAt = fields.Datetime(default=fields.Datetime.now, required=True)
    updateAt = fields.Datetime(default=fields.Datetime.now, required=True)
    deleteAt= fields.Datetime()
    departmentId = fields.Integer() # Manytoone with depatment
    auditorId = fields.Integer() #Many2one with department

    sql_constraints = [
        ('auditor_pk', 'PRIMARY KEY (id)', '''auditor's ID must be Primary Key'''),
        ('user_unique_email', 'UNIQUE (email)','''User's email must be unique''')
    ]
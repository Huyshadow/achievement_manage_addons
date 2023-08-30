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
    isVerified = fields.Boolean(requird=True, default=False)
    createAt = fields.Datetime(default=fields.Datetime.now, required=True)
    updateAt = fields.Datetime(default=fields.Datetime.now, required=True)
    endAt = fields.Datetime(default=fields.Datetime.now, required=True)
    startAt = fields.Datetime(default=fields.Datetime.now, required=True)
    userId = fields.Integer()#manytoone user
    achievementId =fields.Integer() #manytoone achievement
    criteriaId = fields.Integer() #mantoone criteria

    sql_constraints = [
        ('submission_pk', 'PRIMARY KEY (id)', '''ID must be Primary Key'''),
        #
    ]
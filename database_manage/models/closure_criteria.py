from odoo import models, fields, api


class Criteria(models.Model):
    _name = 'database_manage.closure_criteria'
    _description = ' Closure_criteria from Tuyen duong Website'

    id = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code('database.manage.closure_criteria'), required=True, copy=True, readonly=True)
    ancestorsId = fields.Integer()
    descendantsId =fields.Integer()
    
    sql_constraints = [
        ('criteria_pk', 'PRIMARY KEY (id)', '''Criteria's ID must be Primary Key'''),
    ]
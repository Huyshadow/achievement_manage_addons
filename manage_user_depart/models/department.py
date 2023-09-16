
from odoo import models, fields, api


class Department(models.Model):
    _name = 'manage_user_depart.department'
    _description = 'Department of Tuyen duong Website'

    # departmentId = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code(
    #     'database.manage.department'), required=True, copy=True, readonly=True)
    code = fields.Char()
    name = fields.Char(string="Name")
    # updateAt = fields.Datetime()
    # deleteAt = fields.Datetime()

    # _sql_constraints = [
    #     ('department_unique_name', 'UNIQUE (name)',
    #      'Department Name must be unique'),
    #     ('department_unique_code', 'UNIQUE (code)',
    #      'Department Code must be unique'),
    # ]


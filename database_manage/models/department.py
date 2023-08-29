
from odoo import models, fields, api


class Department(models.Model):
    _name = 'database_manage.department'
    _description = 'Department of Tuyen duong Website'

    departmentId = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code('database.manage.department'), required=True, copy=True, readonly=True)
    code = fields.Char(tracking=True)
    name = fields.Char(string="Name", tracking=True)
    createAt = fields.Datetime(default=fields.Datetime.now, required=True)
    updateAt = fields.Datetime(default=fields.Datetime.now, required=True)
    deleteAt = fields.Datetime()

    _sql_constraints = [
        ('department_pk', 'PRIMARY KEY (departmentId)', 'Department ID must be Primary Key'),
        ('department_unique_name', 'UNIQUE (name)', 'Department Name must be unique'),
        ('department_unique_code', 'UNIQUE (code)', 'Department Code must be unique'),
    ]

    @api.model
    def create(self, vals):
        vals['departmentId'] = self.env['ir.sequence'].next_by_code('database.manage.department')
        return super(Department, self).create(vals)
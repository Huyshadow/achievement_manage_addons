
from odoo import models, fields, api


class Department(models.Model):
    _name = 'manage_user_depart.department'
    _description = 'Department of Tuyen duong Website'

    # departmentId = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code(
    #     'database.manage.department'), required=True, copy=True, readonly=True)
    code = fields.Char()
    name = fields.Char(string="Name")
    user_count = fields.Integer(string="Số lượng người dùng", compute="_compute_user_count")

    # @api.depends('user_ids')
    def _compute_user_count(self):
        for department in self:
            department.user_count = self.env['res.users'].search_count([('donvi', '=', department.id)])
    # updateAt = fields.Datetime()
    # deleteAt = fields.Datetime()

    # _sql_constraints = [
    #     ('department_unique_name', 'UNIQUE (name)',
    #      'Department Name must be unique'),
    #     ('department_unique_code', 'UNIQUE (code)',
    #      'Department Code must be unique'),
    # ]


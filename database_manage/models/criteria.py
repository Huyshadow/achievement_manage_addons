from odoo import models, fields, api

class Criteria(models.Model):
    _name = 'database_manage.criteria'
    _description = ' Criteria from Tuyen duong Website'

    id = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code('database.manage.criteria'), required=True, copy=True, readonly=True)
    name = fields.Char(required=True)
    isCriteria = fields.Boolean(required=True, default=False) 
    method = fields.Char(required=True, default='binary')
    note = fields.Char(required=True, default='')
    valueListString = fields.Char(required=True, default='')
    content = fields.Char(required=True, default='')
    type = fields.Selection([
        ('hard','Hard'),
        ('other_type','Other_type')
    ], default = 'hard', required=True)
    evidence = fields.Boolean(required=True, default=False) 
    lowerSign = fields.Selection([
        ('<', '<'),
        ('<=', '<='),
        ('>', '>'),
        ('>=', '>=')
    ], default=('>'),required=True)
    upperSign = fields.Selection([
        ('<', '<'),
        ('<=', '<='),
        ('>', '>'),
        ('>=', '>=')
    ], default=('>'), required=True)
    point = fields.Float(default=0,required=True)
    lowerPoint = fields.Float(default=0, required=True)
    upperPoint = fields.Float(default=0, required=True) 
    updateAt = fields.Datetime()
    deleteAt= fields.Datetime()
    achievementId = fields.Many2one('database_manage.achievement', string='Achievement ID')

    sql_constraints = [
        ('criteria_pk', 'PRIMARY KEY (id)', '''Criteria's ID must be Primary Key'''),
    ]
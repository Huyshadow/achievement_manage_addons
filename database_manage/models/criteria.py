from odoo import models, fields, api

class Criteria(models.Model):
    _name = 'database_manage.criteria'
    _description = ' Criteria from Tuyen duong Website'

    id = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code('database.manage.criteria'), required=True, copy=True, readonly=True)
    name = fields.Char(required=True)
    isCriteria = fields.Boolean(required=True, default=False) 
    method = fields.Char(required=True, default='binary')
    note = fields.Char(required=True,default='')
    valueListString = fields.Char(required=True,default='')
    content = fields.Char(required=True,default='')
    type = fields.Selection([
        ('hard','Hard'),
        ('other_type','Other_type')
    ], default = 'hard', required=True)
    evidence = fields.Boolean(required=True, default=False) 
    lowerSign = fields.Selection([
        ('<'),
        ('<='),
        ('>'),
        ('>=')
    ], default=('>'))
    upperSign = fields.Selection([
        ('<'),
        ('<='),
        ('>'),
        ('>=')
    ], default=('>'))
    point = fields.Float(required=True, default=0)
    lowerPoint = fields.Float(default=0, required=True)
    upperPoint = fields.Float(default=0, required=True)
    createAt = fields.Datetime(default=fields.Datetime.now, required=True)
    updateAt = fields.Datetime(default=fields.Datetime.now, required=True)
    deleteAt= fields.Datetime()
    achievementId = fields.Integer() #Will be defined 
    
    sql_constraints = [
        ('criteria_pk', 'PRIMARY KEY (id)', '''Criteria's ID must be Primary Key'''),
    ]
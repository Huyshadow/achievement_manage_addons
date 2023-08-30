from odoo import models, fields, api


class User(models.Model):
    _name = 'database_manage.criteria'
    _description = ' Criteria from Tuyen duong Website'
    _inherit= []

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
    ], default = 'hard')
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
    point = fields.Float(required=True, default='0')
    lowerPoint = fields.Float(default= '0', required=True)
    upperPoint = fields.Float(default='0', required=True)
    createAt = fields.Datetime(default=fields.Datetime.now, required=True)
    updateAt = fields.Datetime(default=fields.Datetime.now, required=True)
    deleteAt= fields.Datetime()
    achievementRelated = fields.Many2one('database_manage.achievement', string="Achievement")
    achievementId = fields.Integer(related='achievementRelated.id', store=True)
    sql_constraints = [
        ('criteria_pk', 'PRIMARY KEY (id)', '''Criteria's ID must be Primary Key'''),
    ]
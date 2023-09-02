from odoo import models, fields, api
from datetime import datetime
class Achievement(models.Model):
    _name = 'database_manage.achievement'
    _description = 'Achievement of Tuyen duong Website'
    
    id = fields.Integer(string="ID", default=lambda self: self.env['ir.sequence'].next_by_code('database.manage.achievement'))
    name = fields.Char(string="Name",required=True)
    softCriteria = fields.Integer(string="Soft Criteria",required=True)
    description = fields.Text()
    createAt = fields.Datetime(default=fields.Datetime.now, required=True )
    updateAt = fields.Datetime()
    endAt = fields.Datetime()
    startAt = fields.Datetime()
    end_submit_at = fields.Datetime()
    lock = fields.Selection([
        ('unavailable', 'Unavailable'),
        ('available', 'Available')
    ], default='unavailable', required=True)
    type = fields.Selection([
        ('achievement', 'Achievement'),
        ('other_type', 'Other_type')
    ], default='achievement')
    manageUnit = fields.Text(default='{}')
    deleteAt=fields.Datetime()
    auditorFinalid = fields.Many2one('database_manage.user', string="AuditorFinal")
    #@api
    _sql_constraints = [
        ('achievement_pk', 'PRIMARY KEY (id)', 'Achievement ID must be unique.'),
    ]

    @api.model
    def create(self, vals):
        vals['id'] = self.env['ir.sequence'].next_by_code('database.manage.achievement')
        return super(Achievement, self).create(vals)


    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

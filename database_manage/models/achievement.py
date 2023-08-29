
from odoo import models, fields, api


class Achievement(models.Model):
    _name = 'database_manage.achievement'
    _description = 'Achievement of Tuyen duong Website'

    id = fields.Integer(string="ID", default=lambda self: self.env['ir.sequence'].next_by_code('database.manage.achievement'))
    name = fields.Char(string="Name",required=True, tracking=True)
    softCriteria = fields.Integer(string="Soft Criteria",required=True, tracking = True)
    description = fields.Text()
    createAt = fields.Datetime(default=fields.Datetime.now, required=True)
    updateAt = fields.Datetime(default=fields.Datetime.now, required=True)
    endAt = fields.Datetime(default=fields.Datetime.now, required=True)
    startAt = fields.Datetime(default=fields.Datetime.now, required=True)
    endSubmitAt = fields.Datetime(required=True,default=fields.Datetime.now)
    lock = fields.Selection([
        ('unavailable', 'Unavailable'),
        ('available', 'Available')
    ], default='unavailable', required=True)
    type = fields.Selection([
        ('achievement', 'Achievement'),
        ('other_type', 'Other_type')
    ], default='achievement')
    manageUnit = fields.Text(default='{}')
    deleteAt=fields.Datetime(required=True)
    #auditorFinalid = fields.Many2one('database-manage.user', string="Auditor Final")
    _sql_constraints = [
        ('achievement_pk', 'PRIMARY KEY (id)', 'Achievement ID must be unique.'),
        # ('achievement_auditor_fk', 'FOREIGN KEY ("auditorFinalId") REFERENCES "database-manage_user" (id)', 'Auditor Final must reference an existing User.')
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

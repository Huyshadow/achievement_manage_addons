from odoo import models, fields, api


class Achievement(models.Model):
    _name = 'database_manage.achievement'
    _description = 'Achievement of Tuyen duong Website'

    id = fields.Integer(string="ID", default=lambda self: self.env['ir.sequence'].next_by_code(
        'database.manage.achievement'))
    name = fields.Char(string="Name", required=True)
    softCriteria = fields.Integer(string="Soft Criteria", required=True)
    description = fields.Text()
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
    deleteAt = fields.Datetime()
    auditorFinalid = fields.Many2one(
        'database_manage.user', string="AuditorFinal")
    _sql_constraints = [
        ('achievement_pk', 'PRIMARY KEY (id)', 'Achievement ID must be unique.'),
    ]

    @api.model
    def create(self, vals):
        vals['id'] = self.env['ir.sequence'].next_by_code(
            'database.manage.achievement')
        return super(Achievement, self).create(vals)

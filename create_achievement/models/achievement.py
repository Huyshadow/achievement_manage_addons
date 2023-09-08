from odoo import models, fields, api
from datetime import datetime, timedelta


class Achievement(models.Model):
    _name = 'create_achievement.achievement'
    _description = 'Achievement Model of Create-Achievement Module'

    parent_id = fields.Many2one(
        'create_achievement.achievement', string="Root Model")

    criteria_ids = fields.One2many(
        'create_achievement.criteria', 'parent_id', string="Achivement's Criteria")

    id = fields.Integer(string="ID", default=lambda self: self.env['ir.sequence'].next_by_code(
        'create.achievement.achievement'))
    name = fields.Char(default="", required=True, string="Achievement's Title")
    soft_criteria = fields.Integer(string="Soft Criteria")
    description = fields.Text(string="Description")
    end_at = fields.Datetime(string="End time")
    start_at = fields.Datetime(string="Start time")
    end_submit_at = fields.Datetime()
    lock = fields.Selection([
        ('unavailable', 'Unavailable'),
        ('available', 'Available')
    ], default='unavailable', required=True)
    type = fields.Selection([
        ('achievement', 'Achievement'),
        ('other_type', 'Other_type')
    ], default='achievement', required=True)
    manage_unit = fields.Text(default='{}')
    delete_at = fields.Datetime()
    # last_updated_time = fields.Datetime(
    #     string='Last Updated Time', compute='_compute_last_updated_time')

    # @api.depends_context('last_updated_time_refresh')
    # def _compute_last_updated_time(self):
    #     for record in self:
    #         record.last_updated_time = fields.Datetime.now()

    # @api.model
    # def _refresh_last_updated_time(self):
    #     self.env.context = dict(
    #         self.env.context, last_updated_time_refresh=True)
    #     self.search([])._compute_last_updated_time()

    # @api.model
    # def _schedule_refresh_last_updated_time(self):
    #     self.env['ir.cron'].sudo().create({
    #         'name': 'Refresh Last Updated Time',
    #         'model_id': self.env.ref('model_my_class').id,
    #         'state': 'code',
    #         'code': 'model._refresh_last_updated_time()',
    #         'interval_number': 1,
    #         'interval_type': 'minutes',
    #         'numbercall': -1,
    #         'doall': True,
    #     })

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from pytz import timezone
from datetime import datetime, time, timedelta


class AchievementUser(models.Model):
    _name = 'achievement.user.list'
    _description = 'Achievement User Submit List'

    user_id = fields.Many2one(
        'res.users', 'Created By', default=lambda self: self.env.user)
    achievement_id = fields.Many2one(
        'create_achievement.achievement', string="ID danh hiệu")
    donvi_id = fields.Many2one(
        'manage_user_depart.department', string="ID đơn vị")
    appraise_status = fields.Selection(
        'Tình trạng danh hiệu', related='achievement_id.appraise_status')
    submit_list = fields.One2many(
        'achievement.submit', 'parent_id', string='Danh sách hồ sơ nộp')

    user_name = fields.Char(string="Tên người nộp", related='user_id.name')
    mssv_mscb = fields.Char(string="Mã số sinh viên/ cán bộ",
                            related='user_id.mssv_mscb', store=True)
    achievement_name = fields.Char(
        string="Tên danh hiệu", related='achievement_id.name')
    donvi_code = fields.Char(string="Mã đơn vị", related='donvi_id.code')
    donvi_name = fields.Char(
        string="Tên đơn vị", related='donvi_id.name', store=True)
    submit_at = fields.Datetime(string="Lần cuối nộp", store = True, compute = '_compute_submit_at')
    user_approve = fields.Boolean(string="Duyệt thành viên", default=False)

    @api.depends('submit_list.grade','submit_list.is_passed','submit_list.comment','submit_list.evidence',)
    def _compute_submit_at(self):
        for record in self:
            tz = timezone('Asia/Bangkok')
            current_local_time = datetime.now(tz) - timedelta(hours=7)
            string_time = current_local_time.strftime('%Y-%m-%d %H:%M:%S')
            submit_at = string_time
            record.submit_at = submit_at

    def import_donvi_id(self):
        submit_list = self.env['achievement.user.list'].search([])
        for submit in submit_list:
            if not submit.donvi_id:
                id = submit.user_id.donvi.id
                submit.write({
                    'donvi_id': id
                })

    @api.model
    def import_parent_id_for_achievement_submit(self):
        submit_list = self.env['achievement.submit'].search([])
        for submit in submit_list:
            if not submit.parent_id:
                parent = self.env['achievement.user.list'].search([
                    ('user_id', '=', submit.user_id.id),
                    ('achievement_id', '=',
                     submit.criteria.parent_id.parent_id.parent_id.id)
                ])
                submit.write({
                    'parent_id': parent.id
                })

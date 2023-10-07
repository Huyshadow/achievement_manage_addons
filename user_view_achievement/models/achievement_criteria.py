from odoo import models, fields, api


class AchivementCriteria(models.Model):
    _inherit = 'create_achievement.criteria'

    submit_ids = fields.One2many(
        'achievement.submit', 'criteria_id', 'Bản nộp')
    is_submitted = fields.Boolean(
        'Xác nhận nộp', compute='_compute_is_submitted')
    status = fields.Char(
        string="Tình Trạng", compute='_compute_status')

    @api.onchange('is_submitted')
    def _compute_status(self):
        for record in self:
            if record.is_submitted == True:
                record.status = "Đã nộp"
            else:
                record.status = "Chưa nộp"

    @api.depends('submit_ids')
    def _compute_is_submitted(self):
        for record in self:
            record.is_submitted = record.submit_ids.filtered(
                lambda s: s.user_id == self.env.user and s.submit == True)[:1] or False

    def action_submit_criteria(self):
        self.ensure_one()
        form_id = self.env.ref(
            'user_view_achievement.achievement_submit_view_form').id
        action = {
            'name': 'Nộp chỉ tiêu',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': form_id,
            'res_model': 'achievement.submit',
            'target': 'new',
        }
        current_submission = self.submit_ids.filtered(
            lambda s: s.user_id == self.env.user)[:1]
        if current_submission:
            action.update({
                'res_id': current_submission.id,
            })
        else:
            new_submission = self.env['achievement.submit'].create({
                'criteria_id': self.id,
            })
            action.update({
                'res_id': new_submission.id,
            })
        return action

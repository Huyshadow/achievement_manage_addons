from odoo import models, fields, api


class AchivementCriteria(models.Model):
    _inherit = 'create_achievement.criteria'

    submit_ids = fields.One2many('achievement.submit', 'criteria_id', 'Submissions')
    is_submitted = fields.Boolean('Is Submitted?', compute='_compute_is_submitted')

    @api.depends('submit_ids')
    def _compute_is_submitted(self):
        for record in self:
            self.is_submitted = self.submit_ids.filtered(lambda s: s.user_id == self.env.user)[:1] or False

    def action_submit_criteria(self):
        """
        Button to open submission form for criterias
        """
        self.ensure_one()
        form_id = self.env.ref('user_view_achievement.achievement_submit_view_form').id
        action = {
            'name': 'My Submission',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': form_id,
            'res_model': 'achievement.submit',
            'target': 'new',
        }
        current_submission = self.submit_ids.filtered(lambda s: s.user_id == self.env.user)[:1]
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

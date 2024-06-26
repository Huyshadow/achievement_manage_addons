from odoo import models, fields, api
from odoo.exceptions import ValidationError
import webbrowser


class AchievementSubmit(models.Model):
    _inherit = 'achievement.submit'
    display_group_name = fields.Char(
        string="Tên tập tiêu chí hiển thị", related='criteria.group_criteria_name', store=True)

    def action_bosung_hoso(self):
        form_id = self.env.ref(
            'user_view_achievement.achievement_submit_view_form').id
        action = {
            'name': 'Bổ sung chỉ tiêu',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': form_id,
            'res_model': 'achievement.submit',
            'target': 'new',
            'res_id': self.id,
        }
        return action

    def readonly_button(self):
        return True
    def action_expertise_submit(self):
        self.ensure_one()
        form_id = self.env.ref(
            'view_submit.comment_on_user_submit').id
        action = {
            'name': 'Thẩm định tiêu chí',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_id': form_id,
            'res_model': 'achievement.submit',
            'target': 'new',
            'res_id': self.id,
        }
        return action
        
    def create_url(self, target_id):
        protocol = "http"
        web_domain = "tuyenduong.tuoitredhqghcm.edu.vn"
        path = "/web/content?model=achievement.submit&field=evidence&filename_field=pdf_name&id="
        url = f"{protocol}://{web_domain}{path}{target_id}"
        return url

    def action_view_evidence(self):
        target_id = str(self.id)
        url = self.create_url(target_id)
        return {'name': 'test',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': url
                }

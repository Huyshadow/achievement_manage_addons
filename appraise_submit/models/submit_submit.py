from odoo import models, fields, api
from odoo.exceptions import ValidationError
import webbrowser


class AchievementSubmit(models.Model):
    _inherit = 'achievement.submit'
    display_group_name = fields.Char(
        string="Tên tập tiêu chí hiển thị", related='criteria.group_criteria_name', store=True)

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
        print(url)
        # webbrowser.open(url, new=2, autoraise=True)
        return {'name': 'test',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': url
                }

    def duyet(self):
        active_id = self.env.context.get('active_id')
        target = self.env['achievement.user.list'].search([
            ('id', '=', active_id),
        ])
        if target.user_approve:
            text = """Hồ sơ đã được duyệt"""
            query = 'delete from display_dialog_box'
            self.env.cr.execute(query)
            value = self.env['display.dialog.box'].sudo().create({
                'text': text})
            return {
                'type': 'ir.actions.act_window',
                'name': 'Thông báo',
                'res_model': 'display.dialog.box',
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new',
                'res_id': value.id
            }
        else:
            target.write({
                'user_approve': True
            })
            text = """Duyệt hồ sơ thành công"""
            query = 'delete from display_dialog_box'
            self.env.cr.execute(query)
            value = self.env['display.dialog.box'].sudo().create({
                'text': text})
            return {
                'type': 'ir.actions.act_window',
                'name': 'Thông báo',
                'res_model': 'display.dialog.box',
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new',
                'res_id': value.id
            }
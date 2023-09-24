from odoo import http
from odoo.http import request, route


class CreateAchievement(http.Controller):
    @http.route('/achievement', auth='public', website=True)
    def redirect_tree_view(self, **kwargs):
        url = "/web#action=85&model=create_achievement.achievement&view_type=list&menu_id=70"
        return request.redirect(url)

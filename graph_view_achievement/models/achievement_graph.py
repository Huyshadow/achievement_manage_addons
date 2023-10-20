from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Achievement(models.Model):
    _inherit = 'create_achievement.achievement'

    def action_view_graph(self):
        return {
            'name': self.name,
            'type': 'ir.actions.act_window',
            'view_mode': 'graph',
            'view_id': self.env.ref('graph_view_achievement.achievement_statistic_view_graph').id,
            'res_model': 'achievement.department.statistic',
            'target': 'current',
            'context': {
                'search_default_achievement_id': self.id,
            }
        }

    def action_view_graph_achievement(self):
        exist = self.env['achievement.department.statistic'].search([
            ('achievement_id', '=', self.id)
        ])
        department_list = self.env['manage_user_depart.department'].search([])
        if not exist:
            for department in department_list:
                total_list = self.env['achievement.user.list'].search([
                    ("donvi_name", '=', department.name),
                    ("achievement_id", '=', self.id)
                ])
                current_list = self.env['achievement.user.list'].search([
                    ('achievement_id.id', '=', self.id),
                    ('user_approve', '=', True),
                    ('donvi_name', '=', department.name),
                ])
                total = int(len(total_list))
                current = int(len(current_list))
                self.env['achievement.department.statistic'].create({
                    'achievement_id': self.id,
                    'depart_id': department.code,
                    'depart_name': department.name,
                    'num_of_submit': total,
                    'num_of_accept': current,
                })
        else:
            for department in department_list:
                total_list = self.env['achievement.user.list'].search([
                    ("donvi_name", '=', department.name),
                    ("achievement_id", '=', self.id)
                ])
                current_list = self.env['achievement.user.list'].search([
                    ('achievement_id.id', '=', self.id),
                    ('user_approve', '=', True),
                    ('donvi_name', '=', department.name),
                ])
                total = int(len(total_list))
                current = int(len(current_list))
                temp = self.env['achievement.department.statistic'].search([
                    ('achievement_id', '=', self.id),
                    ('depart_id', '=', department.code),
                    ('depart_name', '=', department.name),
                ])
                temp.write({
                    'num_of_submit': total,
                    'num_of_accept': current,
                })
        return {
            'name': self.name,
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'view_id': self.env.ref('graph_view_achievement.achievement_statistic_view_tree').id,
            'res_model': 'achievement.department.statistic',
            'target': 'current',
            'flags': {'hasSelectors': False},
            'context': {'graph_buttons': [{
                'action': "action_view_graph",
                'name': "Xem biểu đồ",
                'model': 'create_achievement.achievement'
            }]
            },
            'domain': [('achievement_id', '=', self.id)],
        }

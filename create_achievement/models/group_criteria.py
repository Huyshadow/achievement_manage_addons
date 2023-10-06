from odoo import models, fields, api


class GroupCriterias(models.Model):
    _name = 'create_achievement.group_criterias'
    _description = 'Group_Criteria for Tuyen duong Website'

    parent_id = fields.Many2one(
        "create_achievement.achievement", string="Danh hiệu")

    name = fields.Char(string="Tên tập tiêu chí", required=True)

    constraint_criterias = fields.One2many(
        "create_achievement.criteria", "parent_id_constraint", string="Danh sách tiêu chí bắt buộc")

    option_criterias = fields.One2many(
        "create_achievement.criteria", "parent_id_option", string="Danh sách tiêu chí khác")

    option_constraint = fields.Integer(
        string="Số tiêu chí khác bắt buộc", default=1)
    description = fields.Text(
        string="Mô tả", default="Không"
    )
    display_name = fields.Char(string="Tên hiển thị", store=True)
    

    constraint_criteria_count = fields.Integer(
        string="Số tiêu chí bắt buộc", compute="_compute_constraint_criteria_count")

    @api.depends('constraint_criterias')  # Specify the dependency
    def _compute_constraint_criteria_count(self):
        for record in self:
            record.constraint_criteria_count = len(record.constraint_criterias)
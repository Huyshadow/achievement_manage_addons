from odoo import models, fields, api


class GroupCriterias(models.Model):
    _name = 'create_achievement.group_criterias'
    _description = 'Group_Criteria for Tuyen duong Website'

    parent_id = fields.Many2one(
        "create_achievement.achievement", string="Danh hiệu")

    name = fields.Char(string="Tên tập tiêu chí", required=True)

    constrait_criterias = fields.One2many(
        "create_achievement.criteria", "parent_id_constraint", string="Danh sách tiêu chí bắt buộc")

    option_criterias = fields.One2many(
        "create_achievement.criteria", "parent_id_option", string="Danh sách tiêu chí tự chọn")

    option_constraint = fields.Integer(
        string="Số tiêu chí tự chọn bắt buộc", default=1)
    description = fields.Text(
        string="Mô tả", default="Không"
    )

    # just have 1 of this criteria
    # @api.model
    # def toggle_field_visibility_option(self, record_ids):
    #     records = self.browse(record_ids)
    #     records.write({'field_visible': not records.field_visible})
    #     return records.read()

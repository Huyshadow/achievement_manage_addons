from odoo import models, fields, api


class GroupCriterias(models.Model):
    _name = 'create_achievement.group_criterias'
    _description = 'Group_Criteria for Tuyen duong Website'

    parent_id = fields.Many2one(
        "create_achievement.achievement", string="Danh hiệu")

    name = fields.Char(string="Tên tập tiêu chí")

    constrait_criterias = fields.One2many(
        "create_achievement.criteria", "parent_id_constraint", string="Danh sách tiêu chí bắt buộc")

    option_criterias = fields.One2many(
        "create_achievement.criteria", "parent_id_option", string="Danh sách tiêu chí tự chọn")

    show_field_1 = fields.Boolean(string='Show Field1', default=False)
    show_field_2 = fields.Boolean(string='Show Field2', default=False)
    # just have 1 of this criteria

    def disable_constrait(self):
        self.show_field_1 = not self.show_field_1
        if (self.show_field_2 == True):
            self.show_field_2 = False

    def disable_option(self):
        self.show_field_2 = not self.show_field_2
        if (self.show_field_1 == True):
            self.show_field_1 = False

    # @api.model
    # def toggle_field_visibility_option(self, record_ids):
    #     records = self.browse(record_ids)
    #     records.write({'field_visible': not records.field_visible})
    #     return records.read()

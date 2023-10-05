from odoo import models, fields, api
from lxml import etree


class GroupCriterias(models.Model):
    _name = 'create_achievement.group_criterias'
    _description = 'Group_Criteria for Tuyen duong Website'

    parent_id = fields.Many2one(
        "create_achievement.achievement", string="Danh hiệu")

    name = fields.Char(string="Tên tập tiêu chí", required=True)
    num_of_group = fields.Integer(
        string="Số tập tiêu chí", required=True, default=0)

    # --------------------------------------------------------
    option_1_criterias = fields.One2many(
        "create_achievement.criteria", "parent_id_option_1")
    option_1_label = fields.Char(default="", translate=True)

    @api.depends('option_1_label')
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        # for record in self:
        result = super(GroupCriterias, self).fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        print(result)
        if view_type == 'form':
            doc = etree.XML(result['arch'])
            option_name = doc.xpath(
                "//page[@name='option_1']")
            if option_name:
                option_name[0].set("string", 'Huy')
                option_name[0].addnext(etree.Element(
                    'label', {'string': 'Huy'}))
                result['arch'] = etree.tostring(doc, encoding='unicode')
        print(result)
        return result
    # -------------------------------------------------------
    option_2_criterias = fields.One2many(
        "create_achievement.criteria", "parent_id_option_2")
    option_3_criterias = fields.One2many(
        "create_achievement.criteria", "parent_id_option_3")
    option_4_criterias = fields.One2many(
        "create_achievement.criteria", "parent_id_option_4")
    option_5_criterias = fields.One2many(
        "create_achievement.criteria", "parent_id_option_5")
    option_6_criterias = fields.One2many(
        "create_achievement.criteria", "parent_id_option_6")
    option_7_criterias = fields.One2many(
        "create_achievement.criteria", "parent_id_option_7")
    option_8_criterias = fields.One2many(
        "create_achievement.criteria", "parent_id_option_8")
    option_9_criterias = fields.One2many(
        "create_achievement.criteria", "parent_id_option_9")
    option_10_criterias = fields.One2many(
        "create_achievement.criteria", "parent_id_option_10")

    option_constraint = fields.Integer(
        string="Số tiêu chí khác bắt buộc", default=1)
    description = fields.Text(
        string="Mô tả", default="Không"
    )
    display_name = fields.Char(string="Tên hiển thị", store=True)

    @api.constrains('num_of_group')
    def _check_num_of_group(self):
        for record in self:
            if record.num_of_group > 10:
                raise ValidationError(
                    "Không thể tạo quá 10 tập tiêu chí")

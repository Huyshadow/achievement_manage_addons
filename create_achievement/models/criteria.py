from odoo import models, fields, api


class Criteria(models.Model):
    _name = 'create_achievement.criteria'
    _description = ' Criteria for Tuyen duong Website'

    parent_id = fields.Many2one('create_achievement.type_criterias')
    achievement_id = fields.Integer(string="Thuộc danh hiệu", related='parent_id.parent_id.id', store=True)
    group_criteria_name = fields.Char(string="Thuộc tập tiêu chí", related='parent_id.parent_id.name', store=True)
    type_group_criteria_name = fields.Char(string="Thuộc loại tiêu chí", related='parent_id.name', store=True)

    name = fields.Char(required=True, string="Tên tiêu chí")
    method = fields.Selection(
        [('thangdiem', 'Thang điểm'), ('nhiphan', 'Nhị Phân'), ('nhanxet', 'Người nộp tự nhận xét'), ('danhsach', 'Dạng danh sách')], default='', string="Phương thức", required=True)
    value_list_string = fields.Char()
    content = fields.Char(required=True, default='Không', string="Nội dung")
    note = fields.Char(required=True, default='Không', string="Ghi chú")
    evidence = fields.Boolean(
        required=True, default=False, string="Minh chứng")
    sign = fields.Selection([
        ('<', '<'),
        ('<=', '<='),
        ('>', '>'),
        ('>=', '>='),
        ('>= or <=', '>= hoặc <='),
        ('>= and <=', '>= và <='),
    ], default='', string="Dấu")
    point = fields.Float(default=0)
    lower_point = fields.Float(
        default=0, string="Khoảng cận dưới")
    upper_point = fields.Float(
        default=0, string="Khoảng cận trên")
    deleteAt = fields.Datetime()

    @api.onchange('method')
    def _onchange_method(self):
        if self.method:
            self.sign = ''
            self.lower_point = ''
            self.upper_point = ''

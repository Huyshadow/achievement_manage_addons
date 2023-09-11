from odoo import models, fields, api


class Criteria(models.Model):
    _name = 'create_achievement.criteria'
    _description = ' Criteria for Tuyen duong Website'

    parent_id = fields.Many2one(
        'create_achievement.achievement', string="Criterias for Achievement")
    self_many2one_id = fields.Many2one(
        'create_achievement.criteria', string="Tập danh hiệu"
    )
    self_one2many_id = fields.One2many(
        'create_achievement.criteria', 'self_many2one_id', string="Danh sách tiêu chí"
    )

    id = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code(
        'create.achievement.criteria'), copy=True, readonly=True)
    type = fields.Selection([
        ('tiêu chí', 'Tiêu chí'),
        ('tập tiêu chí', 'Tập tiêu chí')
    ], default='tiêu chí', string="Loại tiêu chí")

    name = fields.Char(required=True, string="Tên tiêu chí")
    is_criteria = fields.Boolean(default=False)
    method = fields.Selection(
        [('thang điểm', 'Thang điểm'), ('nhi phân', 'Nhị Phân'), ('người nộp tự nhận xét', 'Người nộp tự nhận xét'), ('dạng danh sách', 'Dạng danh sách')], default='', string="Phương thức")
    value_list_string = fields.Char()
    note = fields.Char(required=True, default='Không', string="Chú thích")
    content = fields.Char(required=True, default='Không', string="Nội dung")
    evidence = fields.Boolean(
        required=True, default=False, string="Minh chứng")
    sign = fields.Selection([
        ('<', '<'),
        ('<=', '<='),
        ('>', '>'),
        ('>=', '>='),
        ('>= or <=', '>= or <='),
        ('>= and <=', '>= and <='),
    ], default='', string="Dấu")
    point = fields.Float(default=0)
    lower_point = fields.Float(
        default=0, required=True, string="Khoảng cận dưới")
    upper_point = fields.Float(
        default=0, required=True, string="Khoảng cận trên")
    deleteAt = fields.Datetime()

    @api.onchange('method')
    def _onchange_method(self):
        if self.method:
            self.sign = ''
            self.lower_point = ''
            self.upper_point = ''

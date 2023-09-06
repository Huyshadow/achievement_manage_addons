from odoo import models, fields, api


class Criteria(models.Model):
    _name = 'create_achievement.criteria'
    _description = ' Criteria for Tuyen duong Website'

    parent_id = fields.Many2one(
        'create_achievement.achievement', string="Criterias for Achievement")

    id = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code(
        'create.achievement.criteria'), required=True, copy=True, readonly=True)
    type = fields.Selection([
        ('tiêu chí', 'Tiêu chí'),
        ('tập tiêu chí', 'Tập tiêu chí')
    ], default='tiêu chí', required=True)
    name = fields.Char(required=True)
    isCriteria = fields.Boolean(required=True, default=False)
    method = fields.Selection(
        [('thang điểm', 'Thang điểm'), ('nhi phân', 'Nhị Phân'), ('người nộp tự nhận xét', 'Người nộp tự nhận xét'), ('dạng danh sách', 'Dạng danh sách')], required=True, default='binary')
    valueListString = fields.Char(required=True, default='')
    note = fields.Char(required=True, default='')
    content = fields.Char(required=True, default='')
    evidence = fields.Boolean(required=True, default=False)
    lowerSign = fields.Selection([
        ('<', '<'),
        ('<=', '<='),
        ('>', '>'),
        ('>=', '>=')
    ], default=('>'), required=True)
    upperSign = fields.Selection([
        ('<', '<'),
        ('<=', '<='),
        ('>', '>'),
        ('>=', '>=')
    ], default=('>'), required=True)
    point = fields.Float(default=0, required=True)
    lowerPoint = fields.Float(default=0, required=True)
    upperPoint = fields.Float(default=0, required=True)
    deleteAt = fields.Datetime()
    parent_id = fields.Many2one(
        'create_achievement.achievement', string='''Achievement's Criteria''')

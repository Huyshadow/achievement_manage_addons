from odoo import models, fields, api


class Criteria(models.Model):
	_name = 'create_achievement.criteria'
	_description = ' Criteria for Tuyen duong Website'

	parent_id_constraint = fields.Many2one(
		'create_achievement.group_criterias', string="Danh sách tiêu chí Bắt buộc")
	parent_id_option = fields.Many2one(
		'create_achievement.group_criterias', string="Danh sách tiêu chí Tự do")

	id = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code(
		'create.achievement.criteria'), copy=True, readonly=True)
	type = fields.Selection([
		('tiêu chí', 'Tiêu chí'),
	], default='tiêu chí', string="Loại tiêu chí")

	name = fields.Char(required=True, string="Tên tiêu chí")
	is_criteria = fields.Boolean(default=False)
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
		('>= or <=', '>= or <='),
		('>= and <=', '>= and <='),
	], default='', string="Dấu")
	point = fields.Float(default=0)
	lower_point = fields.Float(
		default=0, string="Khoảng cận dưới")
	upper_point = fields.Float(
		default=0, string="Khoảng cận trên")
	deleteAt = fields.Datetime()

	category = fields.Char(string="Phân loại tiêu chí", compute="_compute_category", store=True)    
	group_criteria = fields.Char(string="Thuộc tập tiêu chí", compute="_compute_group_criteria", store=True)
	achievement_id = fields.Char(string="Thuộc danh hiệu", compute="_compute_achievement_id", store=True)

	@api.depends('parent_id_constraint', 'parent_id_option')
	def _compute_achievement_id(self):
		for record in self:
			if record.parent_id_constraint:
				record.achievement_id = record.parent_id_constraint.parent_id.id
			elif record.parent_id_option:
				record.achievement_id = record.parent_id_option.parent_id.id
			else:
				record.achievement_id = 'None'

	@api.depends('parent_id_constraint', 'parent_id_option')
	def _compute_group_criteria(self):
		for record in self:
			if record.parent_id_constraint:
				record.group_criteria = record.parent_id_constraint.name
			elif record.parent_id_option:
				record.group_criteria = record.parent_id_option.name
			else:
				record.group_criteria = 'None'

	@api.depends('parent_id_constraint', 'parent_id_option')
	def _compute_category(self):
		for record in self:
			if record.parent_id_constraint:
				record.category = 'Tiêu chí Bắt buộc'
			elif record.parent_id_option:
				record.category = 'Tiêu chí Tự do'
			else:
				record.category = 'None'

	@api.onchange('method')
	def _onchange_method(self):
		if self.method:
			self.sign = ''
			self.lower_point = ''
			self.upper_point = ''

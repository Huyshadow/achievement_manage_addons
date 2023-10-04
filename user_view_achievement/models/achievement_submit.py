from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, time, timedelta
from pytz import timezone
import os


class AchievementSubmit(models.Model):
	_name = 'achievement.submit'
	_description = 'Achievement Submit'

	user_id = fields.Many2one('res.users', 'Created By', default=lambda self: self.env.user)
	criteria_id = fields.Many2one('create_achievement.criteria', 'Tieu chi')
	criteria_name = fields.Char('Tên tiêu chí', related='criteria_id.name')
	criteria_content = fields.Char('Mô tả', related='criteria_id.content')
	criteria_method = fields.Selection('Phương thức', related='criteria_id.method', related_sudo=False)
	
	group_criteria_name = fields.Char('Tên tập tiêu chí', related='criteria_id.group_criteria')
	category = fields.Char('Loại tiêu chí', related='criteria_id.category')
	achievement_id = fields.Integer('ID danh hiệu', related = 'criteria_id.achievement_id')
	achievement_name = fields.Char('Tên danh hiệu', compute = '_get_achievement_name',store = True)
	expertise = fields.Boolean(string="Thẩm định", default = False)
	# expertise = fields.Selection([
	#     ('passed', 'Đã đạt'),
	#     ('not_passed', 'Chưa đạt'),
	# 	('need_evidence', 'Thiếu minh chứng')
	# ], default='hard', required=True)
	
	@api.depends('achievement_id')
	def _get_achievement_name(self):
		for record in self:
			record.achievement_name = record.env['manage_user_depart.department'].browse(record.achievement_id).name

	grade = fields.Integer('Điểm')
	is_passed = fields.Boolean('Đã đạt')
	comment = fields.Text(string='Tự nhận xét')
	evidence = fields.Binary(string='Minh Chứng(file .pdf)')
	pdf_name = fields.Char(string='Tên file pdf')
	submit = fields.Boolean('Đã nộp', compute="_check_submit", store=True)
	
	@api.depends('grade', 'is_passed', 'comment')
	def _check_submit(self):
		for record in self:
			if record.criteria_method == "thangdiem":
				if record.grade:
					record.submit = True
					record.add_user_list()
			elif record.criteria_method == "nhiphan":
				if record.is_passed == True:
					record.submit = True
					record.add_user_list()
			elif record.criteria_method == "nhanxet":
				if record.comment:
					record.submit = True
					record.add_user_list()
			else:
				record.submit = False

	@api.constrains('evidence')
	def _check_file(self):
		if os.path.splitext(str(self.pdf_name))[1] != '.pdf':
			raise ValidationError("Chỉ nhận file PDF")

	def add_user_list(self):
		for record in self:
			user_id = record.user_id.id
			achievement_id = record.criteria_id.achievement_id

			tz = timezone('Asia/Bangkok')
			future_date = record.create_date + timedelta(days=0)
			default_time = time(hour=0, minute=0, second=0)
			naive_datetime = datetime.combine(future_date, default_time)
			local_datetime = tz.localize(naive_datetime)
			utc_datetime = local_datetime.astimezone(timezone('UTC'))
			check_time = utc_datetime.replace(tzinfo=None)

			submit_at = check_time

			# Check if a corresponding record already exists, and if not, create it
			existing_achievement_user = self.env['achievement.user.list'].search([
				('user_id', '=', user_id),
				('achievement_id', '=', achievement_id),
			])

			if not existing_achievement_user:
				self.env['achievement.user.list'].create({
					'user_id': user_id,
					'user_name': record.user_id.name,
					'achievement_name': record.criteria_id.achievement_name,
					'achievement_id': achievement_id,
					'donvi_name': record.user_id.donvi.name,
					'submit_at': submit_at
				})
			else:
				existing_achievement_user.write({'submit_at': submit_at})

	submit_content = fields.Char(string="Nội dung khai", compute="_compute_submit_content", store=True)
	@api.depends('grade', 'is_passed','comment')
	def _compute_submit_content(self):
		for record in self:
			if record.criteria_method == "thangdiem":
				if record.grade:
					record.submit_content = str(record.grade)
			if record.criteria_method == "nhiphan":
				if record.is_passed:
					record.submit_content = "Đã đạt"
			if record.criteria_method == "nhanxet":
				if record.comment:
					record.submit_content = record.comment
			else:
				record.submit_content = "Chưa điền"


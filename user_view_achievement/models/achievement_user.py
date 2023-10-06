from odoo import models, fields, api
from odoo.exceptions import ValidationError


class AchievementUser(models.Model):
	_name = 'achievement.user.list'
	_description = 'Achievement User Submit List'

	user_id = fields.Integer(string="ID người nộp")
	achievement_id = fields.Integer(string="ID danh hiệu")


	user_name = fields.Char(string="Tên người nộp")
	achievement_name = fields.Char(string="Tên danh hiệu")
	donvi_name=  fields.Char(string="Tên đơn vị")
	submit_at = fields.Datetime()
	
	expertise = fields.Boolean(string="Thẩm định",default =False, compute ='_compute_expertise', store = True)
	approve = fields.Boolean(string="Duyệt",default =False)

	@api.depends('submit_at')
	def _compute_expertise(self):
		group_criteria_list =  self.env['create_achievement.achievement'].search([
			('parent_id.id', '=', achievement_id)
		])

		for group_criteria in group_criteria_list:
			
			constraint_check = True
			option_check = True
			
			constraint_criteria_ids_list = []
			for record in group_criteria.contraint_criterias:
				constraint_criteria_ids_list.append(record.id)

			for id in constraint_criteria_ids_list:
				exist_submit = self.env['achievement.submit'].search([
					('user_id', '=', user_id),
					('criteria_id', '=', id)
				])
				if exist_submit:
					if exist_submit.submit_content == "Chưa điền":
						constraint_check = False
						break
				else:
					constraint_check = False
					break
			
			if constraint_check:
				option_criteria_ids_list = []
				for record in group_criteria.option_criterias:
					option_criteria_ids_list.append(record.id)
				num_option_criteria = group_criteria.option_constraint

		self.env['achievement.submit'].search([
				('user_id', '=', user_id),
				('achievement_id', '=', achievement_id),
		])

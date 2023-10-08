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
	
	# criteria_submited_list = fields.Char(string="ID tiêu chuẩn đã nộp", compute ='_compute_criteria_submited_list', store = True)
	# type_submited_list = fields.Char(string="ID loại tiêu chí đã nộp đủ", compute ='_compute_type_submited_list', store = True)
	# group_submited_list = fields.Char(string="ID tập tiêu chí đã nộp đủ", compute ='_compute_group_submited_list', store = True)

	full_submit = fields.Boolean(string="Đã nộp đủ tất cả tiêu chí", default=False)
	user_approve = fields.Boolean(string="Duyệt thành viên",default=False)
	expertise = fields.Boolean(string="Thẩm định",default =False, compute ='_compute_expertise', store = True)
	approve = fields.Boolean(string="Thông qua",default=False)

	# @api.depends('submit_at')
	# def _compute_criteria_submited_list(self):
	# 	for record in self:
	# 		if record.criteria_submited_list:
	# 			current_criteria_list = [int(id) for id in record.criteria_submited_list.split(',')]
	# 			criteria_submit = self.env['achievement.submit'].search([
	# 				('user_id', '=',record.user_id),
	# 				('criteria.parent_id.parent_id.parent_id.id','=',record.achievement_id),
	# 				('criteria_id', 'not in', current_criteria_list)
	# 			])
	# 			if criteria_submit and criteria_submit.submit:
	# 				record.criteria_submited_list += ',' + str(criteria_submit_id)
	# 		else:
	# 			criteria_submit_id = self.env['achievement.submit'].search([
	# 				('user_id', '=',record.user_id),
	# 				('criteria.parent_id.parent_id.parent_id.id','=',record.achievement_id),
	# 			])
	# 			record.criteria_submited_list = str(criteria_submit_id)
	
	# @api.depends('criteria_submited_list')
	# def _compute_type_submited_list(self):
	# 	for record in self:
	# 		if record.type_submited_list:
	# 			current_type_list = [int(id) for id in record.type_submited_list.split(',')]
	# 			temp_type_list = self.env['create_achievement.type_criterias'].search([
	# 				('parent_id.parent_id.id','=',record.achievement_id),
	# 				('id', 'not in', current_type_list)
	# 			])
	# 			for type_criteria in temp_type_list:
	# 				submit_criteria_list = [int(id) for id in record.criteria_submited_list.split(',')]
					
	# 				temp_criteria_list = []
	# 				for criteria in type_criteria.criteria_ids:
	# 					temp_criteria_list.append(criteria.id)

	# 				if type_criteria.constraint == 'all':
						
	# 				elif type_criteria.constraint == 'some':

	# 				else:
	# 					continue
				
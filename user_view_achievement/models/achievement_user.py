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
	
	expertise = fields.Boolean(string="Thẩm định",default =False)
	result = fields.Boolean(string="Duyệt",default =False)

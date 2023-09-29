from odoo import models, fields, api

class User(models.Model):
	_inherit = 'res.users'
	
	@api.model
	def open_user_profile(self):
		return {
			'name': 'Thông tin cá nhân',
			'type': 'ir.actions.act_window',
			'view_mode': 'form',
			'views': [(False, 'form')],
			'res_model': 'res.users',
			'res_id': self.env.user.id,
			'target': 'current',
		}
	is_fill_info = fields.Boolean(string = "Đã cập nhập thông tin?", compute='_check_fill_info', store = True)
	
	@api.depends('mssv_mscb','canhan_email','sdt','donvi')
	def _check_fill_info(self):
		for record in self:
			if record.mssv_mscb and record.canhan_email and record.sdt and record.donvi:
				record.is_fill_info = True
			else:
				record.is_fill_info = False
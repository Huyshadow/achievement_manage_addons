# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class smart_login_page(models.Model):
#     _name = 'login.page'
#     _description = 'smart_login_page'

#     name = fields.Char()
#     photo = fields.Image(string='Photo', attachment=True, store=True)
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

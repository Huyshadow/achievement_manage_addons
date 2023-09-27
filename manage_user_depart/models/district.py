from odoo import models, fields, api
import requests
import json
import os

class UserDistrictInfo(models.Model):
  _name = 'user.district.info'
  _description = 'User District Info'
  
  name = fields.Char('Name', required=True)
  code = fields.Integer('Code', required=True)
  division_type = fields.Char('Division Type')
  codename = fields.Char('Codename')
  province_id = fields.Many2one('user.province.info', 'Province')
  wards = fields.One2many('user.ward.info', 'district_id', 'Wards')

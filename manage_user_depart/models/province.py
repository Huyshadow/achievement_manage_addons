from odoo import models, fields, api
import requests
import json
import os

class UserProvinceInfo(models.Model):
  _name = 'user.province.info'
  _description = 'User Province Info'
  
  name = fields.Char('Name', required=True)
  code = fields.Integer('Code', required=True)
  division_type = fields.Char('Division Type')
  codename = fields.Char('Codename')
  phone_code = fields.Integer('Phone Code')
  districts = fields.One2many('user.district.info', 'province_id', 'Districts')

  

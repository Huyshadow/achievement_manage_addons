from odoo import models, fields, api

class ContactInfo(models.Model):
    _name = 'database_manage.contact_info'
    _description = 'Contact information of user from Tuyen duong Website'

    id = fields.Integer(default=lambda self: self.env['ir.sequence'].next_by_code('database.manage.contact_info'), required=True, copy=True, readonly=True)
    gender = fields.Char(default = 'Male', required=True)
    nation = fields.Char(default = '')
    emailPersonal = fields.Char(default='')
    religion = fields.Char(default='')
    birthday = fields.Datetime()
    studentAssociation = fields.Datetime()
    CMND = fields.Char(default='')
    homeTown = fields.Char(default='')
    resident = fields.Char(default='')
    phone = fields.Char(default='')
    placeUnion = fields.Char(default='')
    dateAtUnion = fields.Datetime()
    dateAtCommunistParty = fields.Datetime()
    placeCommunistParty = fields.Char(default='')
    createAt = fields.Datetime(default=fields.Datetime.now, required=True)
    updateAt = fields.Datetime(default=fields.Datetime.now, required=True)
    deleteAt= fields.Datetime()
    userId = fields.Many2one('database_manage.user', string='UserId')

    sql_constraints = [
        ('contact_info_pk', 'PRIMARY KEY (id)', 'Contact ID must be Primary Key'),
        ('contact_info_unique_pk', 'UNIQUE (userId)')
    ]
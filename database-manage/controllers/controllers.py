# -*- coding: utf-8 -*-
# from odoo import http


# class Database-manage(http.Controller):
#     @http.route('/database-manage/database-manage', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/database-manage/database-manage/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('database-manage.listing', {
#             'root': '/database-manage/database-manage',
#             'objects': http.request.env['database-manage.database-manage'].search([]),
#         })

#     @http.route('/database-manage/database-manage/objects/<model("database-manage.database-manage"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('database-manage.object', {
#             'object': obj
#         })

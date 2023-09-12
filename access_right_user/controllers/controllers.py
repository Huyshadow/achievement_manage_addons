# -*- coding: utf-8 -*-
# from odoo import http


# class AccessRightUser(http.Controller):
#     @http.route('/access_right_user/access_right_user', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/access_right_user/access_right_user/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('access_right_user.listing', {
#             'root': '/access_right_user/access_right_user',
#             'objects': http.request.env['access_right_user.access_right_user'].search([]),
#         })

#     @http.route('/access_right_user/access_right_user/objects/<model("access_right_user.access_right_user"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('access_right_user.object', {
#             'object': obj
#         })

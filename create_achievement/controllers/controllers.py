# -*- coding: utf-8 -*-
# from odoo import http


# class CreateAchievement(http.Controller):
#     @http.route('/create_achievement/create_achievement', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/create_achievement/create_achievement/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('create_achievement.listing', {
#             'root': '/create_achievement/create_achievement',
#             'objects': http.request.env['create_achievement.create_achievement'].search([]),
#         })

#     @http.route('/create_achievement/create_achievement/objects/<model("create_achievement.create_achievement"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('create_achievement.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-
# from odoo import http
# from odoo.http import request

# class SmartLoginPage(http.Controller):
#     @http.route('/web/login', auth='public', website= True,)
#     def index(self, **kw):
#         info_card = request.env['login.page'].search([])
#         return http.request.render('smart_login_page.custom_login',{
#             'info_card' : info_card, 
#         })

#     @http.route('/smart_login_page/smart_login_page/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('smart_login_page.listing', {
#             'root': '/smart_login_page/smart_login_page',
#             'objects': http.request.env['smart_login_page.smart_login_page'].search([]),
#         })

#     @http.route('/smart_login_page/smart_login_page/objects/<model("smart_login_page.smart_login_page"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('smart_login_page.object', {
#             'object': obj
#         })

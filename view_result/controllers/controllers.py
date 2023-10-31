# -*- coding: utf-8 -*-
# from odoo import http


# class ViewResult(http.Controller):
#     @http.route('/view_result/view_result', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/view_result/view_result/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('view_result.listing', {
#             'root': '/view_result/view_result',
#             'objects': http.request.env['view_result.view_result'].search([]),
#         })

#     @http.route('/view_result/view_result/objects/<model("view_result.view_result"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('view_result.object', {
#             'object': obj
#         })

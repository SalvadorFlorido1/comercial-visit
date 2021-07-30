# -*- coding: utf-8 -*-
from odoo import http

# class AllCustomCrm(http.Controller):
#     @http.route('/all_custom_crm/all_custom_crm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/all_custom_crm/all_custom_crm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('all_custom_crm.listing', {
#             'root': '/all_custom_crm/all_custom_crm',
#             'objects': http.request.env['all_custom_crm.all_custom_crm'].search([]),
#         })

#     @http.route('/all_custom_crm/all_custom_crm/objects/<model("all_custom_crm.all_custom_crm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('all_custom_crm.object', {
#             'object': obj
#         })
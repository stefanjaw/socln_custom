# -*- coding: utf-8 -*-
from odoo import http

# class MissingFields(http.Controller):
#     @http.route('/missing_fields/missing_fields/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/missing_fields/missing_fields/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('missing_fields.listing', {
#             'root': '/missing_fields/missing_fields',
#             'objects': http.request.env['missing_fields.missing_fields'].search([]),
#         })

#     @http.route('/missing_fields/missing_fields/objects/<model("missing_fields.missing_fields"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('missing_fields.object', {
#             'object': obj
#         })
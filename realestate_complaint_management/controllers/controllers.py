# -*- coding: utf-8 -*-
# from odoo import http


# class RealestateComplaintManagement(http.Controller):
#     @http.route('/realestate_complaint_management/realestate_complaint_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/realestate_complaint_management/realestate_complaint_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('realestate_complaint_management.listing', {
#             'root': '/realestate_complaint_management/realestate_complaint_management',
#             'objects': http.request.env['realestate_complaint_management.realestate_complaint_management'].search([]),
#         })

#     @http.route('/realestate_complaint_management/realestate_complaint_management/objects/<model("realestate_complaint_management.realestate_complaint_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('realestate_complaint_management.object', {
#             'object': obj
#         })

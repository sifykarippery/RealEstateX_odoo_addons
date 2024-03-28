# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
from werkzeug.exceptions import BadRequest

import logging
_logger = logging.getLogger(__name__)


class RealestateComplaintForm(http.Controller):
    @http.route(['/ask_realestatex/'],auth="public", website=True)
    def complaint_form(self,**kw):
        """
                This method renders the complaint form page and loads data for many2one fields.

                :return: HTTP response with the rendered templates.xml
        """

        try:
            # Load data for many2one fields
            countries = request.env['res.country'].sudo().search([])
            states = request.env['res.country.state'].sudo().search([])
            type_complaint = request.env['complaint.type'].sudo().search([])

            # Prepare data to pass to the templates.xml
            vals = {
                'countries': countries,
                'states': states,
                'type_complaint': type_complaint
            }

            return request.render("realestate_complaint_management.complaint_management_template", vals)

        except Exception as e:
            # Return an error response
            return request.render("realestate_complaint_management.error_message_template", {'error_message': str(e)})

    @http.route('/ask_realestatex/submit/',type='http', auth='public',website=True)
    def complaint_form_submit(self, **post):
        try:
            # model operation
            country_id=post.get('country_id')
            country = request.env['res.country'].sudo().search([('name','=',country_id)])
            state_id=post.get('state_id')
            state = request.env['res.country.state'].sudo().search([('name','=',state_id)])
            type_id=post.get('type')
            type_complaint = request.env['complaint.type'].sudo().search([('name','=',type_id)])
            complaint_detail = request.env['realestate.complaint'].sudo().create({
                'customer_name': post.get('name'),
                'email': post.get('email'),
                'street1':post.get('street1'),
                'street2':post.get('street2'),
                'zip':post.get('zip'),
                'country_id':country.id if country.id else country,
                'state_id':state.id if state.id else state,
                'complaint_type':type_complaint.id,
                'description':post.get('description')
            })
            complaint_detail.sudo().action_send_email()
            vals = {
                'complaint_detail': complaint_detail,
            }
            return request.render("realestate_complaint_management.complaint_form_success",vals)

        except Exception as e:
            error_message = str(e)
            return request.render('realestate_complaint_management.error_message_template', {'error_message': error_message})



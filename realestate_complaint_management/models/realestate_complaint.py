# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)



class ComplaintType(models.Model):
    _name = 'complaint.type'

    name = fields.Char("Complaint Type")

class RealestateComplaint(models.Model):

    _name = 'realestate.complaint'
    _description = 'Realestate_complaint_management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name='complaint_reference'
    _order = 'complaint_reference desc'

    complaint_reference=fields.Char(string='Complaint Reference', required=True,
                          readonly=True)
    customer_name = fields.Char("Customer Name")
    email = fields.Char("Email")
    phone=fields.Char('Phone')
    street1=fields.Char("Street1")
    street2=fields.Char("street2")
    city=fields.Char("City")
    state_id=fields.Many2one('res.country.state')
    zip=fields.Char("Zip")
    country_id=fields.Many2one('res.country')
    complaint_type=fields.Many2one('complaint.type')
    description=fields.Text("Description")
    action_plan=fields.Text("Action Plan")
    complaint_date = fields.Date(string='Complaint Date', default=datetime.today())

    state=fields.Selection([('draft', 'New'), ('review', 'In Review'),
                                 ('progress', 'In Progress'), ('solved', 'Solved'),
                                 ('drop', 'Dropped')],string='Complaint Status',
                                default='draft', track_visibility='always',group_expand='_group_expand_states')


    @api.model
    def create(self, vals):
        '''Reference number update automate with sequence'''

        vals['complaint_reference'] = self.env['ir.sequence'].next_by_code(
                'realestate.complaint')
        res = super(RealestateComplaint, self).create(vals)
        return res

    def _group_expand_states(self, states, domain, order):
        '''
            This function display state in Kanban view
        '''
        return [key for key, val in type(self).state.selection]

    def action_review_complaint(self):
        if self.state == 'draft':
            self.state='review'
        return

    def action_progress_complaint(self):
        if self.state == 'review':
            self.state = 'progress'
        return

    def action_solved_complaint(self):
        if self.state in ['progress','review']:
            self.state = 'solved'
            self.action_send_email()

        return

    def action_drop_complaint(self):
        if self.state in ('draft','review','progress'):
            self.state = 'drop'
            self.action_send_email()

        return

    def action_send_email(self):
        '''
            This function send mail when complaint register ,solve/dropped
        '''
        mail_template = self.env.ref('realestate_complaint_management.mail_template_complaint_info')
        mail_template.send_mail(self.id, force_send=True)
        return True

    def action_open_email_wizard(self):
        '''
            This function opens a window to compose an email,Its for email customer if it complaint type question
        '''
        self.ensure_one()
        compose_form = self.env.ref('mail.email_compose_message_wizard_form', False)

        return {
            'name': _('Contact Customer'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form.id, 'form')],
            'view_id': compose_form.id,
            'target': 'new',
        }








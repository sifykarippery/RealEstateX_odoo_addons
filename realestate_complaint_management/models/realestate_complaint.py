# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from datetime import datetime




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
        vals['complaint_reference'] = self.env['ir.sequence'].next_by_code(
                'realestate.complaint')
        res = super(RealestateComplaint, self).create(vals)

        return res

    def _group_expand_states(self, states, domain, order):
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
        if self.state == 'progress':
            self.state = 'solved'
            self.action_send_email()

        return

    def action_drop_complaint(self):
        if self.state in ('draft','review','progress','solved'):
            self.state = 'drop'
            self.action_send_email()

        return

    def action_send_email(self):
        # Create the record
        # Send email
        mail_template = self.env.ref('realestate_complaint_management.mail_template_complaint_info')
        mail_template.send_mail(self.id, force_send=True)

        return








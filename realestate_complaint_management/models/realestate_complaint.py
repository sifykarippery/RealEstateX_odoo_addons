# -*- coding: utf-8 -*-

from odoo import models, fields, api,_


class ComplaintType(models.Model):
    _name = 'complaint.type'

    name = fields.Char("Complaint Type")

class RealestateComplaint(models.Model):
    _name = 'realestate.complaint'
    _description = 'Realestate_complaint_management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name='complaint_reference'

    complaint_reference=fields.Char(string='Complaint Reference', required=True,
                          readonly=True)
    customer_name = fields.Char("Customer Name")
    email = fields.Char("Email")
    address=fields.Text("Address")
    complaint_type=fields.Many2one('complaint.type')
    description=fields.Text("Description")
    action_plan=fields.Text("Action Plan")
    state=fields.Selection([('draft', 'New'), ('review', 'In Review'),
                                 ('progress', 'In Progress'), ('solved', 'Solved'),
                                 ('drop', 'Dropped')],string='Complaint Status',
                                default='draft', track_visibility='always')

    @api.model
    def create(self, vals):
        vals['complaint_reference'] = self.env['ir.sequence'].next_by_code(
                'realestate.complaint')
        res = super(RealestateComplaint, self).create(vals)
        return res

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
        return

    def action_drop_complaint(self):
        if self.state in ('draft','review','progress','solved'):
            self.state = 'drop'
        return
    def action_reset(self):
        if self.state in ('review','progress','solved'):
            self.state = 'draft'
        return






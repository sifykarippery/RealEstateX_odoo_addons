
from odoo.tests import common
class TestModule(common.TransactionCase):

    def setUp(self):
        super(TestModule, self).setUp()
        self.complaint_type = self.env['complaint.type'].create({'name': 'test_type'})

        self.complaint = self.env['realestate.complaint'].create({
            'customer_name': 'bob',
            'email': 'testemail@example.com',
            'street1': 'st.francis str.',
            'street2': 'no.15',
            'zip': '56743',
            'country_id': 104,
            'state_id': 593,
            'complaint_type': self.complaint_type.id,
            'description': 'testcomplaint detail'})

    def test_pipeline_actions(self):
        # Action: Review Complaint
        self.complaint.action_review_complaint()
        self.assertEqual(self.complaint.state, 'review', "Complaint should be in 'review'.")

        # Action: Progress Complaint
        self.complaint.action_progress_complaint()
        self.assertEqual(self.complaint.state, 'progress', "Complaint should be in 'progress'.")

        # Action: Solve Complaint
        self.complaint.action_solved_complaint()
        self.assertEqual(self.complaint.state, 'solved', "Complaint should be in 'solved'.")

    def test_pipeline_invalid_order(self):
        # Action: Review Complaint
        self.complaint.action_review_complaint()
        self.assertEqual(self.complaint.state, 'review', "Complaint should be in 'review'.")

        # Action: Solve Complaint
        self.complaint.action_solved_complaint()
        self.assertEqual(self.complaint.state, 'solved', "Complaint should be in 'solved'.")

        # Action: Progress Complaint (Invalid order)
        self.complaint.action_progress_complaint()
        self.assertNotEqual(self.complaint.state, 'progress', "Complaint should remain in 'solved' state after trying to progress again.")

    def test_action_send_email(self):
        # Action: Automate Send email to customer state in ['draft','solved','dropped']
        action=self.complaint.action_send_email()
        self.assertTrue(action, "Complaint status should send to customer")

    def test_action_open_email_wizard(self):
        # Action: Open email template wizard to send email when complaint type question
        action=self.complaint.action_open_email_wizard()
        self.assertTrue(action, "Open email template wizard to send email")

    def test_pipeline_drop_order(self):
        #Action: Drop complaint when in review,progress not in solved
        self.complaint.action_review_complaint()
        self.assertEqual(self.complaint.state, 'review', "Complaint should be in 'review'.")

        # Action: Drop Complaint
        self.complaint.action_drop_complaint()
        self.assertEqual(self.complaint.state, 'drop', "Complaint should be  in 'drop'.")

    def test_pipeline_drop_invalid_order(self):
        # Action: Review Complaint
        self.complaint.action_review_complaint()
        self.assertEqual(self.complaint.state, 'review', "Complaint should be in 'review'.")

        #Action: Drop complaint when in review,progress not in solved
        self.complaint.action_solved_complaint()
        self.assertEqual(self.complaint.state, 'solved', "Complaint should be in 'solved'.")

        # Action: Drop Complaint invalid drop
        self.complaint.action_drop_complaint()
        self.assertNotEqual(self.complaint.state, 'drop', "Complaint should be  in 'drop'.")

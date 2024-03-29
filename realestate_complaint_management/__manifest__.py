# -*- coding: utf-8 -*-
{
    'name': "RealEstateX_Complaint_Management",

    'summary': """
        RealEstateX complaint Management System""",

    'description': """
        RealEstateX wants to provide a form on their website for
tenants to submit complaints about their rented flats. These complaints will then be classified
and dealt with by RealEstateX’s employees.
    """,

    'author': "Sify Karippery Raphy",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','website','l10n_din5008'],

    # always loaded
    'data': [
        'security/security_data.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/email_template.xml',
        'data/complaint_type_data.xml',
        'report/realestate_complaint_report.xml',
        'views/complaint_management_views.xml',
        'views/complaint_website_form_templates.xml',

    ],
    # only loaded in demonstration mode
'license': 'LGPL-3',
}



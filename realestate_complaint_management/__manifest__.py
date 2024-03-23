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

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security_data.xml',
        'data/sequence.xml',
        'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

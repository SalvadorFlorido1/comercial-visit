# -*- coding: utf-8 -*-
{
    'name': "all_custom_crm",

    'summary': """
        CRM addon for comercial visits control
        """,

    'description': """With this module you could track all visit of your sales agents
    """,

    'author': "Salvador Florido",
    'website': "https://www.alliantum.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
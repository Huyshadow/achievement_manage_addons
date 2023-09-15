# -*- coding: utf-8 -*-
{
    'name': "Quản lý danh hiệu SV5T",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'license': 'LGPL-3',

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Themes/Backend",
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
        'views/info.xml',
        'views/Department_Manage_View/department_view.xml',
        'views/User_Manage_View/user_view.xml',
        'data/achivement.xml',
        'data/auditor.xml',
        'data/department.xml',
        'data/contact_info.xml',
        'data/result.xml',
        'data/user.xml',
        'data/criteria.xml',
        'data/submission.xml',
        'data/closure_criteria.xml',
        'data/result_of_criteria.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'demo/user_demo.xml',
        'demo/department_demo.xml',
    ],
}

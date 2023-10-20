# -*- coding: utf-8 -*-
{
    'name': "Thống kê",

    'summary': """
        Thống kê danh hiệu giải thưởng""",

    'description': """
        Long description of module's purpose
    """,

    'author': "HKT",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'view_submit'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/graph_kanban_view_ach.xml',
        'views/graph_tree_view_ach.xml',
        'views/menu.xml',


    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}

# -*- coding: utf-8 -*-
{
    'name': "Create Achievement",

    'summary': """
        Feature: Creating achievement of the Website
    """,

    'description': """
        No comment
    """,
    'license': 'LGPL-3',

    'author': "HKT Team",
    'website': "https://www.facebook.com/profile.php?id=100074736126982",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'access_right_user', 'manage_user_depart'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/achievement.xml',
        'views/criteria.xml',
        'views/group_criteria.xml',
        'views/type_criteria.xml',
        'views/menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'create_achievement/static/src/styles/achievement.scss',
            'create_achievement/static/src/js/trace_back.js'
        ],
        'web.assets_frontend': [
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

# -*- coding: utf-8 -*-
{
    'name': "View Submit",

    'summary': """
        Feature: Manager view submit
    """,

    'author': "TusDT",
    'license': 'LGPL-3',
    'website': "https://www.facebook.com/clone.lol9/",
    'category': 'HKT addons',
    'version': '0.1',
    'depends': ['base', 'user_view_achievement', 'web_list_view_general_buttons', 'manage_user_depart'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/view_achievement.xml',
        'views/view_list_user_submit.xml',
        'views/view_detail_user_submit.xml',
        'views/menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'view_submit/static/src/js/title_button.js',
            'view_submit/static/src/js/redefine_achievement.js'
        ],
    },

}

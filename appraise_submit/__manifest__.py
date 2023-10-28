# -*- coding: utf-8 -*-
{
    'name': "Appraise Submit",

    'summary': """
        Feature: Comitte view submit
    """,

    'author': "TusDT",
    'license': 'LGPL-3',
    'website': "https://www.facebook.com/clone.lol9/",
    'category': 'HKT addons',
    'version': '0.1',
    'depends': ['base', 'user_view_achievement', 'manage_user_depart'],

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
            'appraise_submit/static/src/scss/form_appraise.scss',
            'appraise_submit/static/src/js/add_stt.js',
        ],
    },

}

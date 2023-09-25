# -*- coding: utf-8 -*-
{
    'name': "User Achievement",

    'summary': """
        Feature: User view list Achievement
    """,

    'author': "TusDT",
    'website': "https://www.facebook.com/clone.lol9/",
    'license': 'LGPL-3',
    'category': 'HKT addons',
    'version': '0.1',
    'depends': ['base', 'create_achievement'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/user_view_achievement_detail.xml',
        'views/user_view_achievement.xml',
        'views/achievement_submit_view.xml',
        'views/menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'user_view_achievement/static/src/js/**/*',
            'user_view_achievement/static/src/xml/**/*',
            'user_view_achievement/static/src/scss/**/*.scss',
        ],
    },

}

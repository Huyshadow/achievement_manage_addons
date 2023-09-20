# -*- coding: utf-8 -*-
{
    'name': "User Achievement",

    'summary': """
        Feature: User view list Achievement
    """,

    'author': "TusDT",
    'website': "https://www.facebook.com/clone.lol9/",
    'category': 'HKT addons',
    'version': '0.1',
    'depends': ['base', 'manage_user_depart'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'security/security.xml',
        'views/user_view.xml',
        'views/menus.xml',  
    ],
    'assets': {
        'web.assets_backend': [
            # # 'user_view_achievement/static/src/js/**/*',
            # 'user_view_achievement/static/src/xml/**/*',
            # 'user_view_achievement/static/src/scss/**/*.scss',
        ],
    },
    
}

# -*- coding: utf-8 -*-
{
    'name': "Login Theme",

    'summary': """
        Smart login page for odoo v16""",

    'description': """
        Animated login page by Odoo Glow
    """,

    'author': "Odoo Glow",
    'website': "https://www.yourcompany.com",
    'category': 'Themes/Backend',
    'version': '0.1',
    'depends': ['base','web','website'],
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
        ],
        'web.assets_frontend': [
            'og_login_page/static/src/css/login.css',
        ],
        'web.assets_common': [
        ],
    },
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['images/main_screenshot.png','images/main_1.png','images/main_2.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'OPL-1',
    'contributors': [
        'Odoo Glow',
    ],
}

# ©  2018 Terrabit
# See README.rst file on addons root folder for license details

# {
#     "name": "List View General Buttons",
#     "summary": "General Buttons in List View ",
#     "version": "13.0.1.0.0",
#     "author": "Terrabit, Odoo Community Association (OCA)",
#     "website": "https://www.terrabit.ro",
#     "category": "Generic Modules",
#     "depends": ["base", "web"],
#     "data": ["views/assets.xml"],
#     "qweb": ["static/src/xml/*.xml"],
#     "development_status": "Mature",
#     "maintainers": ["dhongu"],
# }
# # -*- coding: utf-8 -*-
{
    'name': "List View General Buttons",

    'summary': """
        General Buttons in List View
    """,

    'author': "Huy_Khang_Tu",
    'license': 'LGPL-3',
    'website': "https://www.facebook.com/clone.lol9/",
    'category': 'HKT addons',
    'version': '0.1',
    'depends': ['base', "web"],
    "qweb": ["static/src/xml/*.xml"],
    # always loaded
    'data': [
    ],
    'assets': {
        'web.assets_backend': [
            'web_list_view_general_buttons/static/src/xml/web_list_view_template.xml',
            'web_list_view_general_buttons/static/src/js/list_controller.js',
        ],
    },

}

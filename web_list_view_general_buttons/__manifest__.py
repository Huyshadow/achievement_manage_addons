# -*- coding: utf-8 -*-
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
    # always loaded
    'data': [
    ],
    'assets': {
        'web.assets_backend': [
            'web_list_view_general_buttons/static/src/xml/web_list_view_template.xml',
            'web_list_view_general_buttons/static/src/xml/web_list_button_graph.xml',
            'web_list_view_general_buttons/static/src/js/list_controller.js',
            'web_list_view_general_buttons/static/src/js/graph_button.js'
            'web_list_view_general_buttons/static/src/xml/web_list_view_discard_template.xml',
            'web_list_view_general_buttons/static/src/js/list_morebutton.js',
            'web_list_view_general_buttons/static/src/js/check_button_appear.js',
        ],
    },

}

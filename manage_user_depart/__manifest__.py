# -*- coding: utf-8 -*-
{
    'name': "Quản lý đơn vị",

    'summary': """
        Module cho phép xem danh sách các user và các đơn vị""",

    'description': """
        Long description of module's purpose
    """,
    'license': 'LGPL-3',

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Themes/Backend",
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'access_right_user'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/department_sequence.xml',
        'views/Department_Manage_View/department_view.xml',
        'views/User_Manage_View/user_view.xml',
        'views/User_Manage_View/user_view_by_unit.xml',
        'views/message_dialog.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'manage_user_depart/static/src/scss/heightbox.scss',
            'manage_user_depart/static/src/scss/dialog.scss',
        ],
        # 'web.assets_frontend': [
        #     'manage_user_depart/static/src/scss/heightbox.scss'
        # ],
    },

}

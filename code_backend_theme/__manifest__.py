# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2021-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    "name": "ĐHQG Theme",
    "description": """Minimalist and elegant backend theme for Odoo 16, Backend Theme, Theme""",
    "summary": "Code Backend Theme V16 is an attractive theme for backend",
    "category": "Themes/Backend",
    "version": "16.0.1.0.2",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    "depends": ['base', 'web', 'mail','web_window_title'],
    "data": [
        'views/layout.xml',
        'views/icons.xml',
        'views/replace_login.xml',
        'views/menu_empty.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'code_backend_theme/static/src/xml/styles.xml',
            'code_backend_theme/static/src/xml/custom_error_dialog.xml', #### Comment dòng code này nếu muốn đọc roll back error #######
            'code_backend_theme/static/src/xml/top_bar.xml',
            'code_backend_theme/static/src/scss/theme_accent.scss',
            'code_backend_theme/static/src/scss/navigation_bar.scss',
            'code_backend_theme/static/src/scss/datetimepicker.scss',
            'code_backend_theme/static/src/scss/theme.scss',
            'code_backend_theme/static/src/scss/form.scss',
            'code_backend_theme/static/src/scss/kanban.scss',
            'code_backend_theme/static/src/scss/sidebar.scss',
            'code_backend_theme/static/src/js/chrome/sidebar_menu.js',
            'code_backend_theme/static/src/js/fields/colors.js',
            'code_backend_theme/static/src/js/fields/input.js',

        ],
        'web.assets_frontend': [
            'code_backend_theme/static/src/scss/login.scss',
            'code_backend_theme/static/src/js/fields/input.js',

        ],
    },
    'images': [
        'static/description/banner.png',
        'static/description/theme_screenshot.png',
    ],
    'license': 'LGPL-3',
    'pre_init_hook': 'test_pre_init_hook',
    'post_init_hook': 'test_post_init_hook',
    'installable': True,
    'application': False,
    'auto_install': False,
}

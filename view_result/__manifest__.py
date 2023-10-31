# -*- coding: utf-8 -*-
{
    'name': "view_result",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "HKT",
    'website': "https://www.facebook.com/profile.php?id=100074736126982",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'appraise_submit'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/view_achievement_result.xml',
        'views/view_user_list_result.xml',
        'views/view_user_detail_result.xml',

    ],
}

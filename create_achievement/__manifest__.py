# -*- coding: utf-8 -*-
{
<<<<<<< HEAD
    'name': "Create Achievement",

    'summary': """
        Feature: Creating achievement of the Website
    """,

    'description': """
        No comment
    """,

    'author': "My Company",
    'website': "https://www.facebook.com/profile.php?id=100074736126982",
=======
    'name': "create_achievement",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",
>>>>>>> 62ccb99 (Skeleton of Create Achievement)

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
<<<<<<< HEAD
        'security/ir.model.access.csv',
        'data/ir_cron.xml',
        'data/achievement.xml',
        'data/criteria.xml',
        'views/achievement.xml',
        'views/menu.xml',
        'views/criteria.xml'

=======
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
>>>>>>> 62ccb99 (Skeleton of Create Achievement)
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

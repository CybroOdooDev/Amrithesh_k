# -*- coding: utf-8 -*-

{
    'name': 'Run Query',
    'version': '1.0',
    'summary': 'Run Query',
    'sequence': -1,
    'description': """Run Query""",
    'category': 'Tools',
    'depends': ['base', 'sale_management','sale', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/run_query_views.xml',
    ],
    'installable': True,
    'application': True,
}

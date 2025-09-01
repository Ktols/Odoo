{
    'name': 'Demo Insecure',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Demo: credencial expuesta en DOM',
    'license': 'LGPL-3',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/demo_insecure_views.xml',
        'views/demo_insecure_menu.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': False,
}
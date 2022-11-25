# -*- encoding: utf-8 -*-
{
    'name': 'Home Finances',
    'version': 'A0.2',
    'category': 'Finanzas',
    'summary': """
        Gestiona todas tus finanzas personales en un solo modulo!
    """,
    'author': 'Axel Von',
    'website': 'notenemospaginatodavia.com',
    'depends': ['base'],
    'data': [
            'security/op_security.xml',
            'security/ir.model.access.csv',
            'views/register/A0_base.xml',
            'views/menus.xml',
            ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'images': ['static/description/banner.png'],
}

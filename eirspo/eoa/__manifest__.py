# -*- coding: utf-8 -*-
{
    'name': "eoa",
    'version': '0.8.0',
    'category': 'eoa',
    'summary': 'This module was built to manager and monitor eoa modules.',
    'description': 'base module of eoa',

    'author': "Eirspo Tech",
    'website': "http://www.eirspo.com",

    'depends': ['base'],
    'data': [
        'views/eoa_views.xml',
        'views/eoa_templates.xml',
        'views/eoa_menus.xml'
    ],

    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'qweb': [
        'static/src/xml/website.backend.xml'
    ]
}
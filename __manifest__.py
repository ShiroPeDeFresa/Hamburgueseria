# -*- coding: utf-8 -*-
{
	 'name': "hamburgueseria",
    'summary': """Aplicacion Hamburgueseria""",
    'description': """
        Gestion de la hamburgueseria:
    """,
    'author': "unknown",
    'website': "http://www.salesuanos.edu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Hamburgueseria',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views.xml',
	# 'vistas/matches.xml',
	# 'vistas/maps.xml',
	# 'vistas/characters.xml',
    ],
}

# -*- coding: utf-8 -*-

{
    'name': 'My Employee',
    'summary': 'Manager my employee',
    'version': '10.0.1.0.0',
    'author': 'team5',
    'category': 'Manager Employee Application',
    'license': 'AGPL-3',
    'website': 'http://www.domain.com',
    'sequence': 1,
    'depends': ['base','hr'],
    'data': [
        'views/templates.xml',
        'views/views.xml',
        'views/educate.xml',
        'views/employee.xml',
        'views/Extracurricular.xml',
        'views/requirement_educate.xml',
        'views/classlist.xml',
        'views/autoID.xml',
        #'views/book_loan.xml',
        'views/menu.xml'

    ],
    'demo': [
        # 'demo/demo.xml',
    ],
    'css': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'description': """
		Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do 
		eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut 
		enim ad minim veniam, quis nostrud exercitation ullamco laboris
		nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor 
		in reprehenderit in voluptate velit esse cillum dolore eu fugiat
		nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
		sunt in culpa qui officia deserunt mollit anim id est laborum.
	""",
}



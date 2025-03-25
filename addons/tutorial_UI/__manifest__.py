# -*- coding: utf-8 -*-
{
    'name': 'Tutorial UI',
    'version': '1.0',
    'category': 'Tutorial',
    'sequence': 5,
    'summary': 'Module này dành cho người mới học Odoo, giúp tạo module từ đầu.',
    'description': """ 
        Đây là một module hướng dẫn cơ bản trong Odoo, bao gồm các bước khởi tạo, 
        định nghĩa giao diện và sử dụng snippets trong website.
    """,
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'depends': ['base', 'website'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'data': [
        'views/block.xml',
        'views/snippets.xml',
    ],
    'license': 'LGPL-3',
}

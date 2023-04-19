{
    'name': 'Exams Ranking System',
    'version': '1.0',
    'author': 'Your Name',
    'website': 'https://www.example.com',
    'summary': 'A module to manage exam results and rankings',
    'description': 'This module allows users to create exams, add students, enter scores, and rank students based on their exam results.',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'views/exam_views.xml',
        'views/student_views.xml',
        'views/exam_result_views.xml',
        'security/exam_security.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}


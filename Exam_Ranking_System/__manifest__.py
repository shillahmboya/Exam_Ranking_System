
{    
'name': 'Exam Ranking System',
    'version': '1.0',
    'author': 'Shillah',
    'website': 'https://www.examr.com',
    'summary': 'A module to manage exam results and rankings',
    'description': 'This module allows users to create exams, add students, enter scores, and rank students based on their exam results.',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'views/Exam.xml',
        'views/Student.xml',
        'views/ER.xml',
        #'security/exam_security.xml',
        #'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    
}
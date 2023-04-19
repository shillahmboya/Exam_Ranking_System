from odoo import models
from odoo import fields
class Student(models.Model):
    _name = 'Exam_Ranking_System.student'
    _description = 'Student'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    email = fields.Char(string='Email', required=True)
    exam_result_ids = fields.One2many('Exam_Ranking_System.examresult', 'student_id', string='Exam Results')

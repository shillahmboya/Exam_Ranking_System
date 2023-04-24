from odoo import models
from odoo import fields
class StudentD(models.Model):
    _name = 'student.d'
    _description = 'Student'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    email = fields.Char(string='Email', required=True)
    exam_result_ids = fields.One2many('exam.result', 'student_id', string='Exam Results')

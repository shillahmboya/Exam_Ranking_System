from . import models,fields
class Student(models.Model):
    _name = 'Exams_Ranking_System.student'
    _description = 'Student'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    email = fields.Char(string='Email', required=True)
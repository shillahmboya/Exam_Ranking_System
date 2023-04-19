
from . import models,fields
class Exam(models.Model):
    _name = 'Exam_Ranking_System.exam'
    _description = 'Exam'

    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Date')
    total_marks = fields.Integer(string='Total Marks')

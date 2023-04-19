
from odoo import models
from odoo import fields
class Exam(models.Model):
    _name = 'Exam_Ranking_System.exam'
    _description = 'Exam'

    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Date')
    total_marks = fields.Integer(string='Total Marks')
    exam_result_ids = fields.One2many('Exam_Ranking_System.examresult', 'exam_id', string='Exam Results')

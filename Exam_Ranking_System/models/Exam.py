from odoo import models
from odoo import fields
from odoo import api
class ExamMM(models.Model):
    _name = 'exam.mm'
    _description = 'Exam'

    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Date')
    total_marks = fields.Integer(string='Total Marks')
    #exam_result_ids = fields.One2many('Exam_Ranking_System.examresult', 'exam_id', string='Exam Results')

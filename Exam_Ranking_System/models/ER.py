from odoo import models
from odoo import fields
class ExamResult(models.Model):
    _name = 'exam.result'
    _description = 'Exam Result'

    #studentid = fields.Many2one('student.d', string='Student', required=True)
    #exam_id = fields.Many2one('exam.mm', string='Exam', required=True)
    marks_obtained = fields.Integer(string='Marks Obtained')

from . import models,fields
class ExamResult(models.Model):
    _name = 'Exam_Ranking_System.examresult'
    _description = 'Exam Result'

    student_id = fields.Many2one('Exam_Ranking_System.student', string='Student', required=True)
    exam_id = fields.Many2one('Exam_Ranking_System.exam', string='Exam', required=True)
    marks_obtained = fields.Integer(string='Marks Obtained')
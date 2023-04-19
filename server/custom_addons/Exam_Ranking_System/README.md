Exam Ranking System Module for Odoo
------------------------------------
This module allows you to manage exams, students, and their results in Odoo. With this module, you can create exams, add students, enter their scores, and rank them based on their exam results.

Installation
----------------
Clone this repository to your Odoo addons folder:

git clone  https://github.com/shillahmboya/Exam_Ranking_System.git

Restart your Odoo server.

Log in to your Odoo instance and go to the Apps menu.

In the search bar, search for Exams Ranking System and click Install.

Usage
-------------------
Once the module is installed, go to the Exams menu to create a new exam.

In the Exam form, enter the exam name, date, and total marks.

Go to the Students menu to add students to the system.

In the Student form, enter the student's first name, last name, and email.

After adding students, go back to the Exam form and select the students who will be taking the exam.

Save the Exam form to create Exam Results records for each student.

In the Exam form, click the Results tab to see the list of Exam Results.

To enter scores for each student, click the Edit button beside the Exam Result record.

In the Exam Result form, enter the marks obtained by the student and click Save.

To view the ranking of students based on their exam results, go to the Exam form and click the Ranking button.

In the Ranking view, you can filter and sort the data to view the rankings based on different criteria.

Security
------------
This module includes the following access controls:

Manager: Full access to all features and data.
User: Access to all features and data, except the ability to create, edit, or delete Exams and Students.
Public: No access to any features or data.
To create additional roles or modify the existing ones, go to the Settings menu and select Security > Access Controls > Rules.






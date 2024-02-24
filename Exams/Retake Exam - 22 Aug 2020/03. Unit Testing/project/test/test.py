from unittest import TestCase, main
from project.student_report_card import StudentReportCard


class StudentReportCardTest(TestCase):
    def setUp(self) -> None:
        self.report = StudentReportCard('Pen4o', 3)

    def test_constructor(self):
        name = self.report.student_name
        year = self.report.school_year

        self.assertEqual((name, year), ('Pen4o', 3))
        self.assertEqual(self.report.grades_by_subject, {})

    def test_student_name_empty_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.report.student_name = ''

        self.assertEqual(str(ve.exception), "Student Name cannot be an empty string!")

    def test_school_year_invalid_ve(self):
        invalid_year = 0

        with self.assertRaises(ValueError) as ve:
            self.report.school_year = invalid_year

        self.assertEqual(str(ve.exception), "School Year must be between 1 and 12!")

    def test_school_year_invalid2_ve(self):
        invalid_year = 13

        with self.assertRaises(ValueError) as ve:
            self.report.school_year = invalid_year

        self.assertEqual(str(ve.exception), "School Year must be between 1 and 12!")

    def test_successful_year(self):
        self.report.school_year = 1

        self.assertEqual(1, self.report.school_year)

    def test_successful_year_1(self):
        self.report.school_year = 12

        self.assertEqual(12, self.report.school_year)

    def test_add_grade_subject_not_in_list(self):
        self.report.grades_by_subject = {'Muzika': [3.20]}
        subject = 'Himiq'
        grade = 3.5

        self.report.add_grade(subject, grade)

        res = self.report.grades_by_subject
        exp_res = {'Muzika': [3.20], 'Himiq': [3.5]}

        self.assertEqual(res, exp_res)

    def test_add_grade_subject_in_list(self):
        self.report.grades_by_subject = {'Himiq': [3.5], 'Muzika': [3.20]}
        subject = 'Himiq'
        grade = 4.1

        self.report.add_grade(subject, grade)

        res = self.report.grades_by_subject
        exp_res = {'Himiq': [3.5, 4.1], 'Muzika': [3.20]}

        self.assertEqual(res, exp_res)

    def test_average_grade_by_subject(self):
        self.report.grades_by_subject = {'Himiq': [3.5, 4.1], 'Muzika': [6, 3.44]}

        message = self.report.average_grade_by_subject()

        exp_res = f"Himiq: 3.80" \
                  f"\nMuzika: 4.72"

        self.assertEqual(message, exp_res)

    def test_average_grade_for_all_subjects(self):
        self.report.grades_by_subject = {'Himiq': [3.5, 4.1], 'Muzika': [6, 3.44]}

        message = self.report.average_grade_for_all_subjects()
        exp_res = f"Average Grade: 4.26"

        self.assertEqual(message, exp_res)

    def test_repr_override(self):
        self.report.grades_by_subject = {'Himiq': [3.5, 4.1], 'Muzika': [6, 3.44]}

        res = str(self.report)
        exp_res = f"Name: Pen4o\n" \
                  f"Year: 3\n" \
                  f"----------\n" \
                  f"Himiq: 3.80\n" \
                  f"Muzika: 4.72\n" \
                  f"----------\n" \
                  f"Average Grade: 4.26"


        self.assertEqual(res, exp_res)


if __name__ == '__main__':
    main()
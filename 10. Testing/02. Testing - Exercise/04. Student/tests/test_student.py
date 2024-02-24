from unittest import TestCase, main
from project.student import Student


class StudentTest(TestCase):
    def setUp(self) -> None:
        self.student = Student('Pesho')

    def test_constructor(self):
        name = self.student.name
        courses = self.student.courses

        self.assertEqual(name, 'Pesho')
        self.assertEqual(courses, {})

        new_courses = {'OOP': ['note 1'],
                       'JAVA': ['note 2']
                       }

        self.student.courses = new_courses
        self.assertEqual(self.student.courses, {'OOP': ['note 1'], 'JAVA': ['note 2']})

    def test_enroll_course_already_added(self):
        self.student.courses = {'OOP': ['note 1'], 'JAVA': ['note 2']}
        course = 'OOP'
        notes = ['note 33']
        message = self.student.enroll(course, notes)

        res = self.student.courses[course]

        self.assertEqual(res, ['note 1', 'note 33'])
        self.assertEqual(message, "Course already added. Notes have been updated.")

    def test_enroll_add_course_notes(self):
        course = 'OOP'
        notes = ['note 22']
        message = self.student.enroll(course, notes, "Y")

        res = self.student.courses
        exp_res = {'OOP': ['note 22']}

        self.assertEqual(res, exp_res)
        self.assertEqual(message, "Course and course notes have been added.")

    def test_enroll_add_course_no_add_course_string(self):
        course = 'OOP'
        notes = ['note 22']

        message = self.student.enroll(course, notes)

        res = self.student.courses
        exp_res = {'OOP': ['note 22']}

        self.assertEqual(res, exp_res)
        self.assertEqual(message, "Course and course notes have been added.")

    def test_enroll_add_course_no_notes(self):
        course = 'OOP'
        notes = ['note 22']

        message = self.student.enroll(course, notes, 'N')

        res = self.student.courses[course]
        exp_res = []

        self.assertEqual(res, exp_res)
        self.assertEqual(message, "Course has been added.")

    def test_add_notes_no_course_raise_exc(self):
        notes = ['123']
        fake_course = 'MATHS'
        with self.assertRaises(Exception) as ex:
            self.student.add_notes(fake_course, notes)

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

        course = 'OOP'
        notes = ['old notes']
        new_notes = 'new notes'
        self.student.courses[course] = notes

        message = self.student.add_notes(course, new_notes)

        res = self.student.courses[course]
        exp_res = ['old notes', 'new notes']

        self.assertEqual(res, exp_res)
        self.assertEqual(message, "Notes have been updated")

    def test_leave_course_no_course_raise_exc(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('BZ')

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

        self.student.courses = {'OOP': ['note 1'],
                                'JAVA': ['note 2']}

        self.student.leave_course('OOP')

        res = self.student.courses
        exp_res = {'JAVA': ['note 2']}

        self.assertEqual(res, exp_res)


if __name__ == '__main__':
    main()

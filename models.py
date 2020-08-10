from django.db import models


class Course(models.Model):
    subject_code = models.CharField(max_length=4)
    course_number = models.CharField(max_length=4)
    course_code = models.CharField(max_length=8)
    course_title = models.CharField(max_length=150)
    course_name = models.CharField(max_length=150)
    course_description = models.CharField(max_length=600)
    department = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    course_level = models.CharField(max_length=20)

    class Meta:
        db_table = 'courses'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class CourseReview(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='+',)
    title = models.CharField(max_length=100)
    body = models.TextField
    pub_date = models.DateTimeField('date published')
    helpful = models.IntegerField(default=0)
    not_helpful = models.IntegerField(default=0)

    class Meta:
        db_table = 'coursereviews'
        verbose_name = 'Course Review'
        verbose_name_plural = 'Course Reviews'


class Department(models.Model):
    department_id = models.CharField(max_length=10)
    department_name = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='+',)
    faculty_id = models.CharField(max_length=10)

    class Meta:
        db_table = 'departments'
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class Faculty(models.Model):
    faculty_id = models.CharField(max_length=10)
    faculty_name = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='+',)
    departments = models.CharField(max_length=100)

    class Meta:
        db_table = 'faculty'
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'


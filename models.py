from django.db import models


class Course(models.Model):
    subject_code = models.CharField(max_length=4)
    course_number = models.charField(maxlength=4)
    course_code = subject_code + course_number
    course_title = models.CharField
    course_description = models.CharField
    department = models.CharField
    faculty = models.CharField
    course_level = models.CharField
    reviews_count = models.IntegerField
    one_star_count =
    two_star_count =
    three_star_count =
    four_star_count =
    five_star_count =
    overall_rating = models.Flo
    difficulty_count =
    interest_rating =
    interest_count =
    workload_rating =
    workload_count = 
    keywords = 

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

class Review(models.Model):
    title = 
    body = 


class Department(models.Model):
    department_id
    department_name
    faculty_id

class Faculty(models.Model):
    faculty_id
    faculty_name
    departments

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
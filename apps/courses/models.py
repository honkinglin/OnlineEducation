from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='Course Name')
    desc = models.CharField(max_length=300, verbose_name='Course Description')
    detail = models.TextField(verbose_name='Course Details')
    degree = models.CharField(choices=(('primary', 'Primary'), ('middle', 'Middle'), ('high', 'High')), max_length=10)
    learn_times = models.IntegerField(default=0, verbose_name='Learning Time (minutes)')
    students = models.IntegerField(default=0, verbose_name='Number of Students')
    fav_nums = models.IntegerField(default=0, verbose_name='Number of Favorites')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='Cover Image', max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name='Number of Clicks')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = verbose_name
        db_table = 'Course'

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Course')
    name = models.CharField(max_length=100, verbose_name='Lesson Name')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = verbose_name
        db_table = 'Lesson'

    def __str__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Lesson')
    name = models.CharField(max_length=100, verbose_name='Video Name')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = verbose_name
        db_table = 'Video'

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Course')
    name = models.CharField(max_length=100, verbose_name='Resource Name')
    download = models.FileField(upload_to='course/resource/%Y/%m', verbose_name='Download Link', max_length=100)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Creation Time')

    class Meta:
        verbose_name = 'Course Resource'
        verbose_name_plural = verbose_name
        db_table = 'CourseResource'

    def __str__(self):
        return self.name

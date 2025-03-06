from django.db import models
from django.utils.safestring import mark_safe


# 学生表
class Students(models.Model):
    id = models.AutoField(verbose_name="编号", primary_key=True)
    name = models.CharField(verbose_name="姓名", max_length=22, default='')
    password = models.CharField(verbose_name="密码", max_length=32, default='')
    phone = models.CharField(verbose_name="手机号", max_length=11, default='')
    email = models.CharField(verbose_name="邮箱", max_length=22, default='')
    time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    photo = models.FileField(verbose_name="头像", default='', upload_to="Students/photo/")
    # integral = models.IntegerField(verbose_name="积分", default=100)
    is_active = models.BooleanField(verbose_name="活跃状态", default=True)

    def admin_sample(self):
        return mark_safe('<img src="/media/%s" height="60" width="60" />' % (self.photo,))

    admin_sample.short_description = '  学生图片'
    admin_sample.allow_tags = True

    def __str__(self):
        return self.name

    class Meta:
        # 数据库列表名
        db_table = 'Students'
        # 后台管理名
        verbose_name_plural = '学生管理'

    # def viewed(self):
    #     """
    #     增加阅读数
    #     :return:
    #     """
    #     self.traffic += 1
    #     self.save(update_fields=['traffic'])


# 自习室
class Rooms(models.Model):
    id = models.AutoField(verbose_name="编号", primary_key=True)
    name = models.CharField(verbose_name="名称", max_length=22, default='')
    number = models.IntegerField(verbose_name="座位数量", default=0)
    photo = models.FileField(verbose_name="头像", default='', upload_to="Room/photo/")
    time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    is_active = models.BooleanField(verbose_name="活跃状态", default=True)

    def admin_sample(self):
        return mark_safe('<img src="/media/%s" height="60" width="60" />' % (self.photo,))

    admin_sample.short_description = '  学生图片'
    admin_sample.allow_tags = True

    def __str__(self):
        return self.name

    class Meta:
        # 数据库列表名
        db_table = 'Room'
        # 后台管理名
        verbose_name_plural = '自习室管理'


# 预约管理
class Bookings(models.Model):
    id = models.AutoField(verbose_name="编号", primary_key=True)
    students = models.ForeignKey(verbose_name="学生", to='Students', null=True, on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name="预约座位号", default=0)
    room = models.ForeignKey(verbose_name="自习室", to='Rooms', on_delete=models.CASCADE, null=True)
    # 1.上午 2.下午 3.晚自习
    time_choice = (
        (1, '上午'),
        (2, '下午'),
        (3, '晚自习'),
    )
    is_choice = (
        (1, "预约"),
        (2, "已签到"),
        (3, "未签到"),
        (4, "已取消")
    )
    period = models.IntegerField(verbose_name="时间", choices=time_choice, default=1)
    time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    is_active = models.IntegerField(verbose_name="活跃状态", choices=is_choice, default=1)

    def __str__(self):
        return self.students.name

    class Meta:
        # 数据库列表名
        db_table = 'Booking'
        # 后台管理名
        verbose_name_plural = '预约管理'

    def admin_sample(self):
        return mark_safe('<img src="/media/%s" height="60" width="60" />' % (self.students.photo,))

    admin_sample.short_description = '  学生图片'
    admin_sample.allow_tags = True


# 警告管理
class Integrals(models.Model):
    id = models.AutoField(verbose_name="编号", primary_key=True)
    student = models.ForeignKey(verbose_name="学生", to='Students', on_delete=models.CASCADE)
    # integral = models.IntegerField(verbose_name="扣积分", default=0)
    title = models.CharField(verbose_name="警告题目", max_length=220, default='')
    text = models.TextField(verbose_name="警告内容内容", max_length=220, default='')
    time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    is_active = models.BooleanField(verbose_name="活跃状态", default=True)

    def __str__(self):
        return self.student.name

    class Meta:
        # 数据库列表名
        db_table = 'Integral'
        # 后台管理名
        verbose_name_plural = '扣积分管理'

    def admin_sample(self):
        return mark_safe('<img src="/media/%s" height="60" width="60" />' % (self.student.photo,))

    admin_sample.short_description = '  学生图片'
    admin_sample.allow_tags = True


# 提示管理
class Text(models.Model):
    id = models.AutoField(verbose_name="编号", primary_key=True)
    title = models.CharField(verbose_name="题目", max_length=120, default='')
    text = models.TextField(verbose_name="内容", default='')
    time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    is_active = models.BooleanField(verbose_name="活跃状态", default=True)

    def __str__(self):
        return self.text

    class Meta:
        # 数据库列表名
        db_table = 'Text'
        # 后台管理名
        verbose_name_plural = '提示管理'


# 签到码
class SignCode(models.Model):
    id = models.AutoField(verbose_name="编号", primary_key=True)
    text = models.TextField(verbose_name="内容", default='')
    time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    is_active = models.BooleanField(verbose_name="活跃状态", default=True)

    def __str__(self):
        return self.text

    class Meta:
        # 数据库列表名
        db_table = 'sign_code'
        # 后台管理名
        verbose_name_plural = '签到码'


def __str__(self):
    return self.admin_sample

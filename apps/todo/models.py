from django.db import models
from apps.authenticated.models import User


class ToDoList(models.Model):
    name = models.CharField(verbose_name="نام")
    for_user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربر سازنده")
    create_list_date = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ایجاد لیست")

    class Meta:
        verbose_name = 'ToDoList'
        verbose_name_plural = 'ToDoLists'

    def __str__(self):
        self.name


class Todo(models.Model):
    for_list = models.ForeignKey(ToDoList,on_delete=models.CASCADE)
    title = models.CharField(max_length=110,verbose_name="موضوع")
    description = models.TextField(verbose_name="توضیحات",blank=True,null=True)
    start_date = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ شروع")
    end_date = models.DateTimeField(verbose_name="تاریخ پایین")
    public = models.BooleanField(verbose_name="عمومی",default=False,help_text="اگر شما این گزینه را انتخاب کنید بقیه به این کار دسترسی دارند")   
    @property
    def todo_type(self):
        return "عمومی" if self.public == True else "شخصی"
    
    
    class Meta:
        verbose_name = "کار"
        verbose_name_plural = "کار ها"
        
    def __str__(self):
        return self.title
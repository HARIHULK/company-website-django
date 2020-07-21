from django.db import models

# Create your models here.
class EmployeeRegister(models.Model):
    #genvalues=[('Male','Male'),('Female','Female'),('other','other')]
    #depvalues=[('Technical','Technical'),('Non-Technical','Non-Technical')]
    Emp_Firstname=models.CharField(max_length=50)
    Emp_Lastname=models.CharField(max_length=50)
    Emp_Age=models.IntegerField()
    Emp_Id=models.CharField(max_length=50)
    Emp_Gender=models.CharField(max_length=10)
    Emp_Email=models.EmailField(max_length=50)
    Emp_Password=models.CharField(max_length=30)
    Emp_Salary=models.FloatField(null=False)
    Emp_Department=models.CharField(max_length=30)
    Emp_phoneno=models.CharField(max_length=10)

    


    def __str__(self):
        return self.Emp_Firstname+" "+self.Emp_Lastname+"  "+self.Emp_Email
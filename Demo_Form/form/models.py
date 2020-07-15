from django.db import models

# Create your models here

class MyUser(models.Model):
    image = models.ImageField(upload_to='profile_pics',blank=True)
    Full_name = models.CharField(max_length=256)
    GENDER = (('M','Male'),('F','Female'),('O','Other'))
    gender = models.CharField(max_length=1, choices=GENDER, null=True)
    Phone_Number = models.CharField(max_length=12,unique=True)
    Email = models.EmailField(max_length=264,unique=True)
    Country = models.CharField(max_length=264)
    State = models.CharField(max_length=264)
    City = models.CharField(max_length=264)
    Address = models.CharField(max_length=2048)
    MEMBERS = [
    ('2100','2100 Rs Lifetime Membership'),
    ('21000','21000 Rs Lifetime Patron Membership'),
    ('100000','1Lakh Rs S.A.F Trustee'),
    ('1100000','11Lakh Rs S.A.F Patron Trustee'),
    ('5100000','51Lakh Rs S.A.F Board of Trustee'),
    ]
    Membership = models.CharField(max_length=6,choices=MEMBERS, null=True)
    CAREERS = [
    ('BI','Business & Industry'),
    ('JL','Judicial & Legal Services'),
    ('BP','Bureaucrats & Public Servant'),
    ('DP','Defence, Police & Paramilitary Forces'),
    ('NC','NCC Cadets'),
    ('VJ','VIPR Jan(Pujari/Brahmins)'),
    ('PR','Public Representatives'),
    ('NF','Nandanaar Families'),
    ('SO','Social Organisations'),
    ('DO','Doctors'),
    ('YO','Youths'),
    ('OT','Others'),
    ]
    Career = models.CharField(max_length=264,choices=CAREERS,null=True)

    def __str__(self):
        return str(self.Full_name)

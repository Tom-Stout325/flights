from django.db import models
from django.contrib.auth.models import User


class Drones(models.Model):
    model = models.CharField(max_length=200, null=True, blank=True)
    serial = models.CharField(max_length=50, null=True, blank=True)
    registration = models.CharField(max_length=50, null=True, blank=True)
    reg_exp = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    user = models.ManyToManyField('Profiles')

    def __str__(self):
        return str(self.model)

    class Meta:
        verbose_name_plural = "Drones"


class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/', default="user-default.png")
    license = models.CharField(max_length=200, blank=True, null=True)
    license_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "Profiles"
        ordering = ['user']


class Flights(models.Model):

    STATE_CODES = (
        ('Alabama', 'AL'),
        ('Alaska', 'AK'),
        ('Arizona', 'AZ'),
        ('Arkansas', 'AR'),
        ('California', 'CA'),
        ('Colorado', 'CO'),
        ('Connecticut', 'CT'),
        ('Delaware', 'DE'),
        ('Florida', 'FL'),
        ('Georgia', 'GA'),
        ('Hawaii', 'HI'),
        ('Idaho', 'ID'),
        ('Illinois', 'IL'),
        ('Indiana', 'IN'),
        ('Iowa', 'IA'),
        ('Kansas', 'KS'),
        ('Kentucky', 'KY'),
        ('Louisiana', 'LA'),
        ('Maine', 'ME'),
        ('Maryland', 'MD'),
        ('Massachusetts', 'MA'),
        ('Michigan', 'MI'),
        ('Minnesota', 'MN'),
        ('Mississippi', 'MS'),
        ('Missouri', 'MO'),
        ('Montana', 'MT'),
        ('Nebraska', 'NE'),
        ('Nevada', 'NV'),
        ('New Hampshire', 'NH'),
        ('New Jersey', 'NJ'),
        ('New Mexico', 'NM'),
        ('New York', 'NY'),
        ('North Carolina', 'NC'),
        ('North Dakota', 'ND'),
        ('Ohio', 'OH'),
        ('Oklahoma', 'OK'),
        ('Oregon', 'OR'),
        ('Pennsylvania', 'PA'),
        ('Rhode Island', 'RI'),
        ('South Carolina', 'SC'),
        ('South Dakota', 'SD'),
        ('Tennessee', 'TN'),
        ('Texas', 'TX'),
        ('Utah', 'UT'),
        ('Vermont', 'VT'),
        ('Virginia', 'VA'),
        ('Washington', 'WA'),
        ('West Virginia', 'WV'),
        ('Wisconsin', 'WI'),
        ('Wyoming', 'WY'),
    )
    
    AUTH_REQ = [(False, 'No'), (True, 'Yes')]

    date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    flight_time = models.FloatField(default=0.00, null=True, blank=True)
    event = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    auth_req = models.BooleanField("Authorization Required?", default="False", choices=AUTH_REQ)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=20, null=True,blank=True, choices=STATE_CODES, default='IN')
    notes = models.TextField(max_length=500, null=True, blank=True)
    drone = models.ForeignKey(Drones, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return str(self.event)

    class Meta:
        verbose_name_plural = "Flights"
        ordering = ['date']

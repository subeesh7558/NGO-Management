from email import message
from django.db import models





class designation(models.Model):
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.designation


class user_registration(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,
                                    related_name='userregistrationdesignation', null=True, blank=True)
    firstname = models.CharField(max_length=240, null=True)
    lastname = models.CharField(max_length=240, null=True)
    username = models.CharField(max_length=240, null=True)
    dateofbirth = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    gender = models.CharField(max_length=240, null=True)
    pincode = models.CharField(max_length=240, null=True)
    district = models.CharField(max_length=240, null=True)
    state = models.CharField(max_length=240, null=True)
    country = models.CharField(max_length=240, null=True)
    permanentaddress1 = models.CharField(max_length=240, null=True)
    permanentaddress2 = models.CharField(max_length=240, null=True)
    permanentaddress3 = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240, null=True)
    alternativeno = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default='')

    def __str__(self):
        return self.firstname




class doner_registration(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING, null=True, blank=True)
    duser = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, null=True, blank=True)
    firstname = models.CharField(max_length=240, null=True)
    lastname = models.CharField(max_length=240, null=True)
    pincode = models.CharField(max_length=240, null=True)
    country = models.CharField(max_length=240, null=True)
    permanentaddress1 = models.CharField(max_length=240, null=True)
    permanentaddress2 = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    payment = models.EmailField(max_length=240, null=True)
    message = models.EmailField(max_length=240, null=True)
    status = models.CharField(max_length=240, null=True, default='')

    def __str__(self):
        return self.firstname








class message_admin(models.Model):
    donuser = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, null=True, blank=True)
    message_to = models.ForeignKey(designation, on_delete=models.DO_NOTHING,null=True, blank=True)
    date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    message = models.TextField()
    replay = models.CharField(max_length=240, null=True, default='')


    def __str__(self):
        return self.message_to




class restaurant_registration(models.Model):
    
    restaurantname = models.CharField(max_length=240, null=True)
    location = models.CharField(max_length=240, null=True)
    username = models.CharField(max_length=240, null=True)
    pincode = models.CharField(max_length=240, null=True)
    district = models.CharField(max_length=240, null=True)
    state = models.CharField(max_length=240, null=True)
    country = models.CharField(max_length=240, null=True)
    permanentaddress1 = models.CharField(max_length=240, null=True)
    permanentaddress2 = models.CharField(max_length=240, null=True)
    permanentaddress3 = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240, null=True)
    alternativeno = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
   

    def __str__(self):
        return self.restaurantname




class request_food(models.Model):
    restaurantname = models.ForeignKey(restaurant_registration, on_delete=models.DO_NOTHING, null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default='')
    location = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240, null=True)
    date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    quantity = models.CharField(max_length=240, null=True, default='')
    cookedtime = models.CharField(max_length=240, null=True, default='')
    reason = models.CharField(max_length=240, null=True, default='')
   

    def __str__(self):
        return self.restaurantname
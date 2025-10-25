import random
import uuid
from wsgiref.validate import validator

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager , BaseUserManager , send_mail
from django.core import validators
from django.db import models
from django.utils import timezone


# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self , username , phone_number , email , password , is_staff , is_superuser , **extra_fields):
        now = timezone.now()
#create and saved user with username email phone number
        if not username:
            raise ValueError('The username must be set')
        email = self.normalize_email(email)
        user = self.model(phone_number = phone_number,
                          is_staff = is_staff,
                          is_superuser = is_superuser,
                          username = username,
                          email = email ,
                          is_active = True,
                          date_joined=now ,
                          **extra_fields)
        if not extra_fields.get('no_password'):
            user.set_password(password)

        user.save(using=self._db)
        return user
    def create_user(self , username=None , phone_number=None , email=None , password=None , **extra_fields):
        if username is None:
            if email :
                username =email.split('@' , 1)[0]
            if phone_number :
                username = random.choice('abcdefghijklmnopqrstuvwxyz') + str(phone_number)[-7:]
            while User.objects.filter(username=username).exists():
                username += str(random.randint(10 , 99))

        return self._create_user(username , phone_number , email , password , False , False  , **extra_fields)


    def create_superuser(self , username , phone_number , email , password , **extra_fields):
        return self._create_user(username, phone_number, email, password, True, True, **extra_fields)

    def get_by_phone_number(self , phone_number):
        return self.get(**{'phone_number':phone_number})




class User(AbstractBaseUser , PermissionsMixin):
    username = models.CharField(max_length=30
                                , unique=True
                                , help_text = "Required. 30 characters or fewer."
                                ,validators=[validators.RegexValidator(r'^[A-Za-z0-9_]+$' , "user name must be with characters" , "Invalid")]
                                , error_messages={"unique":"A user with that username already exists."})

    first_name = models.CharField(max_length=30 , blank=True)
    last_name = models.CharField(max_length=30 , blank=True)
    email = models.EmailField(unique=True , null=True, blank=True)
    phone_Number = models.BigIntegerField(unique = True , null=True, blank=True
                                          ,validators= [validators.RegexValidator(r'^989[0-3,9]\d{8}$' , "Enter a valid phone number.") ]
                                          ,error_messages={"unique":"A phone number already exists."})
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default= timezone.now)
    last_seen=models.DateTimeField(default=timezone.now)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email" , "phone_number"]

    class Meta :
        db_table = 'users'
        verbose_name = "user"
        verbose_name_plural = "users"



class UserProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=50 , blank=True)
    avatar = models.ImageField(blank=True)
    birthday = models.DateField(null=True , blank = True)
    gender = models.NullBooleanField(help_text="false is female  & true is male , null is unset")
    province = models.ForeignKey(to='Province',on_delete=models.SET_NULL , null=True , blank=True , help_text="Province")

    class Meta:
        db_table = "user_profiles"
        verbose_name = "user_profile"
        verbose_name_plural = "user_profiles"


class Device(models.Model):
    WEB = 1
    IOS = 2
    ANDROID = 3
    DEVICE_TYPE_CHOICES = (
    (WEB , "web") ,
    (IOS , "ios"),
    (ANDROID , "android")
    )

    user = models.ForeignKey(User,related_name="devices" ,on_delete=models.CASCADE)
    device_uuid = models.UUIDField('device uuid', null = True)
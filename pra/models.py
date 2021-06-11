from django.db import models
from django.contrib.auth.models import ( AbstractBaseUser, BaseUserManager )

# Create your models here.

class UserManager(BaseUserManager):
	def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
		if not email:
			raise ValueError("Users must have an email address")
		if not password:
			raise ValueError("users munt have a password")
		user = self.model(
			email = self.normalize_email(email)
			)
		user_obj.set_password(password)
		user_obj.staff = is_staff
		user_obj.admin = is_admin
		user_obj.avtive = is_active
		user_obj.save(using=self._db)
		return user_obj

	def create_staffuser(self, email, password=None):
		user = self.create_user(
			email,
			password=password,
			is_staff=True
			)
		return user


	def create_superuser(self, email, password=None):
		user = self.create_user(
			email,
			password=password,
			is_staff=True,
			is_admin=True
			)
		return user




class User(AbstractBaseUser):
	email 		= models.EmailField(max_length=332, unique=True)
	active		= models.BooleanField(default=True)
	staff		= models.BooleanField(default=True)
	admin		= models.BooleanField(default=True)
	tinestamp	= models.DateTimeField(auto_now_add=True)

	USERNAME_FIELD = 'email'
	REQUIRDE_FIELD = []

	def __str__(self):
		return self.email

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.email

	@property
	def is_staff(self):
		return self.staff

	@property
	def is_admin(self):
		return self.admin

	@property
	def is_active(self):
		return self.active

# class Profile(models.Model):
# 	user =models.OneToOneField(User)
	
	
	
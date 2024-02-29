from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError("Email field is required !")
		if not password:
			raise ValueError("Password field is required !")
		user = self.model(
			email=email
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		user = self.create_user(
			email=email, password=password)
		user.is_superuser = True
		user.is_staff = True
		user.is_admin = True
		user.save()
		return user

	def create_student(self, email,password):
		user = self.create_user(email, password)
		user.is_student = True
		user.save()
		return user

	def create_teacher(self, email, password):
		user = self.create_user(email, password)
		user.is_teacher = True
		user.save()
		return user

	def create_principal(self, email, password):
		user = self.create_user(email, password)
		user.is_principal = True
		user.save()
		return user


class User(AbstractBaseUser):
	last_name=models.CharField(max_length=150)
	first_name=models.CharField(max_length=150)
	email = models.CharField(
		max_length=200, blank=False, null=False, unique=True)

	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	is_student = models.BooleanField(default=False)
	is_teacher = models.BooleanField(default=False)
	is_principal = models.BooleanField(default=False)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	objects = UserManager()

	USERNAME_FIELD = "email"

	def __unicode__(self):
		return str(self.email)

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)
	

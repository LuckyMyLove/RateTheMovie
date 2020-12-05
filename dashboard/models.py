from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Actors(models.Model):
    firstname = models.TextField()
    surname = models.TextField()
    birthday = models.DateField()
    photo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Actors'


class ActorsRates(models.Model):
    actors = models.ForeignKey(Actors, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    rate = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Actors_rates'


class Categories(models.Model):
    name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'Categories'


class Directors(models.Model):
    firstname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthday = models.DateField()
    photo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Directors'


class DirectorsRates(models.Model):
    director = models.ForeignKey(Directors, models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    rate = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Directors_rates'


class Movies(models.Model):
    title = models.TextField()
    description = models.TextField()
    premier_date = models.DateField()
    category = models.ForeignKey(Categories, models.DO_NOTHING)
    picture = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Movies'


class Movies_Actors(models.Model):
    movie = models.ForeignKey(Movies, models.DO_NOTHING)
    actor = models.ForeignKey(Actors, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Movies_actors'


class Movies_directors(models.Model):
    movie = models.ForeignKey(Movies, models.DO_NOTHING)
    director = models.ForeignKey(Directors, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Movies_directors'


class Movies_rates(models.Model):
    movie = models.ForeignKey(Movies, models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    rate = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Movies_rates'


class Roles(models.Model):
    name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'Roles'


class Users(models.Model):
    username = models.TextField()
    password = models.TextField()
    firstname = models.TextField()
    surname = models.TextField()
    role = models.ForeignKey(Roles, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Users'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DashboardCategories(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'dashboard_categories'


class DashboardMovies(models.Model):
    title = models.TextField()
    description = models.TextField()
    premier_date = models.TextField()
    category_id = models.ForeignKey(DashboardCategories, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dashboard_movies'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

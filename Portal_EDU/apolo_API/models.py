# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
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


class TblAcademicCalendars(models.Model):
    id_academic_calendar = models.BigIntegerField(db_column='idAcademicCalendar', primary_key=True)  # Field name made lowercase.
    id_unit = models.ForeignKey('TblUnits', db_column='idUnit')  # Field name made lowercase.
    id_assignment = models.ForeignKey('TblAssignments', db_column='idAssignment')  # Field name made lowercase.
    ponderation = models.FloatField(db_column='ponderation')
    description = models.TextField(db_column='description', blank=True)
    delivery_date = models.DateTimeField(db_column='deliveryDate', blank=True, null=True)  # Field name made lowercase.
    need_file = models.BooleanField(db_column='needFile', blank=True, null=True)  # Field name made lowercase.
    enable_academic_calendar = models.BooleanField(db_column='enableAcademicCalendar')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAcademicCalendars'


class TblAcademies(models.Model):php
    id_academy = models.BigIntegerField(db_column='idAcademy', primary_key=True)  # Field name made lowercase.
    id_school = models.ForeignKey('TblSchools', db_column='idSchool')  # Field name made lowercase.
    id_year = models.ForeignKey('TblYears', db_column='idYear')  # Field name made lowercase.
    enable_academy = models.BooleanField(db_column='enableAcademy')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAcademies'


class TblAssignments(models.Model):
    id_assignment = models.BigIntegerField(db_column='idAssignment', primary_key=True)  # Field name made lowercase.
    assignment_name = models.CharField(db_column='assignmentName', max_length=45)  # Field name made lowercase.
    enable_assigment = models.BooleanField(db_column='enableAssigment')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAssignments'


class TblBloodTypes(models.Model):
    id_blood_type = models.BigIntegerField(db_column='idBloodType', primary_key=True)  # Field name made lowercase.
    blood_type = models.CharField(db_column='bloodType', max_length=45)  # Field name made lowercase.
    enable_blood_type = models.BooleanField(db_column='enableBloodType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblBloodTypes'


class TblClasses(models.Model):
    id_class = models.BigIntegerField(db_column='idClass', primary_key=True)  # Field name made lowercase.
    max_capacity_class = models.IntegerField(db_column='maxCapacityClass', blank=True, null=True)  # Field name made lowercase.
    quantity_class = models.IntegerField(db_column='quantityClass', blank=True, null=True)  # Field name made lowercase.
    id_grade = models.ForeignKey('TblGrades', db_column='idGrade')  # Field name made lowercase.
    id_course = models.ForeignKey('TblCourses', db_column='idCourse')  # Field name made lowercase.
    enable_class = models.BooleanField(db_column='enableClass')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblClasses'


class TblContactTypes(models.Model):
    id_contact_type = models.BigIntegerField(db_column='idContactType', primary_key=True)  # Field name made lowercase.
    contact_type = models.CharField(db_column='contactType', max_length=45)  # Field name made lowercase.
    enable_contact_type = models.BooleanField(db_column='enableContactType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblContactTypes'


class TblContacts(models.Model):
    id_contact = models.BigIntegerField(db_column='idContact', primary_key=True)  # Field name made lowercase.
    phone_contact = models.CharField(db_column='phoneContact', max_length=15)  # Field name made lowercase.
    id_contact_type = models.ForeignKey('TblContactTypes', db_column='idContactType')  # Field name made lowercase.
    enable_contact = models.BooleanField(db_column='enableContact')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblContacts'


class TblCourses(models.Model):
    id_course = models.BigIntegerField(db_column='idCourse', primary_key=True)  # Field name made lowercase.
    name_course = models.CharField(db_column='nameCourse', max_length=45, blank=True)  # Field name made lowercase.
    id_staff = models.ForeignKey('TblStaffs', db_column='idStaff')  # Field name made lowercase.
    id_schedule = models.ForeignKey('TblSchedules', db_column='idSchedule', blank=True, null=True)  # Field name made lowercase.
    min_note_course = models.IntegerField(db_column='minNoteCourse', blank=True, null=True)  # Field name made lowercase.
    max_note_course = models.IntegerField(db_column='maxNoteCourse', blank=True, null=True)  # Field name made lowercase.
    enable_course = models.BooleanField(db_column='enableCourse')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCourses'


class TblEntranceSchedules(models.Model):
    id_entrance_schedule = models.BigIntegerField(db_column='idEntranceSchedule', primary_key=True)  # Field name made lowercase.
    entrance_time = models.TimeField(db_column='entranceTime')  # Field name made lowercase.
    leave_time = models.TimeField(db_column='leaveTime', blank=True, null=True)  # Field name made lowercase.
    enable_entrance_schedule = models.BooleanField(db_column='enableEntranceSchedule')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblEntranceSchedules'


class TblExtraCurricularActivities(models.Model):
    id_extra_curricular_activity = models.BigIntegerField(db_column='idExtraCurricularActivity', primary_key=True)  # Field name made lowercase.
    name_activity = models.CharField(db_column='nameActivity', max_length=45)  # Field name made lowercase.
    date_time_activity = models.CharField(db_column='dateTimeActivity', max_length=45)  # Field name made lowercase.
    duration_extra_curricular_activity = models.IntegerField(db_column='durationExtraCurricularActivity', blank=True, null=True)  # Field name made lowercase.
    description_activity = models.TextField(db_column='descriptionActivity', blank=True)  # Field name made lowercase.
    id_staff = models.ForeignKey('TblStaffs', db_column='idStaff')  # Field name made lowercase.
    id_extra_curricular_activity_type = models.ForeignKey('TblExtraCurricularActivityTypes', db_column='idExtraCurricularActivityType', blank=True, null=True)  # Field name made lowercase.
    include_parents = models.BooleanField(db_column='includeParents')  # Field name made lowercase.
    include_students = models.BooleanField(db_column='includeStudents')  # Field name made lowercase.
    done_activity = models.BooleanField(db_column='doneActivity')  # Field name made lowercase.
    enable_extra_curricular_activity = models.BooleanField(db_column='enableExtraCurricularActivity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExtraCurricularActivities'


class TblExtraCurricularActivityTypes(models.Model):
    id_extra_curricular_activity_type = models.BigIntegerField(db_column='idExtraCurricularActivityType', primary_key=True)  # Field name made lowercase.
    extra_curricular_activity_type = models.CharField(db_column='extraCurricularActivityType', max_length=45)  # Field name made lowercase.
    enable_extra_curricular_activity_type = models.BooleanField(db_column='enableExtraCurricularActivityType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExtraCurricularActivityTypes'


class TblExtraCurricularCalendars(models.Model):
    id_extra_curricular_calendar = models.BigIntegerField(db_column='idExtraCurricularCalendar', primary_key=True)  # Field name made lowercase.
    id_extra_curricular_activity = models.ForeignKey('TblExtraCurricularActivities', db_column='idExtraCurricularActivity')  # Field name made lowercase.
    id_grade = models.ForeignKey('TblGrades', db_column='idGrade')  # Field name made lowercase.
    enable_extra_curricular_calendar = models.BooleanField(db_column='enableExtraCurricularCalendar')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExtraCurricularCalendars'


class TblGenres(models.Model):
    id_genre = models.BigIntegerField(db_column='idGenre', primary_key=True)  # Field name made lowercase.
    genre = models.CharField(max_length=20)
    enable_genre = models.BooleanField(db_column='enableGenre')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblGenres'


class TblGradeNames(models.Model):
    id_grade_name = models.BigIntegerField(db_column='idGradeName', primary_key=True)  # Field name made lowercase.
    gradename = models.CharField(db_column='gradeName', max_length=45)  # Field name made lowercase.
    enable_grade_name = models.BooleanField(db_column='enableGradeName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblGradeNames'


class TblGrades(models.Model):
    id_grade = models.BigIntegerField(db_column='idGrade', primary_key=True)  # Field name made lowercase.
    id_grade_name = models.ForeignKey('TblGradeNames', db_column='idGradeName')  # Field name made lowercase.
    id_section = models.ForeignKey('TblSections', db_column='idSection', blank=True, null=True)  # Field name made lowercase.
    id_staff = models.ForeignKey('TblStaffs', db_column='idStaff', blank=True, null=True)  # Field name made lowercase.
    id_level = models.ForeignKey('TblLevels', db_column='idLevel')  # Field name made lowercase.
    enable_grade = models.BooleanField(db_column='enableGrade')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblGrades'


class TblGuideTypes(models.Model):
    id_guide_type = models.BigIntegerField(db_column='idGuideType', primary_key=True)  # Field name made lowercase.
    guide_type = models.CharField(db_column='guideType', max_length=45)  # Field name made lowercase.
    enable_guide_type = models.BooleanField(db_column='enableGuideType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblGuideTypes'


class TblInchargeAppointments(models.Model):
    id_incharge_appointment = models.BigIntegerField(db_column='idInchargeAppointment', primary_key=True)  # Field name made lowercase.
    id_staff = models.ForeignKey('TblStaffs', db_column='idStaff')  # Field name made lowercase.
    id_student = models.ForeignKey('TblStudents', db_column='idStudent')  # Field name made lowercase.
    subject_incharge_appointment = models.CharField(db_column='subjectInchargeAppointment', max_length=45, blank=True)  # Field name made lowercase.
    description_incharge_appointment = models.TextField(db_column='descriptionInchargeAppointment', blank=True)  # Field name made lowercase.
    date_time_incharge_appointment = models.DateTimeField(db_column='dateTimeInchargeAppointment', blank=True, null=True)  # Field name made lowercase.
    duration_incharge_appointment = models.IntegerField(db_column='durationInchargeAppointment', blank=True, null=True)  # Field name made lowercase.
    confirmation_incharge_appointment = models.BooleanField(db_column='confirmationInchargeAppointment', blank=True, null=True)  # Field name made lowercase.
    status_incharge_appointment = models.BooleanField(db_column='statusInchargeAppointment', blank=True, null=True)  # Field name made lowercase.
    enable_incharge_appointment = models.BooleanField(db_column='enableInchargeAppointment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInchargeAppointments'


class TblIncharges(models.Model):
    id_incharge = models.BigIntegerField(db_column='idIncharge', primary_key=True)  # Field name made lowercase.
    id_student = models.ForeignKey('TblStudents', db_column='idStudent')  # Field name made lowercase.
    id_parents = models.ForeignKey('TblParents', db_column='idParents')  # Field name made lowercase.
    enable_incharge = models.BooleanField(db_column='enableIncharge')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblIncharges'


class TblLevels(models.Model):
    id_level = models.BigIntegerField(db_column='idLevel', primary_key=True)  # Field name made lowercase.
    level_name = models.CharField(db_column='levelName', max_length=45)  # Field name made lowercase.
    enable_levels = models.BooleanField(db_column='enableLevels')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLevels'


class TblLogin(models.Model):
    id_login = models.BigIntegerField(db_column='idLogin', primary_key=True)  # Field name made lowercase.
    user_login = models.CharField(db_column='userLogin', max_length=45)  # Field name made lowercase.
    password_login = models.CharField(db_column='passwordLogin', max_length=45)  # Field name made lowercase.
    enable_login = models.BooleanField(db_column='enableLogin')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLogin'


class TblMedicalBackGrounds(models.Model):
    id_medical_background = models.BigIntegerField(db_column='idMedicalBackground', primary_key=True)  # Field name made lowercase.
    medical_background = models.TextField(db_column='medicalBackground')  # Field name made lowercase.
    enable_medical_background = models.BooleanField(db_column='enableMedicalBackground')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMedicalBackgrounds'


class TblModules(models.Model):
    id_module = models.BigIntegerField(db_column='idModule', primary_key=True)  # Field name made lowercase.
    module_name = models.CharField(db_column='moduleName', max_length=45)  # Field name made lowercase.
    enable_module = models.BooleanField(db_column='enableModule')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblModules'


class TblParents(models.Model):
    id_parents = models.BigIntegerField(db_column='idParents', primary_key=True)  # Field name made lowercase.
    first_name_parent = models.CharField(db_column='firstNameParent', max_length=45, blank=True)  # Field name made lowercase.
    last_name_parent = models.CharField(db_column='lastNameParent', max_length=45, blank=True)  # Field name made lowercase.
    birth_date_parent = models.CharField(db_column='birthDateParent', max_length=45, blank=True)  # Field name made lowercase.
    email_parent = models.CharField(db_column='emailParent', max_length=45, blank=True)  # Field name made lowercase.
    id_genre = models.ForeignKey('TblGenres', db_column='idGenre')  # Field name made lowercase.
    id_guide_type = models.ForeignKey('TblGuideTypes', db_column='idGuideType')  # Field name made lowercase.
    id_login = models.ForeignKey('TblLogin', db_column='idLogin', blank=True, null=True)  # Field name made lowercase.
    enable_parent = models.BooleanField(db_column='enableParent')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblParents'


class TblPlanificationTypes(models.Model):
    id_planification_type = models.BigIntegerField(db_column='idPlanificationType', primary_key=True)  # Field name made lowercase.
    planification_type = models.CharField(db_column='planificationType', max_length=45)  # Field name made lowercase.
    enable_planification_type = models.BooleanField(db_column='enablePlanificationType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPlanificationTypes'


class TblPlanifications(models.Model):
    id_planification = models.BigIntegerField(db_column='idPlanification', primary_key=True)  # Field name made lowercase.
    planification_file = models.FileField(db_column='planificationFile', blank=True)  # Field name made lowercase.
    id_course = models.ForeignKey('TblCourses', db_column='idCourse')  # Field name made lowercase.
    id_planification_type = models.ForeignKey('TblPlanificationTypes', db_column='idPlanificationType')  # Field name made lowercase.
    enable_planification = models.BooleanField(db_column='enablePlanification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPlanifications'


class TblSchedules(models.Model):
    id_schedule = models.BigIntegerField(db_column='idSchedule', primary_key=True)  # Field name made lowercase.
    init_time = models.TimeField(db_column='initTime')  # Field name made lowercase.
    end_time = models.TimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    enable_schedule = models.BooleanField(db_column='enableSchedule')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSchedules'


class TblSchools(models.Model):
    id_school = models.BigIntegerField(db_column='idSchool', primary_key=True)  # Field name made lowercase.
    name_school = models.CharField(db_column='nameSchool', max_length=45)  # Field name made lowercase.
    phone_school = models.CharField(db_column='phoneSchool', max_length=45, blank=True)  # Field name made lowercase.
    address_school = models.CharField(db_column='addressSchool', max_length=45, blank=True)  # Field name made lowercase.
    director_name = models.CharField(db_column='directorName', max_length=45, blank=True)  # Field name made lowercase.
    enable_school = models.BooleanField(db_column='enableSchool')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSchools'


class TblSections(models.Model):
    id_section = models.BigIntegerField(db_column='idSection', primary_key=True)  # Field name made lowercase.
    name_section = models.CharField(db_column='nameSection', max_length=5)  # Field name made lowercase.
    enable_section = models.BooleanField(db_column='enableSection')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSections'


class TblStaffActivities(models.Model):
    id_staff_activitt = models.BigIntegerField(db_column='idStaffActivitt', primary_key=True)  # Field name made lowercase.
    name_staff_activity = models.CharField(db_column='nameStaffActivity', max_length=45)  # Field name made lowercase.
    date_time_staff_activity = models.DateTimeField(db_column='dateTimeStaffActivity', blank=True, null=True)  # Field name made lowercase.
    descripcion_staff_activity = models.CharField(db_column='descripcionStaffActivity', max_length=255, blank=True)  # Field name made lowercase.
    done = models.IntegerField(blank=True, null=True)
    enable_staff_activity = models.BooleanField(db_column='enableStaffActivity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStaffActivities'


class TblStaffAppointments(models.Model):
    id_staff_appointment = models.BigIntegerField(db_column='idStaffAppointment', primary_key=True)  # Field name made lowercase.
    id_student = models.ForeignKey('TblStudents', db_column='idStudent')  # Field name made lowercase.
    id_staff = models.ForeignKey('TblStaffs', db_column='idStaff')  # Field name made lowercase.
    subject_staff_appointment = models.CharField(db_column='subjectStaffAppointment', max_length=45, blank=True)  # Field name made lowercase.
    description_staff_appointment = models.CharField(db_column='descriptionStaffAppointment', max_length=45, blank=True)  # Field name made lowercase.
    date_time_staff_appointment = models.DateTimeField(db_column='dateTimeStaffAppointment', blank=True, null=True)  # Field name made lowercase.
    duration_staff_appointment = models.IntegerField(db_column='durationStaffAppointment', blank=True, null=True)  # Field name made lowercase.
    confirmation_staff_appointment = models.BooleanField(db_column='confirmationStaffAppointment', blank=True, null=True)  # Field name made lowercase.
    status_staff_appointment = models.BooleanField(db_column='statusStaffAppointment', blank=True, null=True)  # Field name made lowercase.
    enable_staff_appointment = models.BooleanField(db_column='enableStaffAppointment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStaffAppointments'


class TblStaffCalendars(models.Model):
    id_staff_calendar = models.BigIntegerField(db_column='idStaffCalendar', primary_key=True)  # Field name made lowercase.
    id_staff = models.ForeignKey('TblStaffs', db_column='idStaff')  # Field name made lowercase.
    id_staff_activity = models.ForeignKey('TblStaffActivities', db_column='idStaffActivity')  # Field name made lowercase.
    enable_staff_calendar = models.BooleanField(db_column='enableStaffCalendar')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStaffCalendars'


class TblStaffContactLists(models.Model):
    id_staff_contact_list = models.BigIntegerField(db_column='idStaffContactList', primary_key=True)  # Field name made lowercase.
    id_staff = models.ForeignKey('TblStaffs', db_column='idStaff')  # Field name made lowercase.
    id_contact = models.ForeignKey('TblContacts', db_column='idContact')  # Field name made lowercase.
    enable_staff_contact_list = models.BooleanField(db_column='enableStaffContactList')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStaffContactLists'


class TblStaffEntranceReports(models.Model):
    id_staff_entrance_report = models.BigIntegerField(db_column='idStaffEntranceReport', primary_key=True)  # Field name made lowercase.
    date_time_staff_entrance = models.DateTimeField(db_column='dateTimeStaffEntrance')  # Field name made lowercase.
    date_time_staff_exit = models.DateTimeField(db_column='dateTimeStaffExit', blank=True, null=True)  # Field name made lowercase.
    id_staff = models.ForeignKey('TblStaffs', db_column='idStaff')  # Field name made lowercase.
    enable_staff_entrance_report = models.BooleanField(db_column='enableStaffEntranceReport')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStaffEntranceReports'


class TblStaffMedicalBackGroundLists(models.Model):
    id_staff_medical_background_list = models.BigIntegerField(db_column='idStaffMedicalBackGroundList', primary_key=True)  # Field name made lowercase.
    id_staff = models.ForeignKey('TblStaffs', db_column='idStaff')  # Field name made lowercase.
    idmedicalbackground = models.ForeignKey('TblMedicalBackGrounds', db_column='idMedicalBackground')  # Field name made lowercase.
    enablestaffmedicalbackgroundlist = models.BooleanField(db_column='enableStaffMedicalBackGroundList')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStaffMedicalBackGroundLists'


class TblStaffMeetingSchedules(models.Model):
    id_staff_meeting_schedule = models.BigIntegerField(db_column='idStaffMeetingSchedule', primary_key=True)  # Field name made lowercase.
    id_staff = models.ForeignKey('TblStaffs', db_column='idStaff')  # Field name made lowercase.
    date_time_init_staff_meeting_schedule = models.DateTimeField(db_column='dateTimeInitStaffMeetingSchedule')  # Field name made lowercase.
    date_time_end_staff_meeting_schedule = models.DateTimeField(db_column='dateTimeEndStaffMeetingSchedule')  # Field name made lowercase.
    enable_staff_meeting_schedule = models.BooleanField(db_column='enableStaffMeetingSchedule', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStaffMeetingSchedules'


class TblStaffTypes(models.Model):
    id_staff_type = models.BigIntegerField(db_column='idStaffType', primary_key=True)  # Field name made lowercase.
    staff_type = models.CharField(db_column='staffType', max_length=45)  # Field name made lowercase.
    enable_staff_type = models.BooleanField(db_column='enableStaffType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStaffTypes'


class TblStaffs(models.Model):
    id_staff = models.BigIntegerField(db_column='idStaff', primary_key=True)  # Field name made lowercase.
    image_staff = models.ImageField(db_column='imageStaff', blank=True)  # Field name made lowercase.
    code_staff = models.CharField(db_column='codeStaff', max_length=45, blank=True)  # Field name made lowercase.
    first_name_staff = models.CharField(db_column='firstNameStaff', max_length=45)  # Field name made lowercase.
    last_name_staff = models.CharField(db_column='lastNameStaff', max_length=45)  # Field name made lowercase.
    birth_date_staff = models.CharField(db_column='birthDateStaff', max_length=45, blank=True)  # Field name made lowercase.
    email_staff = models.CharField(db_column='emailStaff', max_length=45, blank=True)  # Field name made lowercase.
    id_genre = models.ForeignKey('TblGenres', db_column='idGenre')  # Field name made lowercase.
    id_blood_type = models.ForeignKey('TblBloodTypes', db_column='idBloodType')  # Field name made lowercase.
    id_entrance_schedule = models.ForeignKey('TblEntranceSchedules', db_column='idEntranceSchedule', blank=True, null=True)  # Field name made lowercase.
    id_staff_type = models.ForeignKey('TblStaffTypes', db_column='idStaffType')  # Field name made lowercase.
    id_login = models.ForeignKey('TblLogin', db_column='idLogin', blank=True, null=True)  # Field name made lowercase.
    enable_staff = models.BooleanField(db_column='enableStaff')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStaffs'


class TblStudentLists(models.Model):
    id_student_list = models.BigIntegerField(db_column='idStudentList', primary_key=True)  # Field name made lowercase.
    id_student = models.ForeignKey('TblStudents', db_column='idStudent')  # Field name made lowercase.
    id_grade = models.ForeignKey('TblGrades', db_column='idGrade')  # Field name made lowercase.
    id_academy = models.ForeignKey('TblAcademies', db_column='idAcademy')  # Field name made lowercase.
    enable_student_list = models.BooleanField(db_column='enableStudentList')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStudentLists'


class TblStudentMedicalBackGroundLists(models.Model):
    id_student_medical_background_list = models.BigIntegerField(db_column='idStudentMedicalBackgroundList', primary_key=True)  # Field name made lowercase.
    id_student = models.ForeignKey('TblStudents', db_column='idStudent')  # Field name made lowercase.
    id_disease = models.ForeignKey('TblMedicalBackGrounds', db_column='idDisease')  # Field name made lowercase.
    enable_student_medical_background_list = models.BooleanField(db_column='enableStudentMedicalBackgroundList')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStudentMedicalBackgroundLists'


class TblStudentReports(models.Model):
    id_student_report = models.BigIntegerField(db_column='idStudentReport', primary_key=True)  # Field name made lowercase.
    id_student = models.ForeignKey('TblStudents', db_column='idStudent')  # Field name made lowercase.
    subject_student_report = models.CharField(db_column='subjectStudentReport', max_length=45, blank=True)  # Field name made lowercase.
    description_student_report = models.TextField(db_column='descriptionStudentReport', blank=True)  # Field name made lowercase.
    date_time_sent_report = models.DateTimeField(db_column='dateTimeSentReport', blank=True, null=True)  # Field name made lowercase.
    checked_report = models.BooleanField(db_column='checkedReport', blank=True, null=True)  # Field name made lowercase.
    date_time_checked_report = models.DateTimeField(db_column='dateTimeCheckedReport', blank=True, null=True)  # Field name made lowercase.
    enable_student_report = models.BooleanField(db_column='enableStudentReport')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStudentReports'


class TblStudents(models.Model):
    id_student = models.BigIntegerField(db_column='idStudent', primary_key=True)  # Field name made lowercase.
    image_student = models.ImageField(db_column='imageStudent', blank=True)  # Field name made lowercase.
    code_student = models.CharField(db_column='codeStudent', max_length=45, blank=True)  # Field name made lowercase.
    first_name_student = models.CharField(db_column='firstNameStudent', max_length=45)  # Field name made lowercase.
    last_name_student = models.CharField(db_column='lastNameStudent', max_length=45)  # Field name made lowercase.
    birth_date_student = models.DateField(db_column='birthDateStudent')  # Field name made lowercase.
    email_student = models.CharField(db_column='emailStudent', max_length=45, blank=True)  # Field name made lowercase.
    id_genre = models.ForeignKey('TblGenres', db_column='idGenre')  # Field name made lowercase.
    id_blood_type = models.ForeignKey('TblBloodTypes', db_column='idBloodType')  # Field name made lowercase.
    id_login = models.ForeignKey('TblLogin', db_column='idLogin', blank=True, null=True)  # Field name made lowercase.
    enable_student = models.BooleanField(db_column='enableStudent')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStudents'


class TblStundentContactLists(models.Model):
    id_stundent_contact_list = models.BigIntegerField(db_column='idStundentContactList', primary_key=True)  # Field name made lowercase.
    id_student = models.ForeignKey('TblStudents', db_column='idStudent')  # Field name made lowercase.
    id_contact = models.ForeignKey('TblContacts', db_column='idContact')  # Field name made lowercase.
    enable_student_contact_list = models.BooleanField(db_column='enableStudentContactList')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStundentContactLists'


class TblTasks(models.Model):
    id_task = models.BigIntegerField(db_column='idTask', primary_key=True)  # Field name made lowercase.
    id_academic_calendar = models.ForeignKey('TblAcademicCalendars', db_column='idAcademicCalendar', blank=True, null=True)  # Field name made lowercase.
    ponderation_task = models.FloatField(db_column='ponderationTask', blank=True, null=True)  # Field name made lowercase.
    delivered_date = models.DateTimeField(db_column='deliveredDate', blank=True, null=True)  # Field name made lowercase.
    checked = models.IntegerField(blank=True, null=True)
    teacher_commentary_task = models.TextField(db_column='teacherCommentaryTask', blank=True)  # Field name made lowercase.
    file_task = models.FileField(db_column='fileTask', blank=True)  # Field name made lowercase.
    enable_task = models.BooleanField(db_column='enableTask')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTasks'


class TblUnits(models.Model):
    id_unit = models.BigIntegerField(db_column='idUnit', primary_key=True)  # Field name made lowercase.
    id_course = models.ForeignKey('TblCourses', db_column='idCourse')  # Field name made lowercase.
    id_module = models.ForeignKey('TblModules', db_column='idModule')  # Field name made lowercase.
    enable_unit = models.BooleanField(db_column='enableUnit')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUnits'


class TblYears(models.Model):
    id_year = models.BigIntegerField(db_column='idYear', primary_key=True)  # Field name made lowercase.
    year = models.IntegerField()
    enable_year = models.BooleanField(db_column='enableYear')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblYears'

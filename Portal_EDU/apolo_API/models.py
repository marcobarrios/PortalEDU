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


class Tblacademiccalendars(models.Model):
    idacademiccalendar = models.BigIntegerField(db_column='idAcademicCalendar', primary_key=True)  # Field name made lowercase.
    idunit = models.ForeignKey('Tblunits', db_column='idUnit')  # Field name made lowercase.
    idassignment = models.ForeignKey('Tblassignments', db_column='idAssignment')  # Field name made lowercase.
    ponderation = models.FloatField()
    description = models.TextField(blank=True)
    deliverydate = models.DateTimeField(db_column='deliveryDate', blank=True, null=True)  # Field name made lowercase.
    needfile = models.IntegerField(db_column='needFile', blank=True, null=True)  # Field name made lowercase.
    enableacademiccalendar = models.IntegerField(db_column='enableAcademicCalendar')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAcademicCalendars'


class Tblacademies(models.Model):
    idacademy = models.BigIntegerField(db_column='idAcademy', primary_key=True)  # Field name made lowercase.
    idschool = models.ForeignKey('Tblschools', db_column='idSchool')  # Field name made lowercase.
    idyear = models.ForeignKey('Tblyears', db_column='idYear')  # Field name made lowercase.
    enableacademy = models.IntegerField(db_column='enableAcademy')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAcademies'


class Tblassignments(models.Model):
    idassignment = models.BigIntegerField(db_column='idAssignment', primary_key=True)  # Field name made lowercase.
    assignmentname = models.CharField(db_column='assignmentName', max_length=45)  # Field name made lowercase.
    enableassigment = models.IntegerField(db_column='enableAssigment')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAssignments'


class Tblbloodtypes(models.Model):
    idbloodtype = models.BigIntegerField(db_column='idBloodType', primary_key=True)  # Field name made lowercase.
    bloodtype = models.CharField(db_column='bloodType', max_length=45)  # Field name made lowercase.
    enablebloodtype = models.IntegerField(db_column='enableBloodType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblBloodTypes'


class Tblclasses(models.Model):
    idclass = models.BigIntegerField(db_column='idClass', primary_key=True)  # Field name made lowercase.
    maxcapacityclass = models.IntegerField(db_column='maxCapacityClass', blank=True, null=True)  # Field name made lowercase.
    quantityclass = models.IntegerField(db_column='quantityClass', blank=True, null=True)  # Field name made lowercase.
    idgrade = models.ForeignKey('Tblgrades', db_column='idGrade')  # Field name made lowercase.
    idcourse = models.ForeignKey('Tblcourses', db_column='idCourse')  # Field name made lowercase.
    enableclass = models.IntegerField(db_column='enableClass')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblClasses'


class Tblcontacttypes(models.Model):
    idcontacttype = models.BigIntegerField(db_column='idContactType', primary_key=True)  # Field name made lowercase.
    contacttype = models.CharField(db_column='contactType', max_length=45)  # Field name made lowercase.
    enablecontacttype = models.IntegerField(db_column='enableContactType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblContactTypes'


class Tblcontacts(models.Model):
    idcontact = models.BigIntegerField(db_column='idContact', primary_key=True)  # Field name made lowercase.
    phonecontact = models.CharField(db_column='phoneContact', max_length=15)  # Field name made lowercase.
    idcontacttype = models.ForeignKey(Tblcontacttypes, db_column='idContactType')  # Field name made lowercase.
    enablecontact = models.IntegerField(db_column='enableContact')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblContacts'


class Tblcourses(models.Model):
    idcourse = models.BigIntegerField(db_column='idCourse', primary_key=True)  # Field name made lowercase.
    namecourse = models.CharField(db_column='nameCourse', max_length=45, blank=True)  # Field name made lowercase.
    idstaff = models.ForeignKey('Tblstaffs', db_column='idStaff')  # Field name made lowercase.
    idschedule = models.ForeignKey('Tblschedules', db_column='idSchedule', blank=True, null=True)  # Field name made lowercase.
    minnotecourse = models.IntegerField(db_column='minNoteCourse', blank=True, null=True)  # Field name made lowercase.
    maxnotecourse = models.IntegerField(db_column='maxNoteCourse', blank=True, null=True)  # Field name made lowercase.
    enablecourse = models.IntegerField(db_column='enableCourse')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblCourses'


class Tblentranceschedules(models.Model):
    identranceschedule = models.BigIntegerField(db_column='idEntranceSchedule', primary_key=True)  # Field name made lowercase.
    entrancetime = models.TimeField(db_column='entranceTime')  # Field name made lowercase.
    leavetime = models.TimeField(db_column='leaveTime', blank=True, null=True)  # Field name made lowercase.
    enableentranceschedule = models.IntegerField(db_column='enableEntranceSchedule')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblEntranceSchedules'


class Tblextracurricularactivities(models.Model):
    idextracurricularactivity = models.BigIntegerField(db_column='idExtraCurricularActivity', primary_key=True)  # Field name made lowercase.
    nameactivity = models.CharField(db_column='nameActivity', max_length=45)  # Field name made lowercase.
    datetimeactivity = models.CharField(db_column='dateTimeActivity', max_length=45)  # Field name made lowercase.
    durationextracurricularactivity = models.IntegerField(db_column='durationExtraCurricularActivity', blank=True, null=True)  # Field name made lowercase.
    descriptionactivity = models.TextField(db_column='descriptionActivity', blank=True)  # Field name made lowercase.
    idstaff = models.ForeignKey('Tblstaffs', db_column='idStaff')  # Field name made lowercase.
    idextracurricularactivitytype = models.ForeignKey('Tblextracurricularactivitytypes', db_column='idExtraCurricularActivityType', blank=True, null=True)  # Field name made lowercase.
    includeparents = models.IntegerField(db_column='includeParents')  # Field name made lowercase.
    includestudents = models.IntegerField(db_column='includeStudents')  # Field name made lowercase.
    doneactivity = models.IntegerField(db_column='doneActivity')  # Field name made lowercase.
    enableextracurricularactivity = models.IntegerField(db_column='enableExtraCurricularActivity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExtraCurricularActivities'


class Tblextracurricularactivitytypes(models.Model):
    idextracurricularactivitytype = models.BigIntegerField(db_column='idExtraCurricularActivityType', primary_key=True)  # Field name made lowercase.
    extracurricularactivitytype = models.CharField(db_column='extraCurricularActivityType', max_length=45)  # Field name made lowercase.
    enableextracurricularactivitytype = models.IntegerField(db_column='enableExtraCurricularActivityType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExtraCurricularActivityTypes'


class Tblextracurricularcalendars(models.Model):
    idextracurricularcalendar = models.BigIntegerField(db_column='idExtraCurricularCalendar', primary_key=True)  # Field name made lowercase.
    idextracurricularactivity = models.ForeignKey(Tblextracurricularactivities, db_column='idExtraCurricularActivity')  # Field name made lowercase.
    idgrade = models.ForeignKey('Tblgrades', db_column='idGrade')  # Field name made lowercase.
    enableextracurricularcalendar = models.IntegerField(db_column='enableExtraCurricularCalendar')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblExtraCurricularCalendars'


class Tblgenres(models.Model):
    idgenre = models.BigIntegerField(db_column='idGenre', primary_key=True)  # Field name made lowercase.
    genre = models.CharField(max_length=20)
    enablegenre = models.IntegerField(db_column='enableGenre')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblGenres'


class Tblgradenames(models.Model):
    idgradename = models.BigIntegerField(db_column='idGradeName', primary_key=True)  # Field name made lowercase.
    gradename = models.CharField(db_column='gradeName', max_length=45)  # Field name made lowercase.
    enablegradename = models.IntegerField(db_column='enableGradeName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblGradeNames'


class Tblgrades(models.Model):
    idgrade = models.BigIntegerField(db_column='idGrade', primary_key=True)  # Field name made lowercase.
    idgradename = models.ForeignKey(Tblgradenames, db_column='idGradeName')  # Field name made lowercase.
    idsection = models.ForeignKey('Tblsections', db_column='idSection', blank=True, null=True)  # Field name made lowercase.
    idstaff = models.ForeignKey('Tblstaffs', db_column='idStaff', blank=True, null=True)  # Field name made lowercase.
    idlevel = models.ForeignKey('Tbllevels', db_column='idLevel')  # Field name made lowercase.
    enablegrade = models.IntegerField(db_column='enableGrade')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblGrades'


class Tblguidetypes(models.Model):
    idguidetype = models.BigIntegerField(db_column='idGuideType', primary_key=True)  # Field name made lowercase.
    guidetype = models.CharField(db_column='guideType', max_length=45)  # Field name made lowercase.
    enableguidetype = models.IntegerField(db_column='enableGuideType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblGuideTypes'


class Tblinchargeappointments(models.Model):
    idinchargeappointment = models.BigIntegerField(db_column='idInchargeAppointment', primary_key=True)  # Field name made lowercase.
    idstaff = models.ForeignKey('Tblstaffs', db_column='idStaff')  # Field name made lowercase.
    idstudent = models.ForeignKey('Tblstudents', db_column='idStudent')  # Field name made lowercase.
    subjectinchargeappointment = models.CharField(db_column='subjectInchargeAppointment', max_length=45, blank=True)  # Field name made lowercase.
    descriptioninchargeappointment = models.TextField(db_column='descriptionInchargeAppointment', blank=True)  # Field name made lowercase.
    datetimeinchargeappointment = models.DateTimeField(db_column='dateTimeInchargeAppointment', blank=True, null=True)  # Field name made lowercase.
    durationinchargeappointment = models.IntegerField(db_column='durationInchargeAppointment', blank=True, null=True)  # Field name made lowercase.
    confirmationinchargeappointment = models.IntegerField(db_column='confirmationInchargeAppointment', blank=True, null=True)  # Field name made lowercase.
    statusinchargeappointment = models.IntegerField(db_column='statusInchargeAppointment', blank=True, null=True)  # Field name made lowercase.
    enableinchargeappointment = models.IntegerField(db_column='enableInchargeAppointment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblInchargeAppointments'


class Tblincharges(models.Model):
    idincharge = models.BigIntegerField(db_column='idIncharge', primary_key=True)  # Field name made lowercase.
    idstudent = models.ForeignKey('Tblstudents', db_column='idStudent')  # Field name made lowercase.
    idparents = models.ForeignKey('Tblparents', db_column='idParents')  # Field name made lowercase.
    enableincharge = models.IntegerField(db_column='enableIncharge')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblIncharges'


class Tbllevels(models.Model):
    idlevel = models.BigIntegerField(db_column='idLevel', primary_key=True)  # Field name made lowercase.
    levelname = models.CharField(db_column='levelName', max_length=45)  # Field name made lowercase.
    enablelevels = models.IntegerField(db_column='enableLevels')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLevels'


class Tbllogin(models.Model):
    idlogin = models.BigIntegerField(db_column='idLogin', primary_key=True)  # Field name made lowercase.
    userlogin = models.CharField(db_column='userLogin', max_length=45)  # Field name made lowercase.
    passwordlogin = models.CharField(db_column='passwordLogin', max_length=45)  # Field name made lowercase.
    enablelogin = models.IntegerField(db_column='enableLogin')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLogin'


class Tblmedicalbackgrounds(models.Model):
    idmedicalbackground = models.BigIntegerField(db_column='idMedicalBackground', primary_key=True)  # Field name made lowercase.
    medicalbackground = models.TextField(db_column='medicalBackground')  # Field name made lowercase.
    enablemedicalbackground = models.IntegerField(db_column='enableMedicalBackground')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMedicalBackgrounds'


class Tblmodules(models.Model):
    idmodule = models.BigIntegerField(db_column='idModule', primary_key=True)  # Field name made lowercase.
    modulename = models.CharField(db_column='moduleName', max_length=45)  # Field name made lowercase.
    enablemodule = models.IntegerField(db_column='enableModule')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblModules'


class Tblparents(models.Model):
    idparents = models.BigIntegerField(db_column='idParents', primary_key=True)  # Field name made lowercase.
    firstnameparent = models.CharField(db_column='firstNameParent', max_length=45, blank=True)  # Field name made lowercase.
    lastnameparent = models.CharField(db_column='lastNameParent', max_length=45, blank=True)  # Field name made lowercase.
    birthdateparent = models.CharField(db_column='birthDateParent', max_length=45, blank=True)  # Field name made lowercase.
    emailparent = models.CharField(db_column='emailParent', max_length=45, blank=True)  # Field name made lowercase.
    idgenre = models.ForeignKey(Tblgenres, db_column='idGenre')  # Field name made lowercase.
    idguidetype = models.ForeignKey(Tblguidetypes, db_column='idGuideType')  # Field name made lowercase.
    idlogin = models.ForeignKey(Tbllogin, db_column='idLogin', blank=True, null=True)  # Field name made lowercase.
    enableparent = models.IntegerField(db_column='enableParent')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblParents'


class Tblplanificationtypes(models.Model):
    idplanificationtype = models.BigIntegerField(db_column='idPlanificationType', primary_key=True)  # Field name made lowercase.
    planificationtype = models.CharField(db_column='planificationType', max_length=45)  # Field name made lowercase.
    enableplanificationtype = models.IntegerField(db_column='enablePlanificationType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPlanificationTypes'


class Tblplanifications(models.Model):
    idplanification = models.BigIntegerField(db_column='idPlanification', primary_key=True)  # Field name made lowercase.
    planificationfile = models.TextField(db_column='planificationFile', blank=True)  # Field name made lowercase.
    idcourse = models.ForeignKey(Tblcourses, db_column='idCourse')  # Field name made lowercase.
    idplanificationtype = models.ForeignKey(Tblplanificationtypes, db_column='idPlanificationType')  # Field name made lowercase.
    enableplanification = models.IntegerField(db_column='enablePlanification', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblPlanifications'


class Tblschedules(models.Model):
    idschedule = models.BigIntegerField(db_column='idSchedule', primary_key=True)  # Field name made lowercase.
    inittime = models.TimeField(db_column='initTime')  # Field name made lowercase.
    endtime = models.TimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    enableschedule = models.IntegerField(db_column='enableSchedule')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSchedules'


class Tblschools(models.Model):
    idschool = models.BigIntegerField(db_column='idSchool', primary_key=True)  # Field name made lowercase.
    nameschool = models.CharField(db_column='nameSchool', max_length=45)  # Field name made lowercase.
    phoneschool = models.CharField(db_column='phoneSchool', max_length=45, blank=True)  # Field name made lowercase.
    addressschool = models.CharField(db_column='addressSchool', max_length=45, blank=True)  # Field name made lowercase.
    directorname = models.CharField(db_column='directorName', max_length=45, blank=True)  # Field name made lowercase.
    enableschool = models.IntegerField(db_column='enableSchool')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSchools'


class Tblsections(models.Model):
    idsection = models.BigIntegerField(db_column='idSection', primary_key=True)  # Field name made lowercase.
    namesection = models.CharField(db_column='nameSection', max_length=5)  # Field name made lowercase.
    enablesection = models.IntegerField(db_column='enableSection')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblSections'


class Tblstaffactivities(models.Model):
    idstaffactivitt = models.BigIntegerField(db_column='idStaffActivitt', primary_key=True)  # Field name made lowercase.
    namestaffactivity = models.CharField(db_column='nameStaffActivity', max_length=45)  # Field name made lowercase.
    datetimestaffactivity = models.DateTimeField(db_column='dateTimeStaffActivity', blank=True, null=True)  # Field name made lowercase.
    descripcionstaffactivity = models.CharField(db_column='descripcionStaffActivity', max_length=255, blank=True)  # Field name made lowercase.
    done = models.IntegerField(blank=True, null=True)
    enablestaffactivity = models.IntegerField(db_column='enableStaffActivity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStaffActivities'


class Tblstaffappointments(models.Model):
    idstaffappointment = models.BigIntegerField(db_column='idStaffAppointment', primary_key=True)  # Field name made lowercase.
    idstudent = models.ForeignKey('Tblstudents', db_column='idStudent')  # Field name made lowercase.
    idstaff = models.ForeignKey('Tblstaffs', db_column='idStaff')  # Field name made lowercase.
    subjectstaffappointment = models.CharField(db_column='subjectStaffAppointment', max_length=45, blank=True)  # Field name made lowercase.
    descriptionstaffappointment = models.CharField(db_column='descriptionStaffAppointment', max_length=45, blank=True)  # Field name made lowercase.
    datetimestaffappointment = models.DateTimeField(db_column='dateTimeStaffAppointment', blank=True, null=True)  # Field name made lowercase.
    durationstaffappointment = models.IntegerField(db_column='durationStaffAppointment', blank=True, null=True)  # Field name made lowercase.
    confirmationstaffappointment = models.IntegerField(db_column='confirmationStaffAppointment', blank=True, null=True)  # Field name made lowercase.
    statusstaffappointment = models.IntegerField(db_column='statusStaffAppointment', blank=True, null=True)  # Field name made lowercase.
    enablestaffappointment = models.IntegerField(db_column='enableStaffAppointment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStaffAppointments'


class Tblstaffcalendars(models.Model):
    idstaffcalendar = models.BigIntegerField(db_column='idStaffCalendar', primary_key=True)  # Field name made lowercase.
    idstaff = models.ForeignKey('Tblstaffs', db_column='idStaff')  # Field name made lowercase.
    idstaffactivity = models.ForeignKey(Tblstaffactivities, db_column='idStaffActivity')  # Field name made lowercase.
    enablestaffcalendar = models.IntegerField(db_column='enableStaffCalendar')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStaffCalendars'


class Tblstaffcontactlists(models.Model):
    idstaffcontactlist = models.BigIntegerField(db_column='idStaffContactList', primary_key=True)  # Field name made lowercase.
    idstaff = models.ForeignKey('Tblstaffs', db_column='idStaff')  # Field name made lowercase.
    idcontact = models.ForeignKey(Tblcontacts, db_column='idContact')  # Field name made lowercase.
    enablestaffcontactlist = models.IntegerField(db_column='enableStaffContactList')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStaffContactLists'


class Tblstaffentrancereports(models.Model):
    idstaffentrancereport = models.BigIntegerField(db_column='idStaffEntranceReport', primary_key=True)  # Field name made lowercase.
    datetimestaffentrance = models.DateTimeField(db_column='dateTimeStaffEntrance')  # Field name made lowercase.
    datetimestaffexit = models.DateTimeField(db_column='dateTimeStaffExit', blank=True, null=True)  # Field name made lowercase.
    idstaff = models.ForeignKey('Tblstaffs', db_column='idStaff')  # Field name made lowercase.
    enablestaffentrancereport = models.IntegerField(db_column='enableStaffEntranceReport')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStaffEntranceReports'


class Tblstaffmedicalbackgroundlists(models.Model):
    idstaffmedicalbackgroundlist = models.BigIntegerField(db_column='idStaffMedicalBackGroundList', primary_key=True)  # Field name made lowercase.
    idstaff = models.ForeignKey('Tblstaffs', db_column='idStaff')  # Field name made lowercase.
    idmedicalbackground = models.ForeignKey(Tblmedicalbackgrounds, db_column='idMedicalBackground')  # Field name made lowercase.
    enablestaffmedicalbackgroundlist = models.IntegerField(db_column='enableStaffMedicalBackGroundList')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStaffMedicalBackGroundLists'


class Tblstaffmeetingschedules(models.Model):
    idstaffmeetingschedule = models.BigIntegerField(db_column='idStaffMeetingSchedule', primary_key=True)  # Field name made lowercase.
    idstaff = models.ForeignKey('Tblstaffs', db_column='idStaff')  # Field name made lowercase.
    datetimeinitstaffmeetingschedule = models.DateTimeField(db_column='dateTimeInitStaffMeetingSchedule')  # Field name made lowercase.
    datetimeendstaffmeetingschedule = models.DateTimeField(db_column='dateTimeEndStaffMeetingSchedule')  # Field name made lowercase.
    enablestaffmeetingschedule = models.IntegerField(db_column='enableStaffMeetingSchedule', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStaffMeetingSchedules'


class Tblstafftypes(models.Model):
    idstafftype = models.BigIntegerField(db_column='idStaffType', primary_key=True)  # Field name made lowercase.
    stafftype = models.CharField(db_column='staffType', max_length=45)  # Field name made lowercase.
    enablestafftype = models.IntegerField(db_column='enableStaffType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStaffTypes'


class Tblstaffs(models.Model):
    idstaff = models.BigIntegerField(db_column='idStaff', primary_key=True)  # Field name made lowercase.
    imagestaff = models.TextField(db_column='imageStaff', blank=True)  # Field name made lowercase.
    codestaff = models.CharField(db_column='codeStaff', max_length=45, blank=True)  # Field name made lowercase.
    firstnamestaff = models.CharField(db_column='firstNameStaff', max_length=45)  # Field name made lowercase.
    lastnamestaff = models.CharField(db_column='lastNameStaff', max_length=45)  # Field name made lowercase.
    birthdatestaff = models.CharField(db_column='birthDateStaff', max_length=45, blank=True)  # Field name made lowercase.
    emailstaff = models.CharField(db_column='emailStaff', max_length=45, blank=True)  # Field name made lowercase.
    idgenre = models.ForeignKey(Tblgenres, db_column='idGenre')  # Field name made lowercase.
    idbloodtype = models.ForeignKey(Tblbloodtypes, db_column='idBloodType')  # Field name made lowercase.
    identranceschedule = models.ForeignKey(Tblentranceschedules, db_column='idEntranceSchedule', blank=True, null=True)  # Field name made lowercase.
    idstafftype = models.ForeignKey(Tblstafftypes, db_column='idStaffType')  # Field name made lowercase.
    idlogin = models.ForeignKey(Tbllogin, db_column='idLogin', blank=True, null=True)  # Field name made lowercase.
    enablestaff = models.IntegerField(db_column='enableStaff')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStaffs'


class Tblstudentlists(models.Model):
    idstudentlist = models.BigIntegerField(db_column='idStudentList', primary_key=True)  # Field name made lowercase.
    idstudent = models.ForeignKey('Tblstudents', db_column='idStudent')  # Field name made lowercase.
    idgrade = models.ForeignKey(Tblgrades, db_column='idGrade')  # Field name made lowercase.
    idacademy = models.ForeignKey(Tblacademies, db_column='idAcademy')  # Field name made lowercase.
    enablestudentlist = models.IntegerField(db_column='enableStudentList')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStudentLists'


class Tblstudentmedicalbackgroundlists(models.Model):
    idstudentmedicalbackgroundlist = models.BigIntegerField(db_column='idStudentMedicalBackgroundList', primary_key=True)  # Field name made lowercase.
    idstudent = models.ForeignKey('Tblstudents', db_column='idStudent')  # Field name made lowercase.
    iddisease = models.ForeignKey(Tblmedicalbackgrounds, db_column='idDisease')  # Field name made lowercase.
    enablestudentmedicalbackgroundlist = models.IntegerField(db_column='enableStudentMedicalBackgroundList')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStudentMedicalBackgroundLists'


class Tblstudentreports(models.Model):
    idstudentreport = models.BigIntegerField(db_column='idStudentReport', primary_key=True)  # Field name made lowercase.
    idstudent = models.ForeignKey('Tblstudents', db_column='idStudent')  # Field name made lowercase.
    subjectstudentreport = models.CharField(db_column='subjectStudentReport', max_length=45, blank=True)  # Field name made lowercase.
    descriptionstudentreport = models.TextField(db_column='descriptionStudentReport', blank=True)  # Field name made lowercase.
    datetimesentreport = models.DateTimeField(db_column='dateTimeSentReport', blank=True, null=True)  # Field name made lowercase.
    checkedreport = models.IntegerField(db_column='checkedReport', blank=True, null=True)  # Field name made lowercase.
    datetimecheckedreport = models.DateTimeField(db_column='dateTimeCheckedReport', blank=True, null=True)  # Field name made lowercase.
    enablestudentreport = models.IntegerField(db_column='enableStudentReport')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStudentReports'


class Tblstudents(models.Model):
    idstudent = models.BigIntegerField(db_column='idStudent', primary_key=True)  # Field name made lowercase.
    imagestudent = models.TextField(db_column='imageStudent', blank=True)  # Field name made lowercase.
    codestudent = models.CharField(db_column='codeStudent', max_length=45, blank=True)  # Field name made lowercase.
    firstnamestudent = models.CharField(db_column='firstNameStudent', max_length=45)  # Field name made lowercase.
    lastnamestudent = models.CharField(db_column='lastNameStudent', max_length=45)  # Field name made lowercase.
    birthdatestudent = models.DateField(db_column='birthDateStudent')  # Field name made lowercase.
    emailstudent = models.CharField(db_column='emailStudent', max_length=45, blank=True)  # Field name made lowercase.
    idgenre = models.ForeignKey(Tblgenres, db_column='idGenre')  # Field name made lowercase.
    idbloodtype = models.ForeignKey(Tblbloodtypes, db_column='idBloodType')  # Field name made lowercase.
    idlogin = models.ForeignKey(Tbllogin, db_column='idLogin', blank=True, null=True)  # Field name made lowercase.
    enablestudent = models.IntegerField(db_column='enableStudent')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStudents'


class Tblstundentcontactlists(models.Model):
    idstundentcontactlist = models.BigIntegerField(db_column='idStundentContactList', primary_key=True)  # Field name made lowercase.
    idstudent = models.ForeignKey(Tblstudents, db_column='idStudent')  # Field name made lowercase.
    idcontact = models.ForeignKey(Tblcontacts, db_column='idContact')  # Field name made lowercase.
    enablestudentcontactlist = models.IntegerField(db_column='enableStudentContactList')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblStundentContactLists'


class Tbltasks(models.Model):
    idtask = models.BigIntegerField(db_column='idTask', primary_key=True)  # Field name made lowercase.
    idacademiccalendar = models.ForeignKey(Tblacademiccalendars, db_column='idAcademicCalendar', blank=True, null=True)  # Field name made lowercase.
    ponderationtask = models.FloatField(db_column='ponderationTask', blank=True, null=True)  # Field name made lowercase.
    delivereddate = models.DateTimeField(db_column='deliveredDate', blank=True, null=True)  # Field name made lowercase.
    checked = models.IntegerField(blank=True, null=True)
    teachercommentarytask = models.TextField(db_column='teacherCommentaryTask', blank=True)  # Field name made lowercase.
    filetask = models.TextField(db_column='fileTask', blank=True)  # Field name made lowercase.
    enabletask = models.IntegerField(db_column='enableTask')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblTasks'


class Tblunits(models.Model):
    idunit = models.BigIntegerField(db_column='idUnit', primary_key=True)  # Field name made lowercase.
    idcourse = models.ForeignKey(Tblcourses, db_column='idCourse')  # Field name made lowercase.
    idmodule = models.ForeignKey(Tblmodules, db_column='idModule')  # Field name made lowercase.
    enableunit = models.IntegerField(db_column='enableUnit')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUnits'


class Tblyears(models.Model):
    idyear = models.BigIntegerField(db_column='idYear', primary_key=True)  # Field name made lowercase.
    year = models.IntegerField()
    enableyear = models.IntegerField(db_column='enableYear')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblYears'

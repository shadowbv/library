#from __future__ import unicode_literals
from django.db import models


class ReaderCategory(models.Model):
    #id = models.IntegerField(db_column='ID', primary_key=True, auto_created=True)  # For Firebird
    id = models.AutoField(db_column='ID', primary_key=True, auto_created=True, verbose_name="id")
    name = models.CharField(db_column='NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    prefix = models.CharField(db_column='PREFIX', max_length=20, blank=True, null=True)  # Field name made lowercase.
    suffix = models.CharField(db_column='SUFFIX', max_length=20, blank=True, null=True)  # Field name made lowercase.
    digit_qty = models.SmallIntegerField(db_column='DIGIT_QTY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'READER_CATEGORY'
        ordering = ['id']
        verbose_name = "Категорія читача"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.name


class PhysicalPerson(models.Model):
    #id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    #id = models.IntegerField(db_column='ID', primary_key=True, auto_created=True)  #For Firebird
    id = models.AutoField(db_column='ID', primary_key=True, auto_created=True, verbose_name="id")
    name = models.CharField(db_column='NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    birth_date = models.DateTimeField(db_column='BIRTH_DATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    address = models.CharField(db_column='ADDRESS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    passport_series = models.CharField(db_column='PASSPORT_SERIES', max_length=10, blank=True, null=True)  # Field name made lowercase.
    passport_no = models.IntegerField(db_column='PASSPORT_NO', blank=True, null=True)  # Field name made lowercase.
    work_place = models.CharField(db_column='WORK_PLACE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    person_post = models.CharField(db_column='PERSON_POST', max_length=150, blank=True, null=True)  # Field name made lowercase.
    in_user = models.CharField(db_column='IN_USER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    work_phone = models.CharField(db_column='WORK_PHONE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    home_phone = models.CharField(db_column='HOME_PHONE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kod = models.DecimalField(db_column='KOD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    email = models.CharField(db_column='EMAIL', max_length=80, blank=True, null=True)  # Field name made lowercase.
    mobile_phone = models.CharField(db_column='MOBILE_PHONE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    pager_no = models.IntegerField(db_column='PAGER_NO', blank=True, null=True)  # Field name made lowercase.
    pager_phone = models.CharField(db_column='PAGER_PHONE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    photo_old = models.BinaryField(db_column='PHOTO_OLD', blank=True, null=True)  # Field name made lowercase.
    code_intno = models.IntegerField(db_column='CODE_INTNO', blank=True, null=True)  # Field name made lowercase.
    is_blocked = models.SmallIntegerField(db_column='IS_BLOCKED', blank=True, null=True)  # Field name made lowercase.
    block_reason = models.CharField(db_column='BLOCK_REASON', max_length=200, blank=True, null=True)  # Field name made lowercase.
    register_date = models.DateTimeField(db_column='REGISTER_DATE', auto_now_add=True)  # Field name made lowercase. This field type is a guess.
    #register_date = models.DateTimeField(db_column='REGISTER_DATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    in_date = models.DateTimeField(db_column='IN_DATE', auto_now_add=True)  # Field name made lowercase. This field type is a guess.
    #in_date = models.DateTimeField(db_column='IN_DATE', blank=True, null=True)
    last_edit_date = models.DateTimeField(db_column='LAST_EDIT_DATE', auto_now=True)  # Field name made lowercase. This field type is a guess.
    #last_edit_date = models.DateTimeField(db_column='LAST_EDIT_DATE', blank=True, null=True)
    last_edit_user = models.CharField(db_column='LAST_EDIT_USER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    spassport_no = models.CharField(db_column='SPASSPORT_NO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    pin_code = models.CharField(db_column='PIN_CODE', max_length=250, blank=True, null=True)  # Field name made lowercase.
    service_begdate = models.DateTimeField(db_column='SERVICE_BEGDATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    service_enddate = models.DateTimeField(db_column='SERVICE_ENDDATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    #category_id = models.IntegerField(db_column='CATEGORY_ID', blank=True, null=True)  # Field name made lowercase.
    category = models.ForeignKey(ReaderCategory)
    passport_org = models.CharField(db_column='PASSPORT_ORG', max_length=128, blank=True, null=True)  # Field name made lowercase.
    scomment = models.CharField(db_column='SCOMMENT', max_length=250, blank=True, null=True)  # Field name made lowercase.
    table_id = models.CharField(db_column='TABLE_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    block_edit_date = models.DateTimeField(db_column='BLOCK_EDIT_DATE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    block_edit_user = models.CharField(db_column='BLOCK_EDIT_USER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    person_status = models.CharField(db_column='PERSON_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    division = models.CharField(db_column='DIVISION', max_length=64, blank=True, null=True)  # Field name made lowercase.
    subdivision = models.CharField(db_column='SUBDIVISION', max_length=64, blank=True, null=True)  # Field name made lowercase.
    post_type = models.CharField(db_column='POST_TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    student_course = models.CharField(db_column='STUDENT_COURSE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    speciality = models.CharField(db_column='SPECIALITY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    specialization = models.CharField(db_column='SPECIALIZATION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    student_group = models.CharField(db_column='STUDENT_GROUP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    age_category = models.CharField(db_column='AGE_CATEGORY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    social_category = models.CharField(db_column='SOCIAL_CATEGORY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rfid = models.CharField(db_column='RFID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='BARCODE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    access_category = models.IntegerField(db_column='ACCESS_CATEGORY', blank=True, null=True)  # Field name made lowercase.
    person_password = models.CharField(db_column='PERSON_PASSWORD', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PHYSICAL_PERSON'
        ordering = ['-register_date']
        verbose_name = "Читачі"
        verbose_name_plural = "Читачі"

    def __str__(self):
        return self.name

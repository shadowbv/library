# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AccEldocs(models.Model):
    dt_acc = models.DateTimeField(db_column='DT_ACC')  # Field name made lowercase.
    doc_id = models.IntegerField(db_column='DOC_ID', blank=True, null=True)  # Field name made lowercase.
    r_kod = models.CharField(db_column='R_KOD', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACC_ELDOCS'


class AcquisitionTypes(models.Model):
    kod = models.IntegerField(db_column='KOD')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACQUISITION_TYPES'


class AnnotWordIndex(models.Model):
    doc_id = models.IntegerField(db_column='DOC_ID', blank=True, null=True)  # Field name made lowercase.
    word = models.CharField(db_column='WORD', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANNOT_WORD_INDEX'


class Authoritylist(models.Model):
    code = models.IntegerField(db_column='CODE')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    tablelist = models.CharField(db_column='TABLELIST', max_length=250, blank=True, null=True)  # Field name made lowercase.
    tablelist2 = models.CharField(db_column='TABLELIST2', max_length=250, blank=True, null=True)  # Field name made lowercase.
    authlist = models.CharField(db_column='AUTHLIST', max_length=250, blank=True, null=True)  # Field name made lowercase.
    norder = models.IntegerField(db_column='NORDER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUTHORITYLIST'


class AuthorList(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUTHOR_LIST'


class AuthorMarkList(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mark_order = models.IntegerField(db_column='MARK_ORDER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUTHOR_MARK_LIST'


class AuthorSynonym(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=50)  # Field name made lowercase.
    norder = models.SmallIntegerField(db_column='NORDER')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUTHOR_SYNONYM'


class AuthorWordIndex(models.Model):
    doc_id = models.IntegerField(db_column='DOC_ID')  # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUTHOR_WORD_INDEX'


class AuthTypeMain(models.Model):
    kod = models.IntegerField(db_column='KOD', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='STAT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUTH_TYPE_MAIN'


class BlockreasonList(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BLOCKREASON_LIST'


class Cards(models.Model):
    card_id = models.IntegerField(db_column='CARD_ID')  # Field name made lowercase.
    hier_id = models.IntegerField(db_column='HIER_ID', blank=True, null=True)  # Field name made lowercase.
    stype = models.CharField(db_column='STYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dt_creat = models.DateTimeField(db_column='DT_CREAT')  # Field name made lowercase.
    doc_count = models.SmallIntegerField(db_column='DOC_COUNT', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=230, blank=True, null=True)  # Field name made lowercase.
    topic_type = models.CharField(db_column='TOPIC_TYPE', max_length=250, blank=True, null=True)  # Field name made lowercase.
    sign = models.CharField(db_column='SIGN', max_length=250, blank=True, null=True)  # Field name made lowercase.
    first_part_name = models.CharField(db_column='FIRST_PART_NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    next_part_name = models.CharField(db_column='NEXT_PART_NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    full_initials = models.CharField(db_column='FULL_INITIALS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    add_part_name = models.CharField(db_column='ADD_PART_NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    other_part_name = models.CharField(db_column='OTHER_PART_NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    topic_dates = models.CharField(db_column='TOPIC_DATES', max_length=250, blank=True, null=True)  # Field name made lowercase.
    place = models.CharField(db_column='PLACE', max_length=250, blank=True, null=True)  # Field name made lowercase.
    affilation = models.CharField(db_column='AFFILATION', max_length=250, blank=True, null=True)  # Field name made lowercase.
    topic = models.CharField(db_column='TOPIC', max_length=250, blank=True, null=True)  # Field name made lowercase.
    geographical = models.CharField(db_column='GEOGRAPHICAL', max_length=250, blank=True, null=True)  # Field name made lowercase.
    chronological = models.CharField(db_column='CHRONOLOGICAL', max_length=250, blank=True, null=True)  # Field name made lowercase.
    topic_format = models.CharField(db_column='TOPIC_FORMAT', max_length=250, blank=True, null=True)  # Field name made lowercase.
    topic_comment = models.CharField(db_column='TOPIC_COMMENT', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CARDS'


class CityList(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=80, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FULLNAME', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CITY_LIST'


class ClientFiles(models.Model):
    filename = models.CharField(db_column='FILENAME', max_length=100)  # Field name made lowercase.
    filebin = models.TextField(db_column='FILEBIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIENT_FILES'


class CodeParsingList(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=48, blank=True, null=True)  # Field name made lowercase.
    separators = models.CharField(db_column='SEPARATORS', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CODE_PARSING_LIST'


class CodeParsingRules(models.Model):
    parsing_kod = models.SmallIntegerField(db_column='PARSING_KOD', blank=True, null=True)  # Field name made lowercase.
    norder = models.SmallIntegerField(db_column='NORDER', blank=True, null=True)  # Field name made lowercase.
    master_card = models.IntegerField(db_column='MASTER_CARD', blank=True, null=True)  # Field name made lowercase.
    beg_separator = models.CharField(db_column='BEG_SEPARATOR', max_length=5, blank=True, null=True)  # Field name made lowercase.
    end_separator = models.CharField(db_column='END_SEPARATOR', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CODE_PARSING_RULES'


class Colprofiles(models.Model):
    profile_kod = models.IntegerField(db_column='PROFILE_KOD')  # Field name made lowercase.
    win_kod = models.SmallIntegerField(db_column='WIN_KOD')  # Field name made lowercase.
    col_kod = models.IntegerField(db_column='COL_KOD')  # Field name made lowercase.
    col_w = models.DecimalField(db_column='COL_W', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    col_pos = models.SmallIntegerField(db_column='COL_POS', blank=True, null=True)  # Field name made lowercase.
    col_hidden = models.SmallIntegerField(db_column='COL_HIDDEN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COLPROFILES'


class Devices(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    path = models.CharField(db_column='PATH', max_length=80, blank=True, null=True)  # Field name made lowercase.
    save_style = models.SmallIntegerField(db_column='SAVE_STYLE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEVICES'


class DictionList(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=48, blank=True, null=True)  # Field name made lowercase.
    ntype = models.SmallIntegerField(db_column='NTYPE', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DICTION_LIST'


class DictionWord(models.Model):
    dic_kod = models.SmallIntegerField(db_column='DIC_KOD')  # Field name made lowercase.
    kod = models.IntegerField(db_column='KOD')  # Field name made lowercase.
    word = models.CharField(db_column='WORD', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DICTION_WORD'


class Discipline(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    cipher = models.CharField(db_column='CIPHER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    subname = models.CharField(db_column='SUBNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    scomment = models.CharField(db_column='SCOMMENT', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DISCIPLINE'


class DivisionList(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DIVISION_LIST'


class DocnameList(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOCNAME_LIST'


class Doctype(models.Model):
    code = models.SmallIntegerField(db_column='CODE')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    norder = models.SmallIntegerField(db_column='NORDER')  # Field name made lowercase.
    marccode = models.CharField(db_column='MARCCODE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    nlevel = models.IntegerField(db_column='NLEVEL', blank=True, null=True)  # Field name made lowercase.
    bibtype = models.IntegerField(db_column='BIBTYPE', blank=True, null=True)  # Field name made lowercase.
    default_child_link = models.IntegerField(db_column='DEFAULT_CHILD_LINK', blank=True, null=True)  # Field name made lowercase.
    default_child_type = models.IntegerField(db_column='DEFAULT_CHILD_TYPE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOCTYPE'


class DoctypeField(models.Model):
    doctype_kod = models.SmallIntegerField(db_column='DOCTYPE_KOD')  # Field name made lowercase.
    col_kod = models.SmallIntegerField(db_column='COL_KOD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOCTYPE_FIELD'


class Document(models.Model):
    doc_type = models.SmallIntegerField(db_column='DOC_TYPE')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    device_kod = models.SmallIntegerField(db_column='DEVICE_KOD', blank=True, null=True)  # Field name made lowercase.
    type_kod = models.SmallIntegerField(db_column='TYPE_KOD', blank=True, null=True)  # Field name made lowercase.
    publisher = models.CharField(db_column='PUBLISHER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reg_date = models.DateTimeField(db_column='REG_DATE')  # Field name made lowercase.
    publ_place = models.CharField(db_column='PUBL_PLACE', max_length=80, blank=True, null=True)  # Field name made lowercase.
    in_date = models.DateTimeField(db_column='IN_DATE')  # Field name made lowercase.
    long_filename = models.CharField(db_column='LONG_FILENAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    attr = models.SmallIntegerField(db_column='ATTR', blank=True, null=True)  # Field name made lowercase.
    doc_id = models.IntegerField(db_column='DOC_ID', primary_key=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FILENAME', max_length=245, blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=250, blank=True, null=True)  # Field name made lowercase.
    in_user = models.CharField(db_column='IN_USER', max_length=50)  # Field name made lowercase.
    last_edit_date = models.DateTimeField(db_column='LAST_EDIT_DATE')  # Field name made lowercase.
    last_edit_user = models.CharField(db_column='LAST_EDIT_USER', max_length=50)  # Field name made lowercase.
    item_qty = models.SmallIntegerField(db_column='ITEM_QTY')  # Field name made lowercase.
    item_present = models.SmallIntegerField(db_column='ITEM_PRESENT')  # Field name made lowercase.
    udk = models.CharField(db_column='UDK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=64, blank=True, null=True)  # Field name made lowercase.
    bbk = models.CharField(db_column='BBK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    author_mark = models.CharField(db_column='AUTHOR_MARK', max_length=20, blank=True, null=True)  # Field name made lowercase.
    issn = models.CharField(db_column='ISSN', max_length=32, blank=True, null=True)  # Field name made lowercase.
    lang = models.CharField(db_column='LANG', max_length=32, blank=True, null=True)  # Field name made lowercase.
    lang_kod = models.SmallIntegerField(db_column='LANG_KOD', blank=True, null=True)  # Field name made lowercase.
    cipher = models.CharField(db_column='CIPHER', max_length=32, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sizem = models.CharField(db_column='SIZEM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    annot1 = models.CharField(db_column='ANNOT1', max_length=254, blank=True, null=True)  # Field name made lowercase.
    annot2 = models.CharField(db_column='ANNOT2', max_length=254, blank=True, null=True)  # Field name made lowercase.
    annot3 = models.CharField(db_column='ANNOT3', max_length=254, blank=True, null=True)  # Field name made lowercase.
    annot4 = models.CharField(db_column='ANNOT4', max_length=254, blank=True, null=True)  # Field name made lowercase.
    cdlabel = models.CharField(db_column='CDLABEL', max_length=32, blank=True, null=True)  # Field name made lowercase.
    text_file = models.TextField(db_column='TEXT_FILE', blank=True, null=True)  # Field name made lowercase.
    group_kod = models.IntegerField(db_column='GROUP_KOD')  # Field name made lowercase.
    parent_id = models.IntegerField(db_column='PARENT_ID', blank=True, null=True)  # Field name made lowercase.
    is_parent = models.SmallIntegerField(db_column='IS_PARENT', blank=True, null=True)  # Field name made lowercase.
    author_type = models.SmallIntegerField(db_column='AUTHOR_TYPE', blank=True, null=True)  # Field name made lowercase.
    name_prefix = models.CharField(db_column='NAME_PREFIX', max_length=20, blank=True, null=True)  # Field name made lowercase.
    publ_year = models.CharField(db_column='PUBL_YEAR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parent_type = models.IntegerField(db_column='PARENT_TYPE', blank=True, null=True)  # Field name made lowercase.
    format_num = models.CharField(db_column='FORMAT_NUM', max_length=32, blank=True, null=True)  # Field name made lowercase.
    del_r_user = models.CharField(db_column='DEL_R_USER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    del_r_date = models.DateField(db_column='DEL_R_DATE', blank=True, null=True)  # Field name made lowercase.
    del_d_user = models.CharField(db_column='DEL_D_USER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    del_d_date = models.DateField(db_column='DEL_D_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOCUMENT'


class DocxfieldList(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=250)  # Field name made lowercase.
    stype = models.CharField(db_column='STYPE', max_length=10)  # Field name made lowercase.
    nlength = models.SmallIntegerField(db_column='NLENGTH', blank=True, null=True)  # Field name made lowercase.
    scale = models.SmallIntegerField(db_column='SCALE', blank=True, null=True)  # Field name made lowercase.
    superfield = models.SmallIntegerField(db_column='SUPERFIELD', blank=True, null=True)  # Field name made lowercase.
    useinquery = models.SmallIntegerField(db_column='USEINQUERY', blank=True, null=True)  # Field name made lowercase.
    useinsort = models.SmallIntegerField(db_column='USEINSORT', blank=True, null=True)  # Field name made lowercase.
    useinlist = models.SmallIntegerField(db_column='USEINLIST', blank=True, null=True)  # Field name made lowercase.
    norder = models.SmallIntegerField(db_column='NORDER', blank=True, null=True)  # Field name made lowercase.
    marctag = models.CharField(db_column='MARCTAG', max_length=3, blank=True, null=True)  # Field name made lowercase.
    marc_subfield = models.CharField(db_column='MARC_SUBFIELD', max_length=1, blank=True, null=True)  # Field name made lowercase.
    marcpos_start = models.SmallIntegerField(db_column='MARCPOS_START', blank=True, null=True)  # Field name made lowercase.
    marcpos_end = models.SmallIntegerField(db_column='MARCPOS_END', blank=True, null=True)  # Field name made lowercase.
    marc_multiple = models.CharField(db_column='MARC_MULTIPLE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    marc_codetbl = models.CharField(db_column='MARC_CODETBL', max_length=18, blank=True, null=True)  # Field name made lowercase.
    allowtextedit = models.SmallIntegerField(db_column='ALLOWTEXTEDIT', blank=True, null=True)  # Field name made lowercase.
    marc_indicators = models.CharField(db_column='MARC_INDICATORS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    marc_addfield = models.CharField(db_column='MARC_ADDFIELD', max_length=80, blank=True, null=True)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    separators = models.CharField(db_column='SEPARATORS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    area = models.SmallIntegerField(db_column='AREA', blank=True, null=True)  # Field name made lowercase.
    nno = models.SmallIntegerField(db_column='NNO', blank=True, null=True)  # Field name made lowercase.
    end_separator = models.CharField(db_column='END_SEPARATOR', max_length=5, blank=True, null=True)  # Field name made lowercase.
    unimarctag = models.CharField(db_column='UNIMARCTAG', max_length=3, blank=True, null=True)  # Field name made lowercase.
    unimarc_subfield = models.CharField(db_column='UNIMARC_SUBFIELD', max_length=1, blank=True, null=True)  # Field name made lowercase.
    unimarcpos_start = models.SmallIntegerField(db_column='UNIMARCPOS_START', blank=True, null=True)  # Field name made lowercase.
    unimarcpos_end = models.SmallIntegerField(db_column='UNIMARCPOS_END', blank=True, null=True)  # Field name made lowercase.
    unimarc_indicators = models.CharField(db_column='UNIMARC_INDICATORS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    unimarc_addfield = models.CharField(db_column='UNIMARC_ADDFIELD', max_length=80, blank=True, null=True)  # Field name made lowercase.
    unimarc_multiple = models.CharField(db_column='UNIMARC_MULTIPLE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    unimarc_codetbl = models.CharField(db_column='UNIMARC_CODETBL', max_length=18, blank=True, null=True)  # Field name made lowercase.
    uniallowtextedit = models.SmallIntegerField(db_column='UNIALLOWTEXTEDIT', blank=True, null=True)  # Field name made lowercase.
    author_level = models.SmallIntegerField(db_column='AUTHOR_LEVEL', blank=True, null=True)  # Field name made lowercase.
    colname = models.CharField(db_column='COLNAME', max_length=18, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOCXFIELD_LIST'


class DocxfieldValue(models.Model):
    doc_id = models.IntegerField(db_column='DOC_ID')  # Field name made lowercase.
    col002 = models.CharField(db_column='COL002', max_length=100, blank=True, null=True)  # Field name made lowercase.
    col003 = models.CharField(db_column='COL003', max_length=50, blank=True, null=True)  # Field name made lowercase.
    col004 = models.CharField(db_column='COL004', max_length=20, blank=True, null=True)  # Field name made lowercase.
    col006 = models.CharField(db_column='COL006', max_length=32, blank=True, null=True)  # Field name made lowercase.
    col007 = models.CharField(db_column='COL007', max_length=32, blank=True, null=True)  # Field name made lowercase.
    col008 = models.CharField(db_column='COL008', max_length=64, blank=True, null=True)  # Field name made lowercase.
    col010 = models.CharField(db_column='COL010', max_length=80, blank=True, null=True)  # Field name made lowercase.
    col011 = models.CharField(db_column='COL011', max_length=32, blank=True, null=True)  # Field name made lowercase.
    col012 = models.CharField(db_column='COL012', max_length=80, blank=True, null=True)  # Field name made lowercase.
    col013 = models.CharField(db_column='COL013', max_length=32, blank=True, null=True)  # Field name made lowercase.
    col014 = models.CharField(db_column='COL014', max_length=128, blank=True, null=True)  # Field name made lowercase.
    col016 = models.CharField(db_column='COL016', max_length=250, blank=True, null=True)  # Field name made lowercase.
    col017 = models.CharField(db_column='COL017', max_length=200, blank=True, null=True)  # Field name made lowercase.
    col018 = models.CharField(db_column='COL018', max_length=20, blank=True, null=True)  # Field name made lowercase.
    col019 = models.CharField(db_column='COL019', max_length=200, blank=True, null=True)  # Field name made lowercase.
    col020 = models.CharField(db_column='COL020', max_length=20, blank=True, null=True)  # Field name made lowercase.
    col021 = models.CharField(db_column='COL021', max_length=200, blank=True, null=True)  # Field name made lowercase.
    col022 = models.DateField(db_column='COL022', blank=True, null=True)  # Field name made lowercase.
    col023 = models.DateField(db_column='COL023', blank=True, null=True)  # Field name made lowercase.
    col024 = models.CharField(db_column='COL024', max_length=250, blank=True, null=True)  # Field name made lowercase.
    col025 = models.CharField(db_column='COL025', max_length=250, blank=True, null=True)  # Field name made lowercase.
    col026 = models.CharField(db_column='COL026', max_length=64, blank=True, null=True)  # Field name made lowercase.
    col027 = models.CharField(db_column='COL027', max_length=64, blank=True, null=True)  # Field name made lowercase.
    col028 = models.CharField(db_column='COL028', max_length=50, blank=True, null=True)  # Field name made lowercase.
    col029 = models.CharField(db_column='COL029', max_length=250, blank=True, null=True)  # Field name made lowercase.
    col030 = models.CharField(db_column='COL030', max_length=250, blank=True, null=True)  # Field name made lowercase.
    col031 = models.CharField(db_column='COL031', max_length=64, blank=True, null=True)  # Field name made lowercase.
    col033 = models.CharField(db_column='COL033', max_length=32, blank=True, null=True)  # Field name made lowercase.
    col035 = models.IntegerField(db_column='COL035', blank=True, null=True)  # Field name made lowercase.
    col036 = models.IntegerField(db_column='COL036', blank=True, null=True)  # Field name made lowercase.
    col037 = models.CharField(db_column='COL037', max_length=50, blank=True, null=True)  # Field name made lowercase.
    col038 = models.CharField(db_column='COL038', max_length=250, blank=True, null=True)  # Field name made lowercase.
    col039 = models.CharField(db_column='COL039', max_length=100, blank=True, null=True)  # Field name made lowercase.
    col040 = models.CharField(db_column='COL040', max_length=100, blank=True, null=True)  # Field name made lowercase.
    col041 = models.IntegerField(db_column='COL041', blank=True, null=True)  # Field name made lowercase.
    col043 = models.CharField(db_column='COL043', max_length=50, blank=True, null=True)  # Field name made lowercase.
    col044 = models.CharField(db_column='COL044', max_length=250, blank=True, null=True)  # Field name made lowercase.
    col045 = models.CharField(db_column='COL045', max_length=3, blank=True, null=True)  # Field name made lowercase.
    col046 = models.CharField(db_column='COL046', max_length=50, blank=True, null=True)  # Field name made lowercase.
    col047 = models.CharField(db_column='COL047', max_length=50, blank=True, null=True)  # Field name made lowercase.
    col048 = models.CharField(db_column='COL048', max_length=150, blank=True, null=True)  # Field name made lowercase.
    col049 = models.CharField(db_column='COL049', max_length=25, blank=True, null=True)  # Field name made lowercase.
    col051 = models.CharField(db_column='COL051', max_length=200, blank=True, null=True)  # Field name made lowercase.
    col052 = models.CharField(db_column='COL052', max_length=20, blank=True, null=True)  # Field name made lowercase.
    col054 = models.CharField(db_column='COL054', max_length=20, blank=True, null=True)  # Field name made lowercase.
    col055 = models.CharField(db_column='COL055', max_length=20, blank=True, null=True)  # Field name made lowercase.
    col056 = models.CharField(db_column='COL056', max_length=20, blank=True, null=True)  # Field name made lowercase.
    col057 = models.CharField(db_column='COL057', max_length=100, blank=True, null=True)  # Field name made lowercase.
    col059 = models.CharField(db_column='COL059', max_length=10, blank=True, null=True)  # Field name made lowercase.
    col060 = models.CharField(db_column='COL060', max_length=10, blank=True, null=True)  # Field name made lowercase.
    col061 = models.CharField(db_column='COL061', max_length=10, blank=True, null=True)  # Field name made lowercase.
    col062 = models.CharField(db_column='COL062', max_length=50, blank=True, null=True)  # Field name made lowercase.
    col064 = models.CharField(db_column='COL064', max_length=200, blank=True, null=True)  # Field name made lowercase.
    col065 = models.CharField(db_column='COL065', max_length=40, blank=True, null=True)  # Field name made lowercase.
    col067 = models.CharField(db_column='COL067', max_length=40, blank=True, null=True)  # Field name made lowercase.
    col068 = models.CharField(db_column='COL068', max_length=20, blank=True, null=True)  # Field name made lowercase.
    col069 = models.CharField(db_column='COL069', max_length=100, blank=True, null=True)  # Field name made lowercase.
    col070 = models.CharField(db_column='COL070', max_length=100, blank=True, null=True)  # Field name made lowercase.
    col072 = models.CharField(db_column='COL072', max_length=200, blank=True, null=True)  # Field name made lowercase.
    col073 = models.CharField(db_column='COL073', max_length=200, blank=True, null=True)  # Field name made lowercase.
    col074 = models.CharField(db_column='COL074', max_length=200, blank=True, null=True)  # Field name made lowercase.
    col075 = models.CharField(db_column='COL075', max_length=200, blank=True, null=True)  # Field name made lowercase.
    col077 = models.CharField(db_column='COL077', max_length=10, blank=True, null=True)  # Field name made lowercase.
    col078 = models.CharField(db_column='COL078', max_length=3, blank=True, null=True)  # Field name made lowercase.
    col079 = models.CharField(db_column='COL079', max_length=1, blank=True, null=True)  # Field name made lowercase.
    col080 = models.CharField(db_column='COL080', max_length=10, blank=True, null=True)  # Field name made lowercase.
    col081 = models.CharField(db_column='COL081', max_length=40, blank=True, null=True)  # Field name made lowercase.
    col082 = models.CharField(db_column='COL082', max_length=100, blank=True, null=True)  # Field name made lowercase.
    col083 = models.CharField(db_column='COL083', max_length=20, blank=True, null=True)  # Field name made lowercase.
    col084 = models.CharField(db_column='COL084', max_length=70, blank=True, null=True)  # Field name made lowercase.
    col086 = models.CharField(db_column='COL086', max_length=200, blank=True, null=True)  # Field name made lowercase.
    col087 = models.CharField(db_column='COL087', max_length=250, blank=True, null=True)  # Field name made lowercase.
    col088 = models.CharField(db_column='COL088', max_length=250, blank=True, null=True)  # Field name made lowercase.
    col089 = models.CharField(db_column='COL089', max_length=25, blank=True, null=True)  # Field name made lowercase.
    col090 = models.CharField(db_column='COL090', max_length=200, blank=True, null=True)  # Field name made lowercase.
    col091 = models.CharField(db_column='COL091', max_length=250, blank=True, null=True)  # Field name made lowercase.
    col092 = models.CharField(db_column='COL092', max_length=250, blank=True, null=True)  # Field name made lowercase.
    col093 = models.CharField(db_column='COL093', max_length=25, blank=True, null=True)  # Field name made lowercase.
    col094 = models.CharField(db_column='COL094', max_length=250, blank=True, null=True)  # Field name made lowercase.
    col095 = models.CharField(db_column='COL095', max_length=30, blank=True, null=True)  # Field name made lowercase.
    col097 = models.CharField(db_column='COL097', max_length=3, blank=True, null=True)  # Field name made lowercase.
    col098 = models.CharField(db_column='COL098', max_length=200, blank=True, null=True)  # Field name made lowercase.
    col099 = models.CharField(db_column='COL099', max_length=250, blank=True, null=True)  # Field name made lowercase.
    col101 = models.CharField(db_column='COL101', max_length=1, blank=True, null=True)  # Field name made lowercase.
    col102 = models.CharField(db_column='COL102', max_length=1, blank=True, null=True)  # Field name made lowercase.
    col103 = models.CharField(db_column='COL103', max_length=1, blank=True, null=True)  # Field name made lowercase.
    col104 = models.CharField(db_column='COL104', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOCXFIELD_VALUE'


class DocAgentIndex(models.Model):
    doc_id = models.IntegerField(db_column='DOC_ID', blank=True, null=True)  # Field name made lowercase.
    record_header = models.CharField(db_column='RECORD_HEADER', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOC_AGENT_INDEX'


class DocAnnotation(models.Model):
    doc_id = models.IntegerField(db_column='DOC_ID', blank=True, null=True)  # Field name made lowercase.
    norder = models.SmallIntegerField(db_column='NORDER', blank=True, null=True)  # Field name made lowercase.
    fragment = models.CharField(db_column='FRAGMENT', max_length=251, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOC_ANNOTATION'


class DocDscp(models.Model):
    doc_id = models.IntegerField(db_column='DOC_ID', blank=True, null=True)  # Field name made lowercase.
    dscp_id = models.IntegerField(db_column='DSCP_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOC_DSCP'


class DocItem(models.Model):
    doc_id = models.IntegerField(db_column='DOC_ID')  # Field name made lowercase.
    item_id = models.IntegerField(db_column='ITEM_ID')  # Field name made lowercase.
    item_no = models.CharField(db_column='ITEM_NO', max_length=32, blank=True, null=True)  # Field name made lowercase.
    reg_date = models.DateTimeField(db_column='REG_DATE')  # Field name made lowercase.
    commentt = models.CharField(db_column='COMMENTT', max_length=128, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    delivered = models.SmallIntegerField(db_column='DELIVERED', blank=True, null=True)  # Field name made lowercase.
    device_kod = models.SmallIntegerField(db_column='DEVICE_KOD', blank=True, null=True)  # Field name made lowercase.
    party_kod = models.IntegerField(db_column='PARTY_KOD', blank=True, null=True)  # Field name made lowercase.
    party_no = models.CharField(db_column='PARTY_NO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    act_kod = models.IntegerField(db_column='ACT_KOD', blank=True, null=True)  # Field name made lowercase.
    act_no = models.CharField(db_column='ACT_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    out_reason = models.SmallIntegerField(db_column='OUT_REASON', blank=True, null=True)  # Field name made lowercase.
    qtyall = models.SmallIntegerField(db_column='QTYALL', blank=True, null=True)  # Field name made lowercase.
    qtyact = models.SmallIntegerField(db_column='QTYACT', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='PRICE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    price_unit = models.SmallIntegerField(db_column='PRICE_UNIT', blank=True, null=True)  # Field name made lowercase.
    stock_kod = models.SmallIntegerField(db_column='STOCK_KOD', blank=True, null=True)  # Field name made lowercase.
    nobalance = models.SmallIntegerField(db_column='NOBALANCE', blank=True, null=True)  # Field name made lowercase.
    item_number = models.CharField(db_column='ITEM_NUMBER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    item_intno = models.IntegerField(db_column='ITEM_INTNO', blank=True, null=True)  # Field name made lowercase.
    item_mainno = models.CharField(db_column='ITEM_MAINNO', max_length=32, blank=True, null=True)  # Field name made lowercase.
    device_date = models.DateTimeField(db_column='DEVICE_DATE')  # Field name made lowercase.
    device_user = models.CharField(db_column='DEVICE_USER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    device_prev = models.IntegerField(db_column='DEVICE_PREV', blank=True, null=True)  # Field name made lowercase.
    last_edit_date = models.DateTimeField(db_column='LAST_EDIT_DATE')  # Field name made lowercase.
    last_edit_user = models.CharField(db_column='LAST_EDIT_USER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    distribution_kod = models.SmallIntegerField(db_column='DISTRIBUTION_KOD', blank=True, null=True)  # Field name made lowercase.
    rfid = models.CharField(db_column='RFID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='BARCODE', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOC_ITEM'


class DocLongfield(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    fld_type = models.SmallIntegerField(db_column='FLD_TYPE')  # Field name made lowercase.
    norder = models.IntegerField(db_column='NORDER')  # Field name made lowercase.
    fragment01 = models.CharField(db_column='FRAGMENT01', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment02 = models.CharField(db_column='FRAGMENT02', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment03 = models.CharField(db_column='FRAGMENT03', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment04 = models.CharField(db_column='FRAGMENT04', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment05 = models.CharField(db_column='FRAGMENT05', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment06 = models.CharField(db_column='FRAGMENT06', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment07 = models.CharField(db_column='FRAGMENT07', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment08 = models.CharField(db_column='FRAGMENT08', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOC_LONGFIELD'


class DocNumeration(models.Model):
    doc_id = models.IntegerField(db_column='DOC_ID')  # Field name made lowercase.
    numeration = models.TextField(db_column='NUMERATION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOC_NUMERATION'


class DocOtherfield(models.Model):
    doc_id = models.IntegerField(db_column='DOC_ID')  # Field name made lowercase.
    fields = models.TextField(db_column='FIELDS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOC_OTHERFIELD'


class DocOtherfieldLst(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    usmarc_tag = models.CharField(db_column='USMARC_TAG', max_length=10, blank=True, null=True)  # Field name made lowercase.
    unimarc_tag = models.CharField(db_column='UNIMARC_TAG', max_length=10, blank=True, null=True)  # Field name made lowercase.
    commentt = models.CharField(db_column='COMMENTT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    usmarc_ind = models.CharField(db_column='USMARC_IND', max_length=2, blank=True, null=True)  # Field name made lowercase.
    unimarc_ind = models.CharField(db_column='UNIMARC_IND', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOC_OTHERFIELD_LST'


class DocPresence(models.Model):
    doc_id = models.IntegerField(db_column='DOC_ID')  # Field name made lowercase.
    doc_owner = models.CharField(db_column='DOC_OWNER', max_length=32)  # Field name made lowercase.
    scomment = models.CharField(db_column='SCOMMENT', max_length=250, blank=True, null=True)  # Field name made lowercase.
    actual_date = models.DateTimeField(db_column='ACTUAL_DATE')  # Field name made lowercase.
    numeration = models.TextField(db_column='NUMERATION', blank=True, null=True)  # Field name made lowercase.
    item_qty = models.IntegerField(db_column='ITEM_QTY', blank=True, null=True)  # Field name made lowercase.
    stock_item_qty = models.IntegerField(db_column='STOCK_ITEM_QTY', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='PRICE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOC_PRESENCE'


class DocPresenceNum(models.Model):
    doc_id = models.IntegerField(db_column='DOC_ID')  # Field name made lowercase.
    doc_owner = models.CharField(db_column='DOC_OWNER', max_length=32)  # Field name made lowercase.
    norder = models.IntegerField(db_column='NORDER')  # Field name made lowercase.
    fragment01 = models.CharField(db_column='FRAGMENT01', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment02 = models.CharField(db_column='FRAGMENT02', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment03 = models.CharField(db_column='FRAGMENT03', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment04 = models.CharField(db_column='FRAGMENT04', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment05 = models.CharField(db_column='FRAGMENT05', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment06 = models.CharField(db_column='FRAGMENT06', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment07 = models.CharField(db_column='FRAGMENT07', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment08 = models.CharField(db_column='FRAGMENT08', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOC_PRESENCE_NUM'


class DocRequest(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    doc_id = models.IntegerField(db_column='DOC_ID', blank=True, null=True)  # Field name made lowercase.
    date_req = models.DateTimeField(db_column='DATE_REQ')  # Field name made lowercase.
    order_name = models.CharField(db_column='ORDER_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    qty = models.SmallIntegerField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.
    priority_no = models.SmallIntegerField(db_column='PRIORITY_NO', blank=True, null=True)  # Field name made lowercase.
    req_status = models.SmallIntegerField(db_column='REQ_STATUS', blank=True, null=True)  # Field name made lowercase.
    commentt = models.CharField(db_column='COMMENTT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    division_kod = models.SmallIntegerField(db_column='DIVISION_KOD', blank=True, null=True)  # Field name made lowercase.
    subdivision_kod = models.SmallIntegerField(db_column='SUBDIVISION_KOD', blank=True, null=True)  # Field name made lowercase.
    speciality_kod = models.SmallIntegerField(db_column='SPECIALITY_KOD', blank=True, null=True)  # Field name made lowercase.
    accepted = models.IntegerField(db_column='ACCEPTED', blank=True, null=True)  # Field name made lowercase.
    device_kod = models.IntegerField(db_column='DEVICE_KOD', blank=True, null=True)  # Field name made lowercase.
    dscp_id = models.IntegerField(db_column='DSCP_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOC_REQUEST'


class DscpTopic(models.Model):
    dscp_id = models.IntegerField(db_column='DSCP_ID')  # Field name made lowercase.
    topic_type = models.CharField(db_column='TOPIC_TYPE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    topic_value = models.CharField(db_column='TOPIC_VALUE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DSCP_TOPIC'


class ExtqueryBody(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    fld_type = models.SmallIntegerField(db_column='FLD_TYPE')  # Field name made lowercase.
    norder = models.IntegerField(db_column='NORDER')  # Field name made lowercase.
    fragment01 = models.CharField(db_column='FRAGMENT01', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment02 = models.CharField(db_column='FRAGMENT02', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment03 = models.CharField(db_column='FRAGMENT03', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment04 = models.CharField(db_column='FRAGMENT04', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment05 = models.CharField(db_column='FRAGMENT05', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment06 = models.CharField(db_column='FRAGMENT06', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment07 = models.CharField(db_column='FRAGMENT07', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment08 = models.CharField(db_column='FRAGMENT08', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EXTQUERY_BODY'


class GeneralXmlTree(models.Model):
    tree_id = models.CharField(db_column='TREE_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    node_level = models.SmallIntegerField(db_column='NODE_LEVEL', blank=True, null=True)  # Field name made lowercase.
    is_attribute = models.SmallIntegerField(db_column='IS_ATTRIBUTE', blank=True, null=True)  # Field name made lowercase.
    node_name = models.CharField(db_column='NODE_NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    node_value = models.CharField(db_column='NODE_VALUE', max_length=250, blank=True, null=True)  # Field name made lowercase.
    part_number = models.SmallIntegerField(db_column='PART_NUMBER', blank=True, null=True)  # Field name made lowercase.
    suffix_size = models.SmallIntegerField(db_column='SUFFIX_SIZE', blank=True, null=True)  # Field name made lowercase.
    node_order = models.SmallIntegerField(db_column='NODE_ORDER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GENERAL_XML_TREE'


class Genprofiles(models.Model):
    suser_name = models.CharField(db_column='SUSER_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    section_name = models.CharField(db_column='SECTION_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    item_name = models.CharField(db_column='ITEM_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    svalue = models.CharField(db_column='SVALUE', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GENPROFILES'


class Groupauthority(models.Model):
    groupcode = models.IntegerField(db_column='GROUPCODE')  # Field name made lowercase.
    authcode = models.IntegerField(db_column='AUTHCODE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GROUPAUTHORITY'


class Grouplist(models.Model):
    code = models.IntegerField(db_column='CODE')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GROUPLIST'


class IndexedField(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    ntype = models.SmallIntegerField(db_column='NTYPE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INDEXED_FIELD'


class InventBook(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    item_sort_list = models.CharField(db_column='ITEM_SORT_LIST', max_length=64, blank=True, null=True)  # Field name made lowercase.
    doctype_list = models.CharField(db_column='DOCTYPE_LIST', max_length=64, blank=True, null=True)  # Field name made lowercase.
    flags = models.IntegerField(db_column='FLAGS', blank=True, null=True)  # Field name made lowercase.
    no_from = models.IntegerField(db_column='NO_FROM', blank=True, null=True)  # Field name made lowercase.
    no_to = models.IntegerField(db_column='NO_TO', blank=True, null=True)  # Field name made lowercase.
    date_from = models.DateTimeField(db_column='DATE_FROM')  # Field name made lowercase.
    date_to = models.DateTimeField(db_column='DATE_TO')  # Field name made lowercase.
    no_prefix = models.CharField(db_column='NO_PREFIX', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cur_no = models.IntegerField(db_column='CUR_NO', blank=True, null=True)  # Field name made lowercase.
    no_length = models.SmallIntegerField(db_column='NO_LENGTH', blank=True, null=True)  # Field name made lowercase.
    no_suffix = models.CharField(db_column='NO_SUFFIX', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVENT_BOOK'


class Item(models.Model):
    item_intno = models.IntegerField(db_column='ITEM_INTNO', primary_key=True)  # Field name made lowercase.
    doc_id = models.IntegerField(db_column='DOC_ID')  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=50)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    inv_date = models.DateTimeField(db_column='INV_DATE')  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=25)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITEM'


class ItemAddition(models.Model):
    doc_id = models.IntegerField(db_column='DOC_ID')  # Field name made lowercase.
    device_kod = models.IntegerField(db_column='DEVICE_KOD', blank=True, null=True)  # Field name made lowercase.
    oncreate_qty = models.IntegerField(db_column='ONCREATE_QTY', blank=True, null=True)  # Field name made lowercase.
    accepted_qty = models.IntegerField(db_column='ACCEPTED_QTY', blank=True, null=True)  # Field name made lowercase.
    last_edit_date = models.DateTimeField(db_column='LAST_EDIT_DATE')  # Field name made lowercase.
    last_edit_user = models.CharField(db_column='LAST_EDIT_USER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pass_qty = models.IntegerField(db_column='PASS_QTY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITEM_ADDITION'


class ItemOutreason(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    item_id = models.IntegerField(db_column='ITEM_ID', blank=True, null=True)  # Field name made lowercase.
    out_reason = models.SmallIntegerField(db_column='OUT_REASON', blank=True, null=True)  # Field name made lowercase.
    out_qty = models.SmallIntegerField(db_column='OUT_QTY', blank=True, null=True)  # Field name made lowercase.
    act_kod = models.IntegerField(db_column='ACT_KOD', blank=True, null=True)  # Field name made lowercase.
    act_no = models.CharField(db_column='ACT_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITEM_OUTREASON'


class JuridicalPerson(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    phone1 = models.CharField(db_column='PHONE1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    kod = models.IntegerField(db_column='KOD', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=254, blank=True, null=True)  # Field name made lowercase.
    phone2 = models.CharField(db_column='PHONE2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='FAX', max_length=32, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=64, blank=True, null=True)  # Field name made lowercase.
    chief_name = models.CharField(db_column='CHIEF_NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    chief_post = models.CharField(db_column='CHIEF_POST', max_length=32, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    in_user = models.CharField(db_column='IN_USER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=80, blank=True, null=True)  # Field name made lowercase.
    supplier = models.CharField(db_column='SUPPLIER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    in_date = models.DateTimeField(db_column='IN_DATE')  # Field name made lowercase.
    last_edit_date = models.DateTimeField(db_column='LAST_EDIT_DATE')  # Field name made lowercase.
    last_edit_user = models.CharField(db_column='LAST_EDIT_USER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ispartner = models.IntegerField(db_column='ISPARTNER', blank=True, null=True)  # Field name made lowercase.
    iscomposite = models.IntegerField(db_column='ISCOMPOSITE', blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JURIDICAL_PERSON'


class KatDoc(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=48, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='STAT', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KAT_DOC'


class KnowledgeT(models.Model):
    kod = models.IntegerField(db_column='KOD', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='STAT', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KNOWLEDGE_T'


class Languages(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='STAT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    used = models.SmallIntegerField(db_column='USED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LANGUAGES'


class Licence(models.Model):
    licenceno = models.CharField(db_column='LICENCENO', max_length=50)  # Field name made lowercase.
    userqty = models.SmallIntegerField(db_column='USERQTY')  # Field name made lowercase.
    maxdate = models.DateTimeField(db_column='MAXDATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LICENCE'


class LicenceInfo(models.Model):
    licence_type = models.CharField(db_column='LICENCE_TYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    licence_no = models.CharField(db_column='LICENCE_NO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    user_qty = models.IntegerField(db_column='USER_QTY', blank=True, null=True)  # Field name made lowercase.
    max_date = models.DateField(db_column='MAX_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LICENCE_INFO'


class MarcsysCountry(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=60, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='STAT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    used = models.SmallIntegerField(db_column='USED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MARCSYS_COUNTRY'


class MarcsysForm(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=48, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='STAT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    unimarc_code = models.CharField(db_column='UNIMARC_CODE', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MARCSYS_FORM'


class MarcsysRelator(models.Model):
    code = models.CharField(db_column='CODE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='STAT', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MARCSYS_RELATOR'


class MarcDocdesc(models.Model):
    code = models.CharField(db_column='CODE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MARC_DOCDESC'


class MarcDoclevel(models.Model):
    code = models.CharField(db_column='CODE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    unimarc_code = models.CharField(db_column='UNIMARC_CODE', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MARC_DOCLEVEL'


class MarcDoctype(models.Model):
    code = models.CharField(db_column='CODE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=48, blank=True, null=True)  # Field name made lowercase.
    unimarc_code = models.CharField(db_column='UNIMARC_CODE', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MARC_DOCTYPE'


class MassAction(models.Model):
    action_id = models.IntegerField(db_column='ACTION_ID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    organisation = models.CharField(db_column='ORGANISATION', max_length=250, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='DEPARTMENT', max_length=250, blank=True, null=True)  # Field name made lowercase.
    action_date = models.DateField(db_column='ACTION_DATE', blank=True, null=True)  # Field name made lowercase.
    place = models.CharField(db_column='PLACE', max_length=250, blank=True, null=True)  # Field name made lowercase.
    qty = models.IntegerField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.
    action_result = models.CharField(db_column='ACTION_RESULT', max_length=250, blank=True, null=True)  # Field name made lowercase.
    action_comment = models.CharField(db_column='ACTION_COMMENT', max_length=250, blank=True, null=True)  # Field name made lowercase.
    in_user = models.CharField(db_column='IN_USER', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MASS_ACTION'


class MasterCards(models.Model):
    master_id = models.IntegerField(db_column='MASTER_ID', blank=True, null=True)  # Field name made lowercase.
    group_kod = models.IntegerField(db_column='GROUP_KOD', blank=True, null=True)  # Field name made lowercase.
    hier_id = models.IntegerField(db_column='HIER_ID', blank=True, null=True)  # Field name made lowercase.
    access_type = models.SmallIntegerField(db_column='ACCESS_TYPE', blank=True, null=True)  # Field name made lowercase.
    hier_type = models.SmallIntegerField(db_column='HIER_TYPE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MASTER_CARDS'


class MatAudio(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=48, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='STAT', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MAT_AUDIO'


class MatElDoc(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=48, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='STAT', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MAT_EL_DOC'


class MatVideo(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=48, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='STAT', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MAT_VIDEO'


class Maxes(models.Model):
    jur_person_id = models.IntegerField(db_column='JUR_PERSON_ID', blank=True, null=True)  # Field name made lowercase.
    phys_person_id = models.IntegerField(db_column='PHYS_PERSON_ID', blank=True, null=True)  # Field name made lowercase.
    doc_id = models.IntegerField(db_column='DOC_ID', blank=True, null=True)  # Field name made lowercase.
    card_id = models.IntegerField(db_column='CARD_ID', blank=True, null=True)  # Field name made lowercase.
    item_id = models.IntegerField(db_column='ITEM_ID', blank=True, null=True)  # Field name made lowercase.
    colcnt = models.IntegerField(db_column='COLCNT', blank=True, null=True)  # Field name made lowercase.
    grpcnt = models.IntegerField(db_column='GRPCNT', blank=True, null=True)  # Field name made lowercase.
    party_kod = models.IntegerField(db_column='PARTY_KOD', blank=True, null=True)  # Field name made lowercase.
    request_id = models.IntegerField(db_column='REQUEST_ID', blank=True, null=True)  # Field name made lowercase.
    org_order_id = models.IntegerField(db_column='ORG_ORDER_ID', blank=True, null=True)  # Field name made lowercase.
    item_outreason_id = models.IntegerField(db_column='ITEM_OUTREASON_ID', blank=True, null=True)  # Field name made lowercase.
    deliver_id = models.IntegerField(db_column='DELIVER_ID', blank=True, null=True)  # Field name made lowercase.
    profile_kod = models.IntegerField(db_column='PROFILE_KOD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MAXES'


class Maxes2(models.Model):
    code = models.CharField(db_column='CODE', max_length=20)  # Field name made lowercase.
    max_value = models.IntegerField(db_column='MAX_VALUE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MAXES2'


class Miscprofiles(models.Model):
    profile_kod = models.IntegerField(db_column='PROFILE_KOD', blank=True, null=True)  # Field name made lowercase.
    win_kod = models.SmallIntegerField(db_column='WIN_KOD', blank=True, null=True)  # Field name made lowercase.
    item_name = models.CharField(db_column='ITEM_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    svalue = models.CharField(db_column='SVALUE', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MISCPROFILES'


class MoneyUnit(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    cent_short_name = models.CharField(db_column='CENT_SHORT_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cent_name = models.CharField(db_column='CENT_NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MONEY_UNIT'


class NameList(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    ntype = models.SmallIntegerField(db_column='NTYPE', blank=True, null=True)  # Field name made lowercase.
    person_post = models.CharField(db_column='PERSON_POST', max_length=250, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NAME_LIST'


class Options(models.Model):
    term_days = models.SmallIntegerField(db_column='TERM_DAYS', blank=True, null=True)  # Field name made lowercase.
    term_days_jur = models.SmallIntegerField(db_column='TERM_DAYS_JUR', blank=True, null=True)  # Field name made lowercase.
    dbversion = models.SmallIntegerField(db_column='DBVERSION', blank=True, null=True)  # Field name made lowercase.
    am_short = models.SmallIntegerField(db_column='AM_SHORT', blank=True, null=True)  # Field name made lowercase.
    def_unit = models.SmallIntegerField(db_column='DEF_UNIT', blank=True, null=True)  # Field name made lowercase.
    upd = models.SmallIntegerField(db_column='UPD', blank=True, null=True)  # Field name made lowercase.
    items_no_integer = models.SmallIntegerField(db_column='ITEMS_NO_INTEGER', blank=True, null=True)  # Field name made lowercase.
    money_name = models.CharField(db_column='MONEY_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cent_name = models.CharField(db_column='CENT_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    items_dashed = models.SmallIntegerField(db_column='ITEMS_DASHED', blank=True, null=True)  # Field name made lowercase.
    items_unique = models.SmallIntegerField(db_column='ITEMS_UNIQUE', blank=True, null=True)  # Field name made lowercase.
    udk_hier = models.IntegerField(db_column='UDK_HIER', blank=True, null=True)  # Field name made lowercase.
    udk_separator = models.CharField(db_column='UDK_SEPARATOR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    libcipher = models.CharField(db_column='LIBCIPHER', max_length=32, blank=True, null=True)  # Field name made lowercase.
    libname = models.CharField(db_column='LIBNAME', max_length=254, blank=True, null=True)  # Field name made lowercase.
    use_presence_imp = models.SmallIntegerField(db_column='USE_PRESENCE_IMP', blank=True, null=True)  # Field name made lowercase.
    use_presence_exp = models.SmallIntegerField(db_column='USE_PRESENCE_EXP', blank=True, null=True)  # Field name made lowercase.
    itemno_separator = models.CharField(db_column='ITEMNO_SEPARATOR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    formular_text = models.CharField(db_column='FORMULAR_TEXT', max_length=250, blank=True, null=True)  # Field name made lowercase.
    max_resultset = models.IntegerField(db_column='MAX_RESULTSET', blank=True, null=True)  # Field name made lowercase.
    clnt_ver = models.IntegerField(db_column='CLNT_VER', blank=True, null=True)  # Field name made lowercase.
    clnt_red = models.IntegerField(db_column='CLNT_RED', blank=True, null=True)  # Field name made lowercase.
    clnt_mod = models.IntegerField(db_column='CLNT_MOD', blank=True, null=True)  # Field name made lowercase.
    check_ret_place = models.IntegerField(db_column='CHECK_RET_PLACE', blank=True, null=True)  # Field name made lowercase.
    use_partyno = models.SmallIntegerField(db_column='USE_PARTYNO', blank=True, null=True)  # Field name made lowercase.
    division_colname = models.CharField(db_column='DIVISION_COLNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    subdiv_colname = models.CharField(db_column='SUBDIV_COLNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dscp_name = models.CharField(db_column='DSCP_NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    exchange_fond = models.IntegerField(db_column='EXCHANGE_FOND', blank=True, null=True)  # Field name made lowercase.
    confirm_getting = models.IntegerField(db_column='CONFIRM_GETTING', blank=True, null=True)  # Field name made lowercase.
    order_to_queue = models.SmallIntegerField(db_column='ORDER_TO_QUEUE', blank=True, null=True)  # Field name made lowercase.
    min_clnt_ver = models.IntegerField(db_column='MIN_CLNT_VER', blank=True, null=True)  # Field name made lowercase.
    min_clnt_red = models.IntegerField(db_column='MIN_CLNT_RED', blank=True, null=True)  # Field name made lowercase.
    min_clnt_mod = models.IntegerField(db_column='MIN_CLNT_MOD', blank=True, null=True)  # Field name made lowercase.
    confirm_docgetting = models.IntegerField(db_column='CONFIRM_DOCGETTING', blank=True, null=True)  # Field name made lowercase.
    summary_start_date = models.DateField(db_column='SUMMARY_START_DATE', blank=True, null=True)  # Field name made lowercase.
    confirm_docorder = models.SmallIntegerField(db_column='CONFIRM_DOCORDER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OPTIONS'


class Options2(models.Model):
    option_id = models.CharField(db_column='OPTION_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    option_value = models.CharField(db_column='OPTION_VALUE', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OPTIONS2'


class Orders(models.Model):
    person_id = models.IntegerField(db_column='PERSON_ID', blank=True, null=True)  # Field name made lowercase.
    person_type = models.CharField(db_column='PERSON_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    doc_id = models.IntegerField(db_column='DOC_ID', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    item_id = models.IntegerField(db_column='ITEM_ID', blank=True, null=True)  # Field name made lowercase.
    item_no = models.CharField(db_column='ITEM_NO', max_length=32, blank=True, null=True)  # Field name made lowercase.
    place_date = models.DateTimeField(db_column='PLACE_DATE')  # Field name made lowercase.
    device_kod = models.SmallIntegerField(db_column='DEVICE_KOD', blank=True, null=True)  # Field name made lowercase.
    deliver_kod = models.SmallIntegerField(db_column='DELIVER_KOD', blank=True, null=True)  # Field name made lowercase.
    last_edit_user = models.CharField(db_column='LAST_EDIT_USER', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ORDERS'


class OrderChain(models.Model):
    deliver_kod = models.SmallIntegerField(db_column='DELIVER_KOD', blank=True, null=True)  # Field name made lowercase.
    norder = models.SmallIntegerField(db_column='NORDER', blank=True, null=True)  # Field name made lowercase.
    device_kod = models.SmallIntegerField(db_column='DEVICE_KOD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ORDER_CHAIN'


class OrgOrder(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    doc_id = models.IntegerField(db_column='DOC_ID', blank=True, null=True)  # Field name made lowercase.
    qty = models.SmallIntegerField(db_column='QTY', blank=True, null=True)  # Field name made lowercase.
    org_id = models.IntegerField(db_column='ORG_ID', blank=True, null=True)  # Field name made lowercase.
    date_place = models.DateTimeField(db_column='DATE_PLACE')  # Field name made lowercase.
    date_must = models.DateTimeField(db_column='DATE_MUST')  # Field name made lowercase.
    date_receive = models.DateTimeField(db_column='DATE_RECEIVE')  # Field name made lowercase.
    commentt = models.CharField(db_column='COMMENTT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ord_status = models.SmallIntegerField(db_column='ORD_STATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ORG_ORDER'


class OutReasons(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    par_kod = models.SmallIntegerField(db_column='PAR_KOD', blank=True, null=True)  # Field name made lowercase.
    norder = models.SmallIntegerField(db_column='NORDER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OUT_REASONS'


class Party(models.Model):
    kod = models.IntegerField(db_column='KOD')  # Field name made lowercase.
    party_no = models.CharField(db_column='PARTY_NO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    in_date = models.DateTimeField(db_column='IN_DATE')  # Field name made lowercase.
    stype = models.CharField(db_column='STYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    source_id = models.IntegerField(db_column='SOURCE_ID', blank=True, null=True)  # Field name made lowercase.
    source_name = models.CharField(db_column='SOURCE_NAME', max_length=254, blank=True, null=True)  # Field name made lowercase.
    accompany_doc_date = models.DateTimeField(db_column='ACCOMPANY_DOC_DATE')  # Field name made lowercase.
    accompany_doc_no = models.CharField(db_column='ACCOMPANY_DOC_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    commnt = models.CharField(db_column='COMMNT', max_length=250, blank=True, null=True)  # Field name made lowercase.
    director_post = models.CharField(db_column='DIRECTOR_POST', max_length=250, blank=True, null=True)  # Field name made lowercase.
    director_name = models.CharField(db_column='DIRECTOR_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    signer1_post = models.CharField(db_column='SIGNER1_POST', max_length=250, blank=True, null=True)  # Field name made lowercase.
    signer1_name = models.CharField(db_column='SIGNER1_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    signer2_post = models.CharField(db_column='SIGNER2_POST', max_length=250, blank=True, null=True)  # Field name made lowercase.
    signer2_name = models.CharField(db_column='SIGNER2_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    signer3_post = models.CharField(db_column='SIGNER3_POST', max_length=250, blank=True, null=True)  # Field name made lowercase.
    signer3_name = models.CharField(db_column='SIGNER3_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    full_text = models.CharField(db_column='FULL_TEXT', max_length=250, blank=True, null=True)  # Field name made lowercase.
    last_edit_date = models.DateTimeField(db_column='LAST_EDIT_DATE')  # Field name made lowercase.
    last_edit_user = models.CharField(db_column='LAST_EDIT_USER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    writeoff_person = models.CharField(db_column='WRITEOFF_PERSON', max_length=100, blank=True, null=True)  # Field name made lowercase.
    acquisition_type = models.IntegerField(db_column='ACQUISITION_TYPE', blank=True, null=True)  # Field name made lowercase.
    out_reason = models.IntegerField(db_column='OUT_REASON', blank=True, null=True)  # Field name made lowercase.
    col202 = models.IntegerField(db_column='COL202', blank=True, null=True)  # Field name made lowercase.
    col203 = models.IntegerField(db_column='COL203', blank=True, null=True)  # Field name made lowercase.
    col206 = models.IntegerField(db_column='COL206', blank=True, null=True)  # Field name made lowercase.
    col207 = models.DecimalField(db_column='COL207', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    col208 = models.IntegerField(db_column='COL208', blank=True, null=True)  # Field name made lowercase.
    col209 = models.IntegerField(db_column='COL209', blank=True, null=True)  # Field name made lowercase.
    col211 = models.IntegerField(db_column='COL211', blank=True, null=True)  # Field name made lowercase.
    col212 = models.IntegerField(db_column='COL212', blank=True, null=True)  # Field name made lowercase.
    col213 = models.IntegerField(db_column='COL213', blank=True, null=True)  # Field name made lowercase.
    col214 = models.IntegerField(db_column='COL214', blank=True, null=True)  # Field name made lowercase.
    col215 = models.IntegerField(db_column='COL215', blank=True, null=True)  # Field name made lowercase.
    col216 = models.IntegerField(db_column='COL216', blank=True, null=True)  # Field name made lowercase.
    col217 = models.IntegerField(db_column='COL217', blank=True, null=True)  # Field name made lowercase.
    col218 = models.IntegerField(db_column='COL218', blank=True, null=True)  # Field name made lowercase.
    col220 = models.IntegerField(db_column='COL220', blank=True, null=True)  # Field name made lowercase.
    col221 = models.IntegerField(db_column='COL221', blank=True, null=True)  # Field name made lowercase.
    col222 = models.IntegerField(db_column='COL222', blank=True, null=True)  # Field name made lowercase.
    col224 = models.IntegerField(db_column='COL224', blank=True, null=True)  # Field name made lowercase.
    col225 = models.IntegerField(db_column='COL225', blank=True, null=True)  # Field name made lowercase.
    signer4_name = models.CharField(db_column='SIGNER4_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    signer4_post = models.CharField(db_column='SIGNER4_POST', max_length=250, blank=True, null=True)  # Field name made lowercase.
    signer5_name = models.CharField(db_column='SIGNER5_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    signer5_post = models.CharField(db_column='SIGNER5_POST', max_length=250, blank=True, null=True)  # Field name made lowercase.
    signer6_name = models.CharField(db_column='SIGNER6_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    signer6_post = models.CharField(db_column='SIGNER6_POST', max_length=250, blank=True, null=True)  # Field name made lowercase.
    signer7_name = models.CharField(db_column='SIGNER7_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    signer7_post = models.CharField(db_column='SIGNER7_POST', max_length=250, blank=True, null=True)  # Field name made lowercase.
    signer8_name = models.CharField(db_column='SIGNER8_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    signer8_post = models.CharField(db_column='SIGNER8_POST', max_length=250, blank=True, null=True)  # Field name made lowercase.
    signer9_name = models.CharField(db_column='SIGNER9_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    signer9_post = models.CharField(db_column='SIGNER9_POST', max_length=250, blank=True, null=True)  # Field name made lowercase.
    signer10_name = models.CharField(db_column='SIGNER10_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    signer10_post = models.CharField(db_column='SIGNER10_POST', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PARTY'


class PartyCond(models.Model):
    party_field_kod = models.SmallIntegerField(db_column='PARTY_FIELD_KOD', blank=True, null=True)  # Field name made lowercase.
    field_kod = models.IntegerField(db_column='FIELD_KOD', blank=True, null=True)  # Field name made lowercase.
    pred = models.SmallIntegerField(db_column='PRED', blank=True, null=True)  # Field name made lowercase.
    pred_type = models.SmallIntegerField(db_column='PRED_TYPE', blank=True, null=True)  # Field name made lowercase.
    pred_value1 = models.CharField(db_column='PRED_VALUE1', max_length=250, blank=True, null=True)  # Field name made lowercase.
    pred_value2 = models.CharField(db_column='PRED_VALUE2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pred_value = models.CharField(db_column='PRED_VALUE', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PARTY_COND'


class PartyFields(models.Model):
    kod = models.IntegerField(db_column='KOD', primary_key=True)  # Field name made lowercase.
    norder = models.SmallIntegerField(db_column='NORDER', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    parent_kod = models.SmallIntegerField(db_column='PARENT_KOD', blank=True, null=True)  # Field name made lowercase.
    isvert = models.SmallIntegerField(db_column='ISVERT', blank=True, null=True)  # Field name made lowercase.
    inuse = models.SmallIntegerField(db_column='INUSE', blank=True, null=True)  # Field name made lowercase.
    cond_used = models.SmallIntegerField(db_column='COND_USED', blank=True, null=True)  # Field name made lowercase.
    ntype = models.SmallIntegerField(db_column='NTYPE', blank=True, null=True)  # Field name made lowercase.
    name2 = models.CharField(db_column='NAME2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    name3 = models.CharField(db_column='NAME3', max_length=32, blank=True, null=True)  # Field name made lowercase.
    start_value = models.DecimalField(db_column='START_VALUE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PARTY_FIELDS'


class PersonCard(models.Model):
    person_id = models.IntegerField(db_column='PERSON_ID', blank=True, null=True)  # Field name made lowercase.
    person_type = models.CharField(db_column='PERSON_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    item_id = models.IntegerField(db_column='ITEM_ID', blank=True, null=True)  # Field name made lowercase.
    get_date = models.DateTimeField(db_column='GET_DATE')  # Field name made lowercase.
    return_date = models.DateTimeField(db_column='RETURN_DATE')  # Field name made lowercase.
    must_return_date = models.DateTimeField(db_column='MUST_RETURN_DATE')  # Field name made lowercase.
    commentt = models.CharField(db_column='COMMENTT', max_length=128, blank=True, null=True)  # Field name made lowercase.
    deliver_id = models.IntegerField(db_column='DELIVER_ID')  # Field name made lowercase.
    deliver_qty = models.SmallIntegerField(db_column='DELIVER_QTY', blank=True, null=True)  # Field name made lowercase.
    deliver_kod = models.SmallIntegerField(db_column='DELIVER_KOD', blank=True, null=True)  # Field name made lowercase.
    get_user = models.CharField(db_column='GET_USER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    return_user = models.CharField(db_column='RETURN_USER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    signature = models.CharField(db_column='SIGNATURE', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PERSON_CARD'


class PhysicalPerson(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    birth_date = models.DateTimeField(db_column='BIRTH_DATE')  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    passport_series = models.CharField(db_column='PASSPORT_SERIES', max_length=10, blank=True, null=True)  # Field name made lowercase.
    passport_no = models.IntegerField(db_column='PASSPORT_NO', blank=True, null=True)  # Field name made lowercase.
    work_place = models.CharField(db_column='WORK_PLACE', max_length=150, blank=True, null=True)  # Field name made lowercase.
    person_post = models.CharField(db_column='PERSON_POST', max_length=150, blank=True, null=True)  # Field name made lowercase.
    in_user = models.CharField(db_column='IN_USER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    work_phone = models.CharField(db_column='WORK_PHONE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    home_phone = models.CharField(db_column='HOME_PHONE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    kod = models.DecimalField(db_column='KOD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=80, blank=True, null=True)  # Field name made lowercase.
    mobile_phone = models.CharField(db_column='MOBILE_PHONE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    pager_no = models.IntegerField(db_column='PAGER_NO', blank=True, null=True)  # Field name made lowercase.
    pager_phone = models.CharField(db_column='PAGER_PHONE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    photo_old = models.TextField(db_column='PHOTO_OLD', blank=True, null=True)  # Field name made lowercase.
    code_intno = models.IntegerField(db_column='CODE_INTNO', blank=True, null=True)  # Field name made lowercase.
    is_blocked = models.SmallIntegerField(db_column='IS_BLOCKED', blank=True, null=True)  # Field name made lowercase.
    block_reason = models.CharField(db_column='BLOCK_REASON', max_length=200, blank=True, null=True)  # Field name made lowercase.
    register_date = models.DateTimeField(db_column='REGISTER_DATE')  # Field name made lowercase.
    in_date = models.DateTimeField(db_column='IN_DATE')  # Field name made lowercase.
    last_edit_date = models.DateTimeField(db_column='LAST_EDIT_DATE')  # Field name made lowercase.
    last_edit_user = models.CharField(db_column='LAST_EDIT_USER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    spassport_no = models.CharField(db_column='SPASSPORT_NO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    pin_code = models.CharField(db_column='PIN_CODE', max_length=250, blank=True, null=True)  # Field name made lowercase.
    service_begdate = models.DateTimeField(db_column='SERVICE_BEGDATE')  # Field name made lowercase.
    service_enddate = models.DateTimeField(db_column='SERVICE_ENDDATE')  # Field name made lowercase.
    category_id = models.IntegerField(db_column='CATEGORY_ID', blank=True, null=True)  # Field name made lowercase.
    passport_org = models.CharField(db_column='PASSPORT_ORG', max_length=128, blank=True, null=True)  # Field name made lowercase.
    scomment = models.CharField(db_column='SCOMMENT', max_length=250, blank=True, null=True)  # Field name made lowercase.
    table_id = models.CharField(db_column='TABLE_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    block_edit_date = models.DateTimeField(db_column='BLOCK_EDIT_DATE')  # Field name made lowercase.
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


class PrimaryField(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRIMARY_FIELD'


class PrintHeader(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    hftype = models.SmallIntegerField(db_column='HFTYPE', blank=True, null=True)  # Field name made lowercase.
    svalue = models.CharField(db_column='SVALUE', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRINT_HEADER'


class Profilelist(models.Model):
    suser_name = models.CharField(db_column='SUSER_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kod = models.IntegerField(db_column='KOD')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ntype = models.SmallIntegerField(db_column='NTYPE', blank=True, null=True)  # Field name made lowercase.
    group_kod = models.IntegerField(db_column='GROUP_KOD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROFILELIST'


class PublisherList(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=80, blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FULLNAME', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PUBLISHER_LIST'


class ReaderCategory(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    prefix = models.CharField(db_column='PREFIX', max_length=20, blank=True, null=True)  # Field name made lowercase.
    suffix = models.CharField(db_column='SUFFIX', max_length=20, blank=True, null=True)  # Field name made lowercase.
    digit_qty = models.SmallIntegerField(db_column='DIGIT_QTY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'READER_CATEGORY'


class ReaderPhoto(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    fld_type = models.SmallIntegerField(db_column='FLD_TYPE')  # Field name made lowercase.
    norder = models.IntegerField(db_column='NORDER')  # Field name made lowercase.
    fragment01 = models.CharField(db_column='FRAGMENT01', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment02 = models.CharField(db_column='FRAGMENT02', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment03 = models.CharField(db_column='FRAGMENT03', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment04 = models.CharField(db_column='FRAGMENT04', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment05 = models.CharField(db_column='FRAGMENT05', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment06 = models.CharField(db_column='FRAGMENT06', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment07 = models.CharField(db_column='FRAGMENT07', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment08 = models.CharField(db_column='FRAGMENT08', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'READER_PHOTO'


class ReaderPhoto2(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    field_type = models.IntegerField(db_column='FIELD_TYPE', blank=True, null=True)  # Field name made lowercase.
    fragment_order = models.IntegerField(db_column='FRAGMENT_ORDER', blank=True, null=True)  # Field name made lowercase.
    fragment_value = models.CharField(db_column='FRAGMENT_VALUE', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'READER_PHOTO2'


class ReaderSrvPlace(models.Model):
    reader_id = models.IntegerField(db_column='READER_ID', blank=True, null=True)  # Field name made lowercase.
    place_id = models.IntegerField(db_column='PLACE_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'READER_SRV_PLACE'


class ReaderVisit(models.Model):
    person_id = models.IntegerField(db_column='PERSON_ID', blank=True, null=True)  # Field name made lowercase.
    lock_id = models.IntegerField(db_column='LOCK_ID', blank=True, null=True)  # Field name made lowercase.
    lock_direction = models.CharField(db_column='LOCK_DIRECTION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    place_id = models.IntegerField(db_column='PLACE_ID', blank=True, null=True)  # Field name made lowercase.
    visit_time = models.DateTimeField(db_column='VISIT_TIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'READER_VISIT'


class RefuseStat(models.Model):
    person_id = models.IntegerField(db_column='PERSON_ID', blank=True, null=True)  # Field name made lowercase.
    person_type = models.CharField(db_column='PERSON_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    doc_id = models.IntegerField(db_column='DOC_ID', blank=True, null=True)  # Field name made lowercase.
    item_id = models.IntegerField(db_column='ITEM_ID', blank=True, null=True)  # Field name made lowercase.
    reason_kod = models.SmallIntegerField(db_column='REASON_KOD', blank=True, null=True)  # Field name made lowercase.
    reason_string = models.CharField(db_column='REASON_STRING', max_length=64, blank=True, null=True)  # Field name made lowercase.
    device_kod = models.SmallIntegerField(db_column='DEVICE_KOD', blank=True, null=True)  # Field name made lowercase.
    deliver_kod = models.SmallIntegerField(db_column='DELIVER_KOD', blank=True, null=True)  # Field name made lowercase.
    date_refuse = models.DateTimeField(db_column='DATE_REFUSE')  # Field name made lowercase.
    place_date = models.DateTimeField(db_column='PLACE_DATE')  # Field name made lowercase.
    user_refuse = models.CharField(db_column='USER_REFUSE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    refuse_type = models.SmallIntegerField(db_column='REFUSE_TYPE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REFUSE_STAT'


class RefuseTypes(models.Model):
    kod = models.IntegerField(db_column='KOD')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=80, blank=True, null=True)  # Field name made lowercase.
    is_default = models.SmallIntegerField(db_column='IS_DEFAULT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REFUSE_TYPES'


class RefCard(models.Model):
    card_id = models.IntegerField(db_column='CARD_ID', blank=True, null=True)  # Field name made lowercase.
    card_ref = models.IntegerField(db_column='CARD_REF', blank=True, null=True)  # Field name made lowercase.
    norder = models.SmallIntegerField(db_column='NORDER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REF_CARD'


class RefDoc(models.Model):
    card_id = models.IntegerField(db_column='CARD_ID')  # Field name made lowercase.
    doc_id = models.IntegerField(db_column='DOC_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REF_DOC'


class ServiceList(models.Model):
    service_id = models.IntegerField(db_column='SERVICE_ID', blank=True, null=True)  # Field name made lowercase.
    service_type = models.IntegerField(db_column='SERVICE_TYPE', blank=True, null=True)  # Field name made lowercase.
    place_id = models.IntegerField(db_column='PLACE_ID', blank=True, null=True)  # Field name made lowercase.
    reader_id = models.IntegerField(db_column='READER_ID', blank=True, null=True)  # Field name made lowercase.
    service_date = models.DateField(db_column='SERVICE_DATE', blank=True, null=True)  # Field name made lowercase.
    service_time = models.DateTimeField(db_column='SERVICE_TIME')  # Field name made lowercase.
    number_info = models.IntegerField(db_column='NUMBER_INFO', blank=True, null=True)  # Field name made lowercase.
    service_comment = models.CharField(db_column='SERVICE_COMMENT', max_length=250, blank=True, null=True)  # Field name made lowercase.
    in_user = models.CharField(db_column='IN_USER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    service_cost = models.DecimalField(db_column='SERVICE_COST', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SERVICE_LIST'


class ServicePlace(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SERVICE_PLACE'


class ServiceType(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SERVICE_TYPE'


class SpecialityList(models.Model):
    kod = models.SmallIntegerField(db_column='KOD', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SPECIALITY_LIST'


class StockList(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=48, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STOCK_LIST'


class StorageList(models.Model):
    kod = models.IntegerField(db_column='KOD', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_distribution = models.SmallIntegerField(db_column='IS_DISTRIBUTION', blank=True, null=True)  # Field name made lowercase.
    stype = models.CharField(db_column='STYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reader_qty = models.IntegerField(db_column='READER_QTY', blank=True, null=True)  # Field name made lowercase.
    file_reader_qty = models.IntegerField(db_column='FILE_READER_QTY', blank=True, null=True)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STORAGE_LIST'


class SubdivisionList(models.Model):
    kod = models.SmallIntegerField(db_column='KOD', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    division_kod = models.SmallIntegerField(db_column='DIVISION_KOD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SUBDIVISION_LIST'


class Tableprofile(models.Model):
    name = models.CharField(db_column='NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    profile = models.CharField(db_column='PROFILE', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TABLEPROFILE'


class TemplateBody(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    fld_type = models.SmallIntegerField(db_column='FLD_TYPE')  # Field name made lowercase.
    norder = models.IntegerField(db_column='NORDER')  # Field name made lowercase.
    fragment01 = models.CharField(db_column='FRAGMENT01', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment02 = models.CharField(db_column='FRAGMENT02', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment03 = models.CharField(db_column='FRAGMENT03', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment04 = models.CharField(db_column='FRAGMENT04', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment05 = models.CharField(db_column='FRAGMENT05', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment06 = models.CharField(db_column='FRAGMENT06', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment07 = models.CharField(db_column='FRAGMENT07', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fragment08 = models.CharField(db_column='FRAGMENT08', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEMPLATE_BODY'


class TemplateDatasrc(models.Model):
    template_code = models.SmallIntegerField(db_column='TEMPLATE_CODE', blank=True, null=True)  # Field name made lowercase.
    datasrc_code = models.SmallIntegerField(db_column='DATASRC_CODE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEMPLATE_DATASRC'


class TemplateXml(models.Model):
    code = models.IntegerField(db_column='CODE', blank=True, null=True)  # Field name made lowercase.
    ntype = models.IntegerField(db_column='NTYPE', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    body_old = models.TextField(db_column='BODY_OLD', blank=True, null=True)  # Field name made lowercase.
    isdefault = models.IntegerField(db_column='ISDEFAULT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEMPLATE_XML'


class Tempor(models.Model):
    uni_kod = models.IntegerField(db_column='UNI_KOD', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEMPOR'


class Ttp(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    dscp_id = models.IntegerField(db_column='DSCP_ID', blank=True, null=True)  # Field name made lowercase.
    division = models.IntegerField(db_column='DIVISION', blank=True, null=True)  # Field name made lowercase.
    subdivision = models.IntegerField(db_column='SUBDIVISION', blank=True, null=True)  # Field name made lowercase.
    acquisition_norm = models.DecimalField(db_column='ACQUISITION_NORM', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    student_qty = models.IntegerField(db_column='STUDENT_QTY', blank=True, null=True)  # Field name made lowercase.
    student_contr_qty = models.IntegerField(db_column='STUDENT_CONTR_QTY', blank=True, null=True)  # Field name made lowercase.
    distribution = models.IntegerField(db_column='DISTRIBUTION', blank=True, null=True)  # Field name made lowercase.
    contr_norm = models.DecimalField(db_column='CONTR_NORM', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fld102 = models.IntegerField(db_column='FLD102', blank=True, null=True)  # Field name made lowercase.
    fld103 = models.IntegerField(db_column='FLD103', blank=True, null=True)  # Field name made lowercase.
    fld104 = models.IntegerField(db_column='FLD104', blank=True, null=True)  # Field name made lowercase.
    fld105 = models.IntegerField(db_column='FLD105', blank=True, null=True)  # Field name made lowercase.
    day_from = models.IntegerField(db_column='DAY_FROM', blank=True, null=True)  # Field name made lowercase.
    day_to = models.IntegerField(db_column='DAY_TO', blank=True, null=True)  # Field name made lowercase.
    is_active = models.IntegerField(db_column='IS_ACTIVE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TTP'


class TtphierFldorder(models.Model):
    fld_id = models.IntegerField(db_column='FLD_ID')  # Field name made lowercase.
    norder = models.IntegerField(db_column='NORDER')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TTPHIER_FLDORDER'


class TtphierOptions(models.Model):
    fld_used_qty = models.IntegerField(db_column='FLD_USED_QTY')  # Field name made lowercase.
    show_unused = models.IntegerField(db_column='SHOW_UNUSED')  # Field name made lowercase.
    show_reader_qty = models.IntegerField(db_column='SHOW_READER_QTY')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TTPHIER_OPTIONS'


class TtpField(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    norder = models.SmallIntegerField(db_column='NORDER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TTP_FIELD'


class TtpFieldEnum(models.Model):
    fld_id = models.IntegerField(db_column='FLD_ID')  # Field name made lowercase.
    enum_id = models.IntegerField(db_column='ENUM_ID')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    norder = models.IntegerField(db_column='NORDER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TTP_FIELD_ENUM'


class TypeList(models.Model):
    kod = models.SmallIntegerField(db_column='KOD')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TYPE_LIST'


class TypicalValues(models.Model):
    value_type = models.CharField(db_column='VALUE_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    value_text = models.CharField(db_column='VALUE_TEXT', max_length=250, blank=True, null=True)  # Field name made lowercase.
    value_order = models.IntegerField(db_column='VALUE_ORDER', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TYPICAL_VALUES'


class UsedKod(models.Model):
    kod = models.IntegerField(db_column='KOD', blank=True, null=True)  # Field name made lowercase.
    newkod = models.IntegerField(db_column='NEWKOD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USED_KOD'


class Usergroup(models.Model):
    alias = models.CharField(db_column='ALIAS', max_length=50)  # Field name made lowercase.
    groupcode = models.IntegerField(db_column='GROUPCODE', blank=True, null=True)  # Field name made lowercase.
    isdefault = models.SmallIntegerField(db_column='ISDEFAULT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USERGROUP'


class Userlist(models.Model):
    alias = models.CharField(db_column='ALIAS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USERLIST'


class UserrepAuthority(models.Model):
    rep_code = models.IntegerField(db_column='REP_CODE')  # Field name made lowercase.
    group_code = models.IntegerField(db_column='GROUP_CODE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USERREP_AUTHORITY'


class UserReports(models.Model):
    kod = models.SmallIntegerField(db_column='KOD', blank=True, null=True)  # Field name made lowercase.
    sqls = models.TextField(db_column='SQLS', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FILENAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    body = models.TextField(db_column='BODY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USER_REPORTS'


class Winprofiles(models.Model):
    profile_kod = models.IntegerField(db_column='PROFILE_KOD', blank=True, null=True)  # Field name made lowercase.
    norder = models.SmallIntegerField(db_column='NORDER', blank=True, null=True)  # Field name made lowercase.
    win_kod = models.SmallIntegerField(db_column='WIN_KOD', blank=True, null=True)  # Field name made lowercase.
    window_name = models.CharField(db_column='WINDOW_NAME', max_length=40, blank=True, null=True)  # Field name made lowercase.
    win_type = models.SmallIntegerField(db_column='WIN_TYPE', blank=True, null=True)  # Field name made lowercase.
    win_aux_int = models.IntegerField(db_column='WIN_AUX_INT', blank=True, null=True)  # Field name made lowercase.
    win_aux_str = models.CharField(db_column='WIN_AUX_STR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    win_x = models.DecimalField(db_column='WIN_X', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    win_y = models.DecimalField(db_column='WIN_Y', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    win_w = models.DecimalField(db_column='WIN_W', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    win_h = models.DecimalField(db_column='WIN_H', max_digits=10, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    win_state = models.SmallIntegerField(db_column='WIN_STATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WINPROFILES'


class WordIndex(models.Model):
    doc_id = models.IntegerField(db_column='DOC_ID', blank=True, null=True)  # Field name made lowercase.
    field_kod = models.SmallIntegerField(db_column='FIELD_KOD', blank=True, null=True)  # Field name made lowercase.
    word = models.CharField(db_column='WORD', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WORD_INDEX'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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

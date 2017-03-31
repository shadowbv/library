# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AccEldocs(models.Model):
    dt_acc = models.DateTimeField(blank=True, null=True)
    doc_id = models.IntegerField(blank=True, null=True)
    r_kod = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acc_eldocs'


class AcquisitionTypes(models.Model):
    kod = models.IntegerField()
    name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acquisition_types'


class AnnotWordIndex(models.Model):
    doc = models.ForeignKey('Document', blank=True, null=True)
    word = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'annot_word_index'


class AuthTypeMain(models.Model):
    kod = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=1, blank=True, null=True)
    stat = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_type_main'


class AuthorList(models.Model):
    kod = models.SmallIntegerField()
    name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'author_list'


class AuthorMarkList(models.Model):
    kod = models.SmallIntegerField()
    name = models.CharField(max_length=20, blank=True, null=True)
    mark_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'author_mark_list'


class AuthorSynonym(models.Model):
    id = models.IntegerField()
    author = models.CharField(max_length=50)
    norder = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'author_synonym'


class AuthorWordIndex(models.Model):
    doc = models.ForeignKey('Document')
    author = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'author_word_index'


class Authoritylist(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=250, blank=True, null=True)
    tablelist = models.CharField(max_length=250, blank=True, null=True)
    tablelist2 = models.CharField(max_length=250, blank=True, null=True)
    authlist = models.CharField(max_length=250, blank=True, null=True)
    norder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authoritylist'


class BlockreasonList(models.Model):
    kod = models.SmallIntegerField()
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blockreason_list'


class Cards(models.Model):
    card_id = models.IntegerField()
    hier_id = models.IntegerField(blank=True, null=True)
    stype = models.CharField(max_length=1, blank=True, null=True)
    dt_creat = models.DateTimeField(blank=True, null=True)
    doc_count = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=230, blank=True, null=True)
    topic_type = models.CharField(max_length=250, blank=True, null=True)
    sign = models.CharField(max_length=250, blank=True, null=True)
    first_part_name = models.CharField(max_length=250, blank=True, null=True)
    next_part_name = models.CharField(max_length=250, blank=True, null=True)
    full_initials = models.CharField(max_length=250, blank=True, null=True)
    add_part_name = models.CharField(max_length=250, blank=True, null=True)
    other_part_name = models.CharField(max_length=250, blank=True, null=True)
    topic_dates = models.CharField(max_length=250, blank=True, null=True)
    place = models.CharField(max_length=250, blank=True, null=True)
    affilation = models.CharField(max_length=250, blank=True, null=True)
    topic = models.CharField(max_length=250, blank=True, null=True)
    geographical = models.CharField(max_length=250, blank=True, null=True)
    chronological = models.CharField(max_length=250, blank=True, null=True)
    topic_format = models.CharField(max_length=250, blank=True, null=True)
    topic_comment = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cards'


class CityList(models.Model):
    kod = models.SmallIntegerField()
    name = models.CharField(max_length=80, blank=True, null=True)
    fullname = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city_list'


class ClientFiles(models.Model):
    filename = models.CharField(max_length=100)
    filebin = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'client_files'


class CodeParsingList(models.Model):
    kod = models.SmallIntegerField()
    name = models.CharField(max_length=48, blank=True, null=True)
    separator = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'code_parsing_list'


class CodeParsingRules(models.Model):
    parsing_kod = models.SmallIntegerField(blank=True, null=True)
    norder = models.SmallIntegerField(blank=True, null=True)
    master_card = models.IntegerField(blank=True, null=True)
    beg_separator = models.CharField(max_length=5, blank=True, null=True)
    end_separator = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'code_parsing_rules'


class Colprofiles(models.Model):
    profile_kod = models.IntegerField()
    win_kod = models.SmallIntegerField()
    col_kod = models.IntegerField()
    col_w = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    col_pos = models.SmallIntegerField(blank=True, null=True)
    col_hidden = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'colprofiles'
        unique_together = (('profile_kod', 'win_kod', 'col_kod'),)


class Devices(models.Model):
    kod = models.SmallIntegerField()
    name = models.CharField(max_length=32, blank=True, null=True)
    path = models.CharField(max_length=80, blank=True, null=True)
    save_style = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devices'


class DictionList(models.Model):
    kod = models.SmallIntegerField()
    name = models.CharField(max_length=48, blank=True, null=True)
    ntype = models.SmallIntegerField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diction_list'


class DictionWord(models.Model):
    dic_kod = models.SmallIntegerField()
    kod = models.IntegerField()
    word = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diction_word'


class Discipline(models.Model):
    id = models.IntegerField()
    cipher = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    subname = models.CharField(max_length=100, blank=True, null=True)
    scomment = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discipline'


class DivisionList(models.Model):
    kod = models.SmallIntegerField()
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'division_list'


class DocAgentIndex(models.Model):
    doc_id = models.IntegerField(blank=True, null=True)
    record_header = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doc_agent_index'


class DocAnnotation(models.Model):
    doc_id = models.IntegerField(blank=True, null=True)
    norder = models.SmallIntegerField(blank=True, null=True)
    fragment = models.CharField(max_length=251, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doc_annotation'


class DocDscp(models.Model):
    doc_id = models.IntegerField(blank=True, null=True)
    dscp_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doc_dscp'


class DocItem(models.Model):
    doc = models.ForeignKey('Document')
    item_id = models.IntegerField()
    item_no = models.CharField(max_length=32, blank=True, null=True)
    reg_date = models.DateTimeField(blank=True, null=True)
    commentt = models.CharField(max_length=128, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    delivered = models.SmallIntegerField(blank=True, null=True)
    device_kod = models.SmallIntegerField(blank=True, null=True)
    party_kod = models.IntegerField(blank=True, null=True)
    party_no = models.CharField(max_length=15, blank=True, null=True)
    act_kod = models.IntegerField(blank=True, null=True)
    act_no = models.CharField(max_length=10, blank=True, null=True)
    out_reason = models.SmallIntegerField(blank=True, null=True)
    qtyall = models.SmallIntegerField(blank=True, null=True)
    qtyact = models.SmallIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price_unit = models.SmallIntegerField(blank=True, null=True)
    stock_kod = models.SmallIntegerField(blank=True, null=True)
    nobalance = models.SmallIntegerField(blank=True, null=True)
    item_number = models.CharField(max_length=20, blank=True, null=True)
    item_intno = models.IntegerField(blank=True, null=True)
    item_mainno = models.CharField(max_length=32, blank=True, null=True)
    device_date = models.DateTimeField(blank=True, null=True)
    device_user = models.CharField(max_length=30, blank=True, null=True)
    device_prev = models.IntegerField(blank=True, null=True)
    last_edit_date = models.DateTimeField(blank=True, null=True)
    last_edit_user = models.CharField(max_length=30, blank=True, null=True)
    distribution_kod = models.SmallIntegerField(blank=True, null=True)
    rfid = models.CharField(max_length=32, blank=True, null=True)
    barcode = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doc_item'


class DocLongfield(models.Model):
    id = models.IntegerField()
    fld_type = models.SmallIntegerField()
    norder = models.IntegerField()
    fragment01 = models.CharField(max_length=250, blank=True, null=True)
    fragment02 = models.CharField(max_length=250, blank=True, null=True)
    fragment03 = models.CharField(max_length=250, blank=True, null=True)
    fragment04 = models.CharField(max_length=250, blank=True, null=True)
    fragment05 = models.CharField(max_length=250, blank=True, null=True)
    fragment06 = models.CharField(max_length=250, blank=True, null=True)
    fragment07 = models.CharField(max_length=250, blank=True, null=True)
    fragment08 = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doc_longfield'


class DocNumeration(models.Model):
    doc_id = models.IntegerField()
    numeration = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doc_numeration'


class DocOtherfield(models.Model):
    doc = models.ForeignKey('Document')
    fields = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doc_otherfield'


class DocOtherfieldLst(models.Model):
    kod = models.SmallIntegerField()
    name = models.CharField(max_length=64, blank=True, null=True)
    usmarc_tag = models.CharField(max_length=10, blank=True, null=True)
    unimarc_tag = models.CharField(max_length=10, blank=True, null=True)
    commentt = models.CharField(max_length=100, blank=True, null=True)
    usmarc_ind = models.CharField(max_length=2, blank=True, null=True)
    unimarc_ind = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doc_otherfield_lst'


class DocPresence(models.Model):
    doc_id = models.IntegerField()
    doc_owner = models.CharField(max_length=32)
    scomment = models.CharField(max_length=250, blank=True, null=True)
    actual_date = models.DateTimeField(blank=True, null=True)
    numeration = models.BinaryField(blank=True, null=True)
    item_qty = models.IntegerField(blank=True, null=True)
    stock_item_qty = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doc_presence'


class DocPresenceNum(models.Model):
    doc_id = models.IntegerField()
    doc_owner = models.CharField(max_length=32)
    norder = models.IntegerField()
    fragment01 = models.CharField(max_length=250, blank=True, null=True)
    fragment02 = models.CharField(max_length=250, blank=True, null=True)
    fragment03 = models.CharField(max_length=250, blank=True, null=True)
    fragment04 = models.CharField(max_length=250, blank=True, null=True)
    fragment05 = models.CharField(max_length=250, blank=True, null=True)
    fragment06 = models.CharField(max_length=250, blank=True, null=True)
    fragment07 = models.CharField(max_length=250, blank=True, null=True)
    fragment08 = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doc_presence_num'


class DocRequest(models.Model):
    id = models.IntegerField()
    doc = models.ForeignKey('Document', blank=True, null=True)
    date_req = models.DateTimeField(blank=True, null=True)
    order_name = models.CharField(max_length=64, blank=True, null=True)
    qty = models.SmallIntegerField(blank=True, null=True)
    priority_no = models.SmallIntegerField(blank=True, null=True)
    req_status = models.SmallIntegerField(blank=True, null=True)
    commentt = models.CharField(max_length=100, blank=True, null=True)
    division_kod = models.SmallIntegerField(blank=True, null=True)
    subdivision_kod = models.SmallIntegerField(blank=True, null=True)
    speciality_kod = models.SmallIntegerField(blank=True, null=True)
    accepted = models.IntegerField(blank=True, null=True)
    device_kod = models.IntegerField(blank=True, null=True)
    dscp_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doc_request'


class DocnameList(models.Model):
    kod = models.SmallIntegerField()
    name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'docname_list'


class Doctype(models.Model):
    code = models.SmallIntegerField()
    name = models.CharField(max_length=250, blank=True, null=True)
    norder = models.SmallIntegerField()
    marccode = models.CharField(max_length=3, blank=True, null=True)
    nlevel = models.IntegerField(blank=True, null=True)
    bibtype = models.IntegerField(blank=True, null=True)
    default_child_link = models.IntegerField(blank=True, null=True)
    default_child_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctype'


class DoctypeField(models.Model):
    doctype_kod = models.SmallIntegerField()
    col_kod = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'doctype_field'


class Document(models.Model):
    doc_type = models.SmallIntegerField()
    name = models.CharField(max_length=250, blank=True, null=True)
    device_kod = models.SmallIntegerField(blank=True, null=True)
    type_kod = models.SmallIntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    reg_date = models.DateTimeField(blank=True, null=True)
    publ_place = models.CharField(max_length=80, blank=True, null=True)
    in_date = models.DateTimeField()
    long_filename = models.CharField(max_length=250, blank=True, null=True)
    attr = models.SmallIntegerField(blank=True, null=True)
    doc_id = models.IntegerField(primary_key=True)
    filename = models.CharField(max_length=245, blank=True, null=True)
    author = models.CharField(max_length=250, blank=True, null=True)
    in_user = models.CharField(max_length=50)
    last_edit_date = models.DateTimeField()
    last_edit_user = models.CharField(max_length=50)
    item_qty = models.SmallIntegerField()
    item_present = models.SmallIntegerField()
    udk = models.CharField(max_length=200, blank=True, null=True)
    isbn = models.CharField(max_length=64, blank=True, null=True)
    bbk = models.CharField(max_length=200, blank=True, null=True)
    author_mark = models.CharField(max_length=20, blank=True, null=True)
    issn = models.CharField(max_length=32, blank=True, null=True)
    lang = models.CharField(max_length=32, blank=True, null=True)
    lang_kod = models.SmallIntegerField(blank=True, null=True)
    cipher = models.CharField(max_length=32, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sizem = models.CharField(max_length=50, blank=True, null=True)
    annot1 = models.CharField(max_length=254, blank=True, null=True)
    annot2 = models.CharField(max_length=254, blank=True, null=True)
    annot3 = models.CharField(max_length=254, blank=True, null=True)
    annot4 = models.CharField(max_length=254, blank=True, null=True)
    cdlabel = models.CharField(max_length=32, blank=True, null=True)
    text_file = models.BinaryField(blank=True, null=True)
    group_kod = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    is_parent = models.SmallIntegerField(blank=True, null=True)
    author_type = models.SmallIntegerField(blank=True, null=True)
    name_prefix = models.CharField(max_length=20, blank=True, null=True)
    publ_year = models.CharField(max_length=50, blank=True, null=True)
    parent_type = models.IntegerField(blank=True, null=True)
    format_num = models.CharField(max_length=32, blank=True, null=True)
    del_r_user = models.CharField(max_length=50, blank=True, null=True)
    del_r_date = models.DateField(blank=True, null=True)
    del_d_user = models.CharField(max_length=50, blank=True, null=True)
    del_d_date = models.DateField(blank=True, null=True)


class Document(models.Model):
    doc_type = models.SmallIntegerField()
    name = models.CharField(max_length=250, blank=True, null=True)
    device_kod = models.SmallIntegerField(blank=True, null=True)
    type_kod = models.SmallIntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    reg_date = models.DateTimeField(blank=True, null=True)
    publ_place = models.CharField(max_length=80, blank=True, null=True)
    in_date = models.DateTimeField()
    long_filename = models.CharField(max_length=250, blank=True, null=True)
    attr = models.SmallIntegerField(blank=True, null=True)
    doc_id = models.IntegerField(primary_key=True)
    filename = models.CharField(max_length=245, blank=True, null=True)
    author = models.CharField(max_length=250, blank=True, null=True)
    in_user = models.CharField(max_length=50)
    last_edit_date = models.DateTimeField()
    last_edit_user = models.CharField(max_length=50)
    item_qty = models.SmallIntegerField()
    item_present = models.SmallIntegerField()
    udk = models.CharField(max_length=200, blank=True, null=True)
    isbn = models.CharField(max_length=64, blank=True, null=True)
    bbk = models.CharField(max_length=200, blank=True, null=True)
    author_mark = models.CharField(max_length=20, blank=True, null=True)
    issn = models.CharField(max_length=32, blank=True, null=True)
    lang = models.CharField(max_length=32, blank=True, null=True)
    lang_kod = models.SmallIntegerField(blank=True, null=True)
    cipher = models.CharField(max_length=32, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sizem = models.CharField(max_length=50, blank=True, null=True)
    annot1 = models.CharField(max_length=254, blank=True, null=True)
    annot2 = models.CharField(max_length=254, blank=True, null=True)
    annot3 = models.CharField(max_length=254, blank=True, null=True)
    annot4 = models.CharField(max_length=254, blank=True, null=True)
    cdlabel = models.CharField(max_length=32, blank=True, null=True)
    text_file = models.BinaryField(blank=True, null=True)
    group_kod = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    is_parent = models.SmallIntegerField(blank=True, null=True)
    author_type = models.SmallIntegerField(blank=True, null=True)
    name_prefix = models.CharField(max_length=20, blank=True, null=True)
    publ_year = models.CharField(max_length=50, blank=True, null=True)
    parent_type = models.IntegerField(blank=True, null=True)
    format_num = models.CharField(max_length=32, blank=True, null=True)
    del_r_user = models.CharField(max_length=50, blank=True, null=True)
    del_r_date = models.DateField(blank=True, null=True)
    del_d_user = models.CharField(max_length=50, blank=True, null=True)
    del_d_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document'


class DocxfieldList(models.Model):
    kod = models.SmallIntegerField()
    name = models.CharField(max_length=250)
    stype = models.CharField(max_length=10)
    nlength = models.SmallIntegerField(blank=True, null=True)
    scale = models.SmallIntegerField(blank=True, null=True)
    superfield = models.SmallIntegerField(blank=True, null=True)
    useinquery = models.SmallIntegerField(blank=True, null=True)
    useinsort = models.SmallIntegerField(blank=True, null=True)
    useinlist = models.SmallIntegerField(blank=True, null=True)
    norder = models.SmallIntegerField(blank=True, null=True)
    marctag = models.CharField(max_length=3, blank=True, null=True)
    marc_subfield = models.CharField(max_length=1, blank=True, null=True)
    marcpos_start = models.SmallIntegerField(blank=True, null=True)
    marcpos_end = models.SmallIntegerField(blank=True, null=True)
    marc_multiple = models.CharField(max_length=1, blank=True, null=True)
    marc_codetbl = models.CharField(max_length=18, blank=True, null=True)
    allowtextedit = models.SmallIntegerField(blank=True, null=True)
    marc_indicators = models.CharField(max_length=2, blank=True, null=True)
    marc_addfield = models.CharField(max_length=80, blank=True, null=True)
    short_name = models.CharField(max_length=100, blank=True, null=True)
    separator = models.CharField(max_length=5, blank=True, null=True)
    area = models.SmallIntegerField(blank=True, null=True)
    nno = models.SmallIntegerField(blank=True, null=True)
    end_separator = models.CharField(max_length=5, blank=True, null=True)
    unimarctag = models.CharField(max_length=3, blank=True, null=True)
    unimarc_subfield = models.CharField(max_length=1, blank=True, null=True)
    unimarcpos_start = models.SmallIntegerField(blank=True, null=True)
    unimarcpos_end = models.SmallIntegerField(blank=True, null=True)
    unimarc_indicators = models.CharField(max_length=2, blank=True, null=True)
    unimarc_addfield = models.CharField(max_length=80, blank=True, null=True)
    unimarc_multiple = models.CharField(max_length=1, blank=True, null=True)
    unimarc_codetbl = models.CharField(max_length=18, blank=True, null=True)
    uniallowtextedit = models.SmallIntegerField(blank=True, null=True)
    author_level = models.SmallIntegerField(blank=True, null=True)
    colname = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'docxfield_list'


class DocxfieldValue(models.Model):
    doc = models.ForeignKey(Document)
    col002 = models.CharField(max_length=100, blank=True, null=True)
    col003 = models.CharField(max_length=50, blank=True, null=True)
    col004 = models.CharField(max_length=20, blank=True, null=True)
    col006 = models.CharField(max_length=32, blank=True, null=True)
    col007 = models.CharField(max_length=32, blank=True, null=True)
    col008 = models.CharField(max_length=64, blank=True, null=True)
    col010 = models.CharField(max_length=80, blank=True, null=True)
    col011 = models.CharField(max_length=32, blank=True, null=True)
    col012 = models.CharField(max_length=80, blank=True, null=True)
    col013 = models.CharField(max_length=32, blank=True, null=True)
    col014 = models.CharField(max_length=128, blank=True, null=True)
    col016 = models.CharField(max_length=250, blank=True, null=True)
    col017 = models.CharField(max_length=200, blank=True, null=True)
    col018 = models.CharField(max_length=20, blank=True, null=True)
    col019 = models.CharField(max_length=200, blank=True, null=True)
    col020 = models.CharField(max_length=20, blank=True, null=True)
    col021 = models.CharField(max_length=200, blank=True, null=True)
    col022 = models.DateField(blank=True, null=True)
    col023 = models.DateField(blank=True, null=True)
    col024 = models.CharField(max_length=250, blank=True, null=True)
    col025 = models.CharField(max_length=250, blank=True, null=True)
    col026 = models.CharField(max_length=64, blank=True, null=True)
    col027 = models.CharField(max_length=64, blank=True, null=True)
    col028 = models.CharField(max_length=50, blank=True, null=True)
    col029 = models.CharField(max_length=250, blank=True, null=True)
    col030 = models.CharField(max_length=250, blank=True, null=True)
    col031 = models.CharField(max_length=64, blank=True, null=True)
    col033 = models.CharField(max_length=32, blank=True, null=True)
    col035 = models.IntegerField(blank=True, null=True)
    col036 = models.IntegerField(blank=True, null=True)
    col037 = models.CharField(max_length=50, blank=True, null=True)
    col038 = models.CharField(max_length=250, blank=True, null=True)
    col039 = models.CharField(max_length=100, blank=True, null=True)
    col040 = models.CharField(max_length=100, blank=True, null=True)
    col041 = models.IntegerField(blank=True, null=True)
    col043 = models.CharField(max_length=50, blank=True, null=True)
    col044 = models.CharField(max_length=250, blank=True, null=True)
    col045 = models.CharField(max_length=3, blank=True, null=True)
    col046 = models.CharField(max_length=50, blank=True, null=True)
    col047 = models.CharField(max_length=50, blank=True, null=True)
    col048 = models.CharField(max_length=150, blank=True, null=True)
    col049 = models.CharField(max_length=25, blank=True, null=True)
    col051 = models.CharField(max_length=200, blank=True, null=True)
    col052 = models.CharField(max_length=20, blank=True, null=True)
    col054 = models.CharField(max_length=20, blank=True, null=True)
    col055 = models.CharField(max_length=20, blank=True, null=True)
    col056 = models.CharField(max_length=20, blank=True, null=True)
    col057 = models.CharField(max_length=100, blank=True, null=True)
    col059 = models.CharField(max_length=10, blank=True, null=True)
    col060 = models.CharField(max_length=10, blank=True, null=True)
    col061 = models.CharField(max_length=10, blank=True, null=True)
    col062 = models.CharField(max_length=50, blank=True, null=True)
    col064 = models.CharField(max_length=200, blank=True, null=True)
    col065 = models.CharField(max_length=40, blank=True, null=True)
    col067 = models.CharField(max_length=40, blank=True, null=True)
    col068 = models.CharField(max_length=20, blank=True, null=True)
    col069 = models.CharField(max_length=100, blank=True, null=True)
    col070 = models.CharField(max_length=100, blank=True, null=True)
    col072 = models.CharField(max_length=200, blank=True, null=True)
    col073 = models.CharField(max_length=200, blank=True, null=True)
    col074 = models.CharField(max_length=200, blank=True, null=True)
    col075 = models.CharField(max_length=200, blank=True, null=True)
    col077 = models.CharField(max_length=10, blank=True, null=True)
    col078 = models.CharField(max_length=3, blank=True, null=True)
    col079 = models.CharField(max_length=1, blank=True, null=True)
    col080 = models.CharField(max_length=10, blank=True, null=True)
    col081 = models.CharField(max_length=40, blank=True, null=True)
    col082 = models.CharField(max_length=100, blank=True, null=True)
    col083 = models.CharField(max_length=20, blank=True, null=True)
    col084 = models.CharField(max_length=70, blank=True, null=True)
    col086 = models.CharField(max_length=200, blank=True, null=True)
    col087 = models.CharField(max_length=250, blank=True, null=True)
    col088 = models.CharField(max_length=250, blank=True, null=True)
    col089 = models.CharField(max_length=25, blank=True, null=True)
    col090 = models.CharField(max_length=200, blank=True, null=True)
    col091 = models.CharField(max_length=250, blank=True, null=True)
    col092 = models.CharField(max_length=250, blank=True, null=True)
    col093 = models.CharField(max_length=25, blank=True, null=True)
    col094 = models.CharField(max_length=250, blank=True, null=True)
    col095 = models.CharField(max_length=30, blank=True, null=True)
    col097 = models.CharField(max_length=3, blank=True, null=True)
    col098 = models.CharField(max_length=200, blank=True, null=True)
    col099 = models.CharField(max_length=250, blank=True, null=True)
    col101 = models.CharField(max_length=1, blank=True, null=True)
    col102 = models.CharField(max_length=1, blank=True, null=True)
    col103 = models.CharField(max_length=1, blank=True, null=True)
    col104 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'docxfield_value'


class DscpTopic(models.Model):
    dscp_id = models.IntegerField()
    topic_type = models.CharField(max_length=3, blank=True, null=True)
    topic_value = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dscp_topic'


class ExtqueryBody(models.Model):
    id = models.IntegerField()
    fld_type = models.SmallIntegerField()
    norder = models.IntegerField()
    fragment01 = models.CharField(max_length=250, blank=True, null=True)
    fragment02 = models.CharField(max_length=250, blank=True, null=True)
    fragment03 = models.CharField(max_length=250, blank=True, null=True)
    fragment04 = models.CharField(max_length=250, blank=True, null=True)
    fragment05 = models.CharField(max_length=250, blank=True, null=True)
    fragment06 = models.CharField(max_length=250, blank=True, null=True)
    fragment07 = models.CharField(max_length=250, blank=True, null=True)
    fragment08 = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'extquery_body'


class GeneralXmlTree(models.Model):
    tree_id = models.CharField(max_length=50, blank=True, null=True)
    node_level = models.SmallIntegerField(blank=True, null=True)
    is_attribute = models.SmallIntegerField(blank=True, null=True)
    node_name = models.CharField(max_length=250, blank=True, null=True)
    node_value = models.CharField(max_length=250, blank=True, null=True)
    part_number = models.SmallIntegerField(blank=True, null=True)
    suffix_size = models.SmallIntegerField(blank=True, null=True)
    node_order = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_xml_tree'


class Genprofiles(models.Model):
    suser_name = models.CharField(max_length=50, blank=True, null=True)
    section_name = models.CharField(max_length=40, blank=True, null=True)
    item_name = models.CharField(max_length=40, blank=True, null=True)
    svalue = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genprofiles'
        unique_together = (('suser_name', 'section_name', 'item_name'),)


class Groupauthority(models.Model):
    groupcode = models.IntegerField()
    authcode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'groupauthority'


class Grouplist(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grouplist'


class IndexedField(models.Model):
    kod = models.SmallIntegerField()
    ntype = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indexed_field'


class InventBook(models.Model):
    kod = models.SmallIntegerField()
    name = models.CharField(max_length=32, blank=True, null=True)
    item_sort_list = models.CharField(max_length=64, blank=True, null=True)
    doctype_list = models.CharField(max_length=64, blank=True, null=True)
    flags = models.IntegerField(blank=True, null=True)
    no_from = models.IntegerField(blank=True, null=True)
    no_to = models.IntegerField(blank=True, null=True)
    date_from = models.DateTimeField(blank=True, null=True)
    date_to = models.DateTimeField(blank=True, null=True)
    no_prefix = models.CharField(max_length=10, blank=True, null=True)
    cur_no = models.IntegerField(blank=True, null=True)
    no_length = models.SmallIntegerField(blank=True, null=True)
    no_suffix = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invent_book'


class Item(models.Model):
    item_intno = models.IntegerField(primary_key=True)
    doc_id = models.IntegerField()
    user_name = models.CharField(max_length=50)
    status = models.CharField(max_length=1, blank=True, null=True)
    inv_date = models.DateTimeField()
    ip = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'item'


class ItemAddition(models.Model):
    doc_id = models.IntegerField()
    device_kod = models.IntegerField(blank=True, null=True)
    oncreate_qty = models.IntegerField(blank=True, null=True)
    accepted_qty = models.IntegerField(blank=True, null=True)
    last_edit_date = models.DateTimeField(blank=True, null=True)
    last_edit_user = models.CharField(max_length=50, blank=True, null=True)
    pass_qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_addition'


class ItemOutreason(models.Model):
    id = models.IntegerField(blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    out_reason = models.SmallIntegerField(blank=True, null=True)
    out_qty = models.SmallIntegerField(blank=True, null=True)
    act_kod = models.IntegerField(blank=True, null=True)
    act_no = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_outreason'


class JuridicalPerson(models.Model):
    id = models.IntegerField()
    phone1 = models.CharField(max_length=32, blank=True, null=True)
    kod = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    phone2 = models.CharField(max_length=32, blank=True, null=True)
    fax = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    chief_name = models.CharField(max_length=32, blank=True, null=True)
    chief_post = models.CharField(max_length=32, blank=True, null=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    in_user = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    supplier = models.CharField(max_length=1, blank=True, null=True)
    in_date = models.DateTimeField(blank=True, null=True)
    last_edit_date = models.DateTimeField(blank=True, null=True)
    last_edit_user = models.CharField(max_length=50, blank=True, null=True)
    ispartner = models.IntegerField(blank=True, null=True)
    iscomposite = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'juridical_person'


class KatDoc(models.Model):
    kod = models.SmallIntegerField()
    code = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=48, blank=True, null=True)
    stat = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kat_doc'


class KnowledgeT(models.Model):
    kod = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    code = models.CharField(max_length=3, blank=True, null=True)
    stat = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'knowledge_t'


class Languages(models.Model):
    kod = models.SmallIntegerField()
    name = models.CharField(max_length=32, blank=True, null=True)
    code = models.CharField(max_length=3, blank=True, null=True)
    stat = models.CharField(max_length=1, blank=True, null=True)
    used = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'languages'


class Licence(models.Model):
    licenceno = models.CharField(max_length=50)
    userqty = models.SmallIntegerField()
    maxdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'licence'


class LicenceInfo(models.Model):
    licence_type = models.CharField(max_length=100, blank=True, null=True)
    licence_no = models.CharField(max_length=200, blank=True, null=True)
    user_qty = models.IntegerField(blank=True, null=True)
    max_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'licence_info'


class MarcDocdesc(models.Model):
    code = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marc_docdesc'


class MarcDoclevel(models.Model):
    code = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    unimarc_code = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marc_doclevel'


class MarcDoctype(models.Model):
    code = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=48, blank=True, null=True)
    unimarc_code = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marc_doctype'


class MarcsysCountry(models.Model):
    kod = models.SmallIntegerField()
    code = models.CharField(max_length=5, blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    stat = models.CharField(max_length=1, blank=True, null=True)
    used = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marcsys_country'


class MarcsysForm(models.Model):
    kod = models.SmallIntegerField()
    code = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=48, blank=True, null=True)
    stat = models.CharField(max_length=1, blank=True, null=True)
    unimarc_code = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marcsys_form'


class MarcsysRelator(models.Model):
    code = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    stat = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marcsys_relator'


class MassAction(models.Model):
    action_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    organisation = models.CharField(max_length=250, blank=True, null=True)
    department = models.CharField(max_length=250, blank=True, null=True)
    action_date = models.DateField(blank=True, null=True)
    place = models.CharField(max_length=250, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    action_result = models.CharField(max_length=250, blank=True, null=True)
    action_comment = models.CharField(max_length=250, blank=True, null=True)
    in_user = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mass_action'


class MasterCards(models.Model):
    master_id = models.IntegerField(blank=True, null=True)
    group_kod = models.IntegerField(blank=True, null=True)
    hier_id = models.IntegerField(blank=True, null=True)
    access_type = models.SmallIntegerField(blank=True, null=True)
    hier_type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_cards'


class MatAudio(models.Model):
    kod = models.SmallIntegerField()
    code = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=48, blank=True, null=True)
    stat = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mat_audio'


class MatElDoc(models.Model):
    kod = models.SmallIntegerField()
    code = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=48, blank=True, null=True)
    stat = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mat_el_doc'


class MatVideo(models.Model):
    kod = models.SmallIntegerField()
    code = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=48, blank=True, null=True)
    stat = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mat_video'


class Maxes(models.Model):
    jur_person_id = models.IntegerField(blank=True, null=True)
    phys_person_id = models.IntegerField(blank=True, null=True)
    doc_id = models.IntegerField(blank=True, null=True)
    card_id = models.IntegerField(blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    colcnt = models.IntegerField(blank=True, null=True)
    grpcnt = models.IntegerField(blank=True, null=True)
    party_kod = models.IntegerField(blank=True, null=True)
    request_id = models.IntegerField(blank=True, null=True)
    org_order_id = models.IntegerField(blank=True, null=True)
    item_outreason_id = models.IntegerField(blank=True, null=True)
    deliver_id = models.IntegerField(blank=True, null=True)
    profile_kod = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maxes'


class Maxes2(models.Model):
    code = models.CharField(max_length=20)
    max_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'maxes2'


class Miscprofiles(models.Model):
    profile_kod = models.IntegerField(blank=True, null=True)
    win_kod = models.SmallIntegerField(blank=True, null=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    svalue = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'miscprofiles'


class MoneyUnit(models.Model):
    kod = models.SmallIntegerField()
    short_name = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    cent_short_name = models.CharField(max_length=10, blank=True, null=True)
    cent_name = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'money_unit'


class NameList(models.Model):
    kod = models.SmallIntegerField()
    ntype = models.SmallIntegerField(blank=True, null=True)
    person_post = models.CharField(max_length=250, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'name_list'


class Options(models.Model):
    term_days = models.SmallIntegerField(blank=True, null=True)
    term_days_jur = models.SmallIntegerField(blank=True, null=True)
    dbversion = models.SmallIntegerField(blank=True, null=True)
    am_short = models.SmallIntegerField(blank=True, null=True)
    def_unit = models.SmallIntegerField(blank=True, null=True)
    upd = models.SmallIntegerField(blank=True, null=True)
    items_no_integer = models.SmallIntegerField(blank=True, null=True)
    money_name = models.CharField(max_length=10, blank=True, null=True)
    cent_name = models.CharField(max_length=10, blank=True, null=True)
    items_dashed = models.SmallIntegerField(blank=True, null=True)
    items_unique = models.SmallIntegerField(blank=True, null=True)
    udk_hier = models.IntegerField(blank=True, null=True)
    udk_separator = models.CharField(max_length=2, blank=True, null=True)
    libcipher = models.CharField(max_length=32, blank=True, null=True)
    libname = models.CharField(max_length=254, blank=True, null=True)
    use_presence_imp = models.SmallIntegerField(blank=True, null=True)
    use_presence_exp = models.SmallIntegerField(blank=True, null=True)
    itemno_separator = models.CharField(max_length=20, blank=True, null=True)
    formular_text = models.CharField(max_length=250, blank=True, null=True)
    max_resultset = models.IntegerField(blank=True, null=True)
    clnt_ver = models.IntegerField(blank=True, null=True)
    clnt_red = models.IntegerField(blank=True, null=True)
    clnt_mod = models.IntegerField(blank=True, null=True)
    check_ret_place = models.IntegerField(blank=True, null=True)
    use_partyno = models.SmallIntegerField(blank=True, null=True)
    division_colname = models.CharField(max_length=30, blank=True, null=True)
    subdiv_colname = models.CharField(max_length=30, blank=True, null=True)
    dscp_name = models.CharField(max_length=250, blank=True, null=True)
    exchange_fond = models.IntegerField(blank=True, null=True)
    confirm_getting = models.IntegerField(blank=True, null=True)
    order_to_queue = models.SmallIntegerField(blank=True, null=True)
    min_clnt_ver = models.IntegerField(blank=True, null=True)
    min_clnt_red = models.IntegerField(blank=True, null=True)
    min_clnt_mod = models.IntegerField(blank=True, null=True)
    confirm_docgetting = models.IntegerField(blank=True, null=True)
    summary_start_date = models.DateField(blank=True, null=True)
    confirm_docorder = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'options'


class Options2(models.Model):
    option_id = models.CharField(max_length=100, blank=True, null=True)
    option_value = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'options2'


class OrderChain(models.Model):
    deliver_kod = models.ForeignKey('StorageList', db_column='deliver_kod', blank=True, null=True)
    norder = models.SmallIntegerField(blank=True, null=True)
    device_kod = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_chain'


class Orders(models.Model):
    person_id = models.IntegerField(blank=True, null=True)
    person_type = models.CharField(max_length=1, blank=True, null=True)
    doc_id = models.IntegerField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    item_no = models.CharField(max_length=32, blank=True, null=True)
    place_date = models.DateTimeField(blank=True, null=True)
    device_kod = models.SmallIntegerField(blank=True, null=True)
    deliver_kod = models.SmallIntegerField(blank=True, null=True)
    last_edit_user = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class OrgOrder(models.Model):
    id = models.IntegerField()
    doc = models.ForeignKey(Document, blank=True, null=True)
    qty = models.SmallIntegerField(blank=True, null=True)
    org_id = models.IntegerField(blank=True, null=True)
    date_place = models.DateTimeField(blank=True, null=True)
    date_must = models.DateTimeField(blank=True, null=True)
    date_receive = models.DateTimeField(blank=True, null=True)
    commentt = models.CharField(max_length=200, blank=True, null=True)
    ord_status = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org_order'


class OutReasons(models.Model):
    kod = models.SmallIntegerField()
    name = models.CharField(max_length=32, blank=True, null=True)
    par_kod = models.SmallIntegerField(blank=True, null=True)
    norder = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'out_reasons'


class Party(models.Model):
    kod = models.IntegerField()
    party_no = models.CharField(max_length=10, blank=True, null=True)
    in_date = models.DateTimeField(blank=True, null=True)
    stype = models.CharField(max_length=1, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    source_name = models.CharField(max_length=254, blank=True, null=True)
    accompany_doc_date = models.DateTimeField(blank=True, null=True)
    accompany_doc_no = models.CharField(max_length=20, blank=True, null=True)
    commnt = models.CharField(max_length=250, blank=True, null=True)
    director_post = models.CharField(max_length=250, blank=True, null=True)
    director_name = models.CharField(max_length=64, blank=True, null=True)
    signer1_post = models.CharField(max_length=250, blank=True, null=True)
    signer1_name = models.CharField(max_length=64, blank=True, null=True)
    signer2_post = models.CharField(max_length=250, blank=True, null=True)
    signer2_name = models.CharField(max_length=64, blank=True, null=True)
    signer3_post = models.CharField(max_length=250, blank=True, null=True)
    signer3_name = models.CharField(max_length=64, blank=True, null=True)
    full_text = models.CharField(max_length=250, blank=True, null=True)
    last_edit_date = models.DateTimeField(blank=True, null=True)
    last_edit_user = models.CharField(max_length=30, blank=True, null=True)
    writeoff_person = models.CharField(max_length=100, blank=True, null=True)
    acquisition_type = models.IntegerField(blank=True, null=True)
    out_reason = models.IntegerField(blank=True, null=True)
    col202 = models.IntegerField(blank=True, null=True)
    col203 = models.IntegerField(blank=True, null=True)
    col206 = models.IntegerField(blank=True, null=True)
    col207 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    col208 = models.IntegerField(blank=True, null=True)
    col209 = models.IntegerField(blank=True, null=True)
    col211 = models.IntegerField(blank=True, null=True)
    col212 = models.IntegerField(blank=True, null=True)
    col213 = models.IntegerField(blank=True, null=True)
    col214 = models.IntegerField(blank=True, null=True)
    col215 = models.IntegerField(blank=True, null=True)
    col216 = models.IntegerField(blank=True, null=True)
    col217 = models.IntegerField(blank=True, null=True)
    col218 = models.IntegerField(blank=True, null=True)
    col220 = models.IntegerField(blank=True, null=True)
    col221 = models.IntegerField(blank=True, null=True)
    col222 = models.IntegerField(blank=True, null=True)
    col224 = models.IntegerField(blank=True, null=True)
    col225 = models.IntegerField(blank=True, null=True)
    signer4_name = models.CharField(max_length=64, blank=True, null=True)
    signer4_post = models.CharField(max_length=250, blank=True, null=True)
    signer5_name = models.CharField(max_length=64, blank=True, null=True)
    signer5_post = models.CharField(max_length=250, blank=True, null=True)
    signer6_name = models.CharField(max_length=64, blank=True, null=True)
    signer6_post = models.CharField(max_length=250, blank=True, null=True)
    signer7_name = models.CharField(max_length=64, blank=True, null=True)
    signer7_post = models.CharField(max_length=250, blank=True, null=True)
    signer8_name = models.CharField(max_length=64, blank=True, null=True)
    signer8_post = models.CharField(max_length=250, blank=True, null=True)
    signer9_name = models.CharField(max_length=64, blank=True, null=True)
    signer9_post = models.CharField(max_length=250, blank=True, null=True)
    signer10_name = models.CharField(max_length=64, blank=True, null=True)
    signer10_post = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party'


class PartyCond(models.Model):
    party_field_kod = models.ForeignKey('PartyFields', db_column='party_field_kod', blank=True, null=True)
    field_kod = models.IntegerField(blank=True, null=True)
    pred = models.SmallIntegerField(blank=True, null=True)
    pred_type = models.SmallIntegerField(blank=True, null=True)
    pred_value1 = models.CharField(max_length=250, blank=True, null=True)
    pred_value2 = models.CharField(max_length=50, blank=True, null=True)
    pred_value = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_cond'


class PartyFields(models.Model):
    kod = models.SmallIntegerField(primary_key=True)
    norder = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    parent_kod = models.SmallIntegerField(blank=True, null=True)
    isvert = models.SmallIntegerField(blank=True, null=True)
    inuse = models.SmallIntegerField(blank=True, null=True)
    cond_used = models.SmallIntegerField(blank=True, null=True)
    ntype = models.SmallIntegerField(blank=True, null=True)
    name2 = models.CharField(max_length=32, blank=True, null=True)
    name3 = models.CharField(max_length=32, blank=True, null=True)
    start_value = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party_fields'


class PersonCard(models.Model):
    person_id = models.IntegerField(blank=True, null=True)
    person_type = models.CharField(max_length=1, blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    get_date = models.DateTimeField(blank=True, null=True)
    return_date = models.DateTimeField(blank=True, null=True)
    must_return_date = models.DateTimeField(blank=True, null=True)
    commentt = models.CharField(max_length=128, blank=True, null=True)
    deliver_id = models.IntegerField()
    deliver_qty = models.SmallIntegerField(blank=True, null=True)
    deliver_kod = models.SmallIntegerField(blank=True, null=True)
    get_user = models.CharField(max_length=50, blank=True, null=True)
    return_user = models.CharField(max_length=50, blank=True, null=True)
    signature = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_card'


class PhysicalPerson(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=64, blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    passport_series = models.CharField(max_length=10, blank=True, null=True)
    passport_no = models.IntegerField(blank=True, null=True)
    work_place = models.CharField(max_length=150, blank=True, null=True)
    person_post = models.CharField(max_length=150, blank=True, null=True)
    in_user = models.CharField(max_length=50, blank=True, null=True)
    work_phone = models.CharField(max_length=100, blank=True, null=True)
    home_phone = models.CharField(max_length=100, blank=True, null=True)
    kod = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    mobile_phone = models.CharField(max_length=32, blank=True, null=True)
    pager_no = models.IntegerField(blank=True, null=True)
    pager_phone = models.CharField(max_length=32, blank=True, null=True)
    code = models.CharField(max_length=32, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    photo_old = models.BinaryField(blank=True, null=True)
    code_intno = models.IntegerField(blank=True, null=True)
    is_blocked = models.SmallIntegerField(blank=True, null=True)
    block_reason = models.CharField(max_length=200, blank=True, null=True)
    register_date = models.DateTimeField(blank=True, null=True)
    in_date = models.DateTimeField(blank=True, null=True)
    last_edit_date = models.DateTimeField(blank=True, null=True)
    last_edit_user = models.CharField(max_length=50, blank=True, null=True)
    spassport_no = models.CharField(max_length=15, blank=True, null=True)
    pin_code = models.CharField(max_length=250, blank=True, null=True)
    service_begdate = models.DateTimeField(blank=True, null=True)
    service_enddate = models.DateTimeField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    passport_org = models.CharField(max_length=128, blank=True, null=True)
    scomment = models.CharField(max_length=250, blank=True, null=True)
    table_id = models.CharField(max_length=30, blank=True, null=True)
    block_edit_date = models.DateTimeField(blank=True, null=True)
    block_edit_user = models.CharField(max_length=30, blank=True, null=True)
    person_status = models.CharField(max_length=1, blank=True, null=True)
    division = models.CharField(max_length=64, blank=True, null=True)
    subdivision = models.CharField(max_length=64, blank=True, null=True)
    post_type = models.CharField(max_length=20, blank=True, null=True)
    student_course = models.CharField(max_length=200, blank=True, null=True)
    speciality = models.CharField(max_length=200, blank=True, null=True)
    specialization = models.CharField(max_length=200, blank=True, null=True)
    student_group = models.CharField(max_length=100, blank=True, null=True)
    age_category = models.CharField(max_length=50, blank=True, null=True)
    social_category = models.CharField(max_length=50, blank=True, null=True)
    rfid = models.CharField(max_length=32, blank=True, null=True)
    barcode = models.CharField(max_length=32, blank=True, null=True)
    access_category = models.IntegerField(blank=True, null=True)
    person_password = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physical_person'


class PrimaryField(models.Model):
    kod = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'primary_field'


class PrintHeader(models.Model):
    kod = models.SmallIntegerField()
    hftype = models.SmallIntegerField(blank=True, null=True)
    svalue = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'print_header'


class Profilelist(models.Model):
    suser_name = models.CharField(max_length=50, blank=True, null=True)
    kod = models.IntegerField()
    name = models.CharField(max_length=64, blank=True, null=True)
    ntype = models.SmallIntegerField(blank=True, null=True)
    group_kod = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profilelist'


class PublisherList(models.Model):
    kod = models.SmallIntegerField()
    name = models.CharField(max_length=80, blank=True, null=True)
    fullname = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publisher_list'


class ReaderCategory(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=200, blank=True, null=True)
    prefix = models.CharField(max_length=20, blank=True, null=True)
    suffix = models.CharField(max_length=20, blank=True, null=True)
    digit_qty = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reader_category'


class ReaderPhoto(models.Model):
    id = models.IntegerField()
    fld_type = models.SmallIntegerField()
    norder = models.IntegerField()
    fragment01 = models.CharField(max_length=250, blank=True, null=True)
    fragment02 = models.CharField(max_length=250, blank=True, null=True)
    fragment03 = models.CharField(max_length=250, blank=True, null=True)
    fragment04 = models.CharField(max_length=250, blank=True, null=True)
    fragment05 = models.CharField(max_length=250, blank=True, null=True)
    fragment06 = models.CharField(max_length=250, blank=True, null=True)
    fragment07 = models.CharField(max_length=250, blank=True, null=True)
    fragment08 = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reader_photo'


class ReaderPhoto2(models.Model):
    id = models.IntegerField(blank=True, null=True)
    field_type = models.IntegerField(blank=True, null=True)
    fragment_order = models.IntegerField(blank=True, null=True)
    fragment_value = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reader_photo2'


class ReaderSrvPlace(models.Model):
    reader_id = models.IntegerField(blank=True, null=True)
    place_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reader_srv_place'


class ReaderVisit(models.Model):
    person_id = models.IntegerField(blank=True, null=True)
    lock_id = models.IntegerField(blank=True, null=True)
    lock_direction = models.CharField(max_length=10, blank=True, null=True)
    place_id = models.IntegerField(blank=True, null=True)
    visit_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reader_visit'


class RefCard(models.Model):
    card_id = models.IntegerField(blank=True, null=True)
    card_ref = models.IntegerField(blank=True, null=True)
    norder = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ref_card'
        unique_together = (('card_id', 'card_ref'),)


class RefDoc(models.Model):
    card_id = models.IntegerField()
    doc_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ref_doc'


class RefuseStat(models.Model):
    person_id = models.IntegerField(blank=True, null=True)
    person_type = models.CharField(max_length=1, blank=True, null=True)
    doc_id = models.IntegerField(blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    reason_kod = models.SmallIntegerField(blank=True, null=True)
    reason_string = models.CharField(max_length=64, blank=True, null=True)
    device_kod = models.SmallIntegerField(blank=True, null=True)
    deliver_kod = models.SmallIntegerField(blank=True, null=True)
    date_refuse = models.DateTimeField(blank=True, null=True)
    place_date = models.DateTimeField(blank=True, null=True)
    user_refuse = models.CharField(max_length=30, blank=True, null=True)
    refuse_type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refuse_stat'


class RefuseTypes(models.Model):
    kod = models.IntegerField()
    name = models.CharField(max_length=80, blank=True, null=True)
    is_default = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refuse_types'


class ServiceList(models.Model):
    service_id = models.IntegerField(blank=True, null=True)
    service_type = models.IntegerField(blank=True, null=True)
    place_id = models.IntegerField(blank=True, null=True)
    reader_id = models.IntegerField(blank=True, null=True)
    service_date = models.DateField(blank=True, null=True)
    service_time = models.DateTimeField(blank=True, null=True)
    number_info = models.IntegerField(blank=True, null=True)
    service_comment = models.CharField(max_length=250, blank=True, null=True)
    in_user = models.CharField(max_length=50, blank=True, null=True)
    service_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_list'


class ServicePlace(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_place'


class ServiceType(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_type'


class SpecialityList(models.Model):
    kod = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'speciality_list'


class StockList(models.Model):
    kod = models.SmallIntegerField()
    name = models.CharField(max_length=48, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_list'


class StorageList(models.Model):
    kod = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    is_distribution = models.SmallIntegerField(blank=True, null=True)
    stype = models.CharField(max_length=1, blank=True, null=True)
    reader_qty = models.IntegerField(blank=True, null=True)
    file_reader_qty = models.IntegerField(blank=True, null=True)
    short_name = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storage_list'


class SubdivisionList(models.Model):
    kod = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    division_kod = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subdivision_list'


class Tableprofile(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    profile = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tableprofile'


class TemplateBody(models.Model):
    id = models.IntegerField()
    fld_type = models.SmallIntegerField()
    norder = models.IntegerField()
    fragment01 = models.CharField(max_length=250, blank=True, null=True)
    fragment02 = models.CharField(max_length=250, blank=True, null=True)
    fragment03 = models.CharField(max_length=250, blank=True, null=True)
    fragment04 = models.CharField(max_length=250, blank=True, null=True)
    fragment05 = models.CharField(max_length=250, blank=True, null=True)
    fragment06 = models.CharField(max_length=250, blank=True, null=True)
    fragment07 = models.CharField(max_length=250, blank=True, null=True)
    fragment08 = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'template_body'


class TemplateDatasrc(models.Model):
    template_code = models.SmallIntegerField(blank=True, null=True)
    datasrc_code = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'template_datasrc'


class TemplateXml(models.Model):
    code = models.IntegerField(blank=True, null=True)
    ntype = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    body_old = models.BinaryField(blank=True, null=True)
    isdefault = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'template_xml'


class Tempor(models.Model):
    uni_kod = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tempor'


class TestTable(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?

    class Meta:
        managed = False
        db_table = 'test_table'


class Ttp(models.Model):
    id = models.IntegerField()
    dscp_id = models.IntegerField(blank=True, null=True)
    division = models.IntegerField(blank=True, null=True)
    subdivision = models.IntegerField(blank=True, null=True)
    acquisition_norm = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    student_qty = models.IntegerField(blank=True, null=True)
    student_contr_qty = models.IntegerField(blank=True, null=True)
    distribution = models.IntegerField(blank=True, null=True)
    contr_norm = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    fld102 = models.IntegerField(blank=True, null=True)
    fld103 = models.IntegerField(blank=True, null=True)
    fld104 = models.IntegerField(blank=True, null=True)
    fld105 = models.IntegerField(blank=True, null=True)
    day_from = models.IntegerField(blank=True, null=True)
    day_to = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ttp'


class TtpField(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=200, blank=True, null=True)
    norder = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ttp_field'


class TtpFieldEnum(models.Model):
    fld_id = models.IntegerField()
    enum_id = models.IntegerField()
    name = models.CharField(max_length=200, blank=True, null=True)
    norder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ttp_field_enum'


class TtphierFldorder(models.Model):
    fld_id = models.IntegerField()
    norder = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ttphier_fldorder'


class TtphierOptions(models.Model):
    fld_used_qty = models.IntegerField()
    show_unused = models.IntegerField()
    show_reader_qty = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ttphier_options'


class TypeList(models.Model):
    kod = models.SmallIntegerField()
    name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_list'


class TypicalValues(models.Model):
    value_type = models.CharField(max_length=50, blank=True, null=True)
    value_text = models.CharField(max_length=250, blank=True, null=True)
    value_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typical_values'


class UsedKod(models.Model):
    kod = models.IntegerField(blank=True, null=True)
    newkod = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'used_kod'
        unique_together = (('kod', 'newkod'),)


class UserReports(models.Model):
    kod = models.SmallIntegerField(blank=True, null=True)
    sql = models.BinaryField(blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    filename = models.CharField(max_length=100, blank=True, null=True)
    body = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_reports'


class Usergroup(models.Model):
    alias = models.CharField(max_length=50)
    groupcode = models.IntegerField(blank=True, null=True)
    isdefault = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usergroup'
        unique_together = (('alias', 'groupcode'),)


class Userlist(models.Model):
    alias = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userlist'


class UserrepAuthority(models.Model):
    rep_code = models.IntegerField()
    group_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'userrep_authority'


class Winprofiles(models.Model):
    profile_kod = models.IntegerField(blank=True, null=True)
    norder = models.SmallIntegerField(blank=True, null=True)
    win_kod = models.SmallIntegerField(blank=True, null=True)
    window_name = models.CharField(max_length=40, blank=True, null=True)
    win_type = models.SmallIntegerField(blank=True, null=True)
    win_aux_int = models.IntegerField(blank=True, null=True)
    win_aux_str = models.CharField(max_length=100, blank=True, null=True)
    win_x = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    win_y = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    win_w = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    win_h = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    win_state = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'winprofiles'
        unique_together = (('profile_kod', 'win_kod'),)


class WordIndex(models.Model):
    doc = models.ForeignKey(Document, blank=True, null=True)
    field_kod = models.SmallIntegerField(blank=True, null=True)
    word = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'word_index'

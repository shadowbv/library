#from __future__ import unicode_literals
from django.db import models


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
        db_table = 'DOCTYPE'

    def __str__(self):
        return self.name


class Document(models.Model):
    doc_type = models.SmallIntegerField()
    #doc_type = models.SmallIntegerField()
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
        db_table = 'DOCUMENT'
        ordering = ['-reg_date']
        verbose_name = "Документ"
        verbose_name_plural = "Документи"

    def __str__(self):
        return self.name


class DocItem(models.Model):
    doc_id = models.ForeignKey('Document')
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
        db_table = 'DOC_ITEM'
        ordering = ['reg_date']
        verbose_name = "Примірник"
        verbose_name_plural = "Примірники"

    def __str__(self):
        return self.item_id

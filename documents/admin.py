from django.contrib import admin

from documents.models import *


class DocumentAdmin(admin.ModelAdmin):
    #list_display = [field.name for field in Document._meta.fields]
    list_display = ["name", "author", "doc_id", "reg_date", "lang"]
    search_fields = ["author", "doc_id"]
    #list_filter = ["author"]
    #exclude = ["ADDRESS"]

    class Meta:
        model = Document

admin.site.register(Document, DocumentAdmin)

class DocItemAdmin(admin.ModelAdmin):
    #list_display = [field.name for field in Document._meta.fields]
    list_display = ["item_id", "doc_id", "reg_date"]
    search_fields = ["doc_id"]
    #list_filter = ["author"]
    #exclude = ["ITEM_INTNO", "ITEM_MAINNO", "ITEM_NO"]
    fields = ["doc_id"]

    class Meta:
        model = DocItem


admin.site.register(DocItem, DocItemAdmin)



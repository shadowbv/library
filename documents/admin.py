from django.contrib import admin

from documents.models import *


class DocumentAdmin(admin.ModelAdmin):
    #list_display = [field.name for field in Document._meta.fields]
    list_display = ["name", "author", "reg_date", "lang"]
    search_fields = ["author", "doc_id"]
    #list_filter = ["author"]
    #exclude = ["ADDRESS"]

    class Meta:
        model = Document

admin.site.register(Document, DocumentAdmin)

class DocItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DocItem._meta.fields]
    #list_display = ["item_id", "item_no", "item_intno", "reg_date"]
    #search_fields = ["doc.name"]
    #list_filter = ["author"]
    exclude = ["doc"]
    #fields = ["doc"]

    class Meta:
        model = DocItem


admin.site.register(DocItem, DocItemAdmin)


class StorageListAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StorageList._meta.fields]
    #list_display = ["item_id", "item_no", "item_intno", "reg_date"]
    #search_fields = ["doc.name"]
    #list_filter = ["author"]
    #exclude = ["doc"]
    #fields = ["doc"]

    class Meta:
        model = StorageList

admin.site.register(StorageList, StorageListAdmin)


class AuthTypeMainAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AuthTypeMain._meta.fields]
    #list_display = ["item_id", "item_no", "item_intno", "reg_date"]
    #search_fields = ["doc.name"]
    #list_filter = ["author"]
    #exclude = ["doc"]
    #fields = ["doc"]

    class Meta:
        model = AuthTypeMain

admin.site.register(AuthTypeMain, AuthTypeMainAdmin)



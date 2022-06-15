from __future__ import unicode_literals
import frappe
from frappe.utils.file_manager import save_url

def create_equipment_for_rent_item(asset_doc, method):
    if asset_doc.docstatus == 1 and (not len(frappe.get_all("Equipment for Rent", filters={
        "asset_item": asset_doc.name})) and asset_doc.create_equipment_for_rent_entry ==1) :
        eq_for_rent_item = frappe.get_doc({
            "doctype": "Equipment for Rent",
            "title": asset_doc.asset_name,
            "asset_item": asset_doc.name
        })
        eq_for_rent_item.insert(True)
        if asset_doc.image:
            attach = frappe.db.get_value("File", {"file_url": asset_doc.image}, ["file_name" ,"file_url", "is_private"],
                                         as_dict=1)
            new_file = save_url(attach.file_url, asset_doc.image, "Equipment for Rent", eq_for_rent_item.name,
                                "Home/Attachments", False)

            eq_for_rent_item.picture_attachment = new_file.file_url

            eq_for_rent_item.save()

from __future__ import unicode_literals

import frappe
import json


@frappe.whitelist()
def bulk_insert_equipment_for_rent(data):
    """

    :param kwargs:
    :return:
    """

    data = frappe._dict(json.loads(data))
    equipments_for_rent = data["equipments_for_rent"]

    for equipment_for_rent in equipments_for_rent:
        new_equipment = frappe.get_doc({
            "doctype": "Equipment for Rent",
            "title": equipment_for_rent["title"],
            "description": equipment_for_rent["description"]
        })

        new_equipment.save(True)
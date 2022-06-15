# -*- coding: utf-8 -*-
# Copyright (c) 2022, a and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class RentalBooking(Document):
	pass

def validate(self):
	print(self)

	other_bookings_start_clash = frappe.get_all("Rental Booking", filters=[
		['status', 'in', ['booked', 'out']],
		['booking_date', '>=', self.booking_date],
		['booking_date', '<=', self.return_date],
		['name', '=', self.item_to_rent],
		['docstatus', '=', 1]
	])
	other_bookings_return_clash = frappe.get_all("Rental Booking", filters=[
		['status', 'in', ['booked', 'out']],
		['return_date', '>=', self.booking_date],
		['return_date', '<=', self.return_date],
		['name', '!=', self.item_to_rent],
		['docstatus', '=', 1]
	])

	booking_clashes_as_string = []
	for booking_clash in other_bookings_start_clash:
		booking_clashes_as_string.append(booking_clash.name)

	for booking_clash in other_bookings_return_clash:
		booking_clashes_as_string.append(booking_clash.name)

	if len(other_bookings_start_clash) or len(other_bookings_return_clash):
		frappe.msgprint(
			"The booking is clashing, please change your date. (" + ", ".join(booking_clashes_as_string) + ")",
			raise_exception=1)
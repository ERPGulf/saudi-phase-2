
import frappe
from frappe import _
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.permissions import add_permission, update_permission_property



def setup(company=None, patch=True):
	make_custom_fields()
	# setup_report()
	# add_permissions()
def make_custom_fields(update=True):
    custom_fields ={
        'Address': [
			dict(fieldname='street', label='Street',
				fieldtype='Data', insert_after='address_line2'
				),
			dict(fieldname='building_no', label='Building Number',
				fieldtype='Data', insert_after='street'),
            dict(fieldname='plot_id_no', label='Plot Identification Number',
				fieldtype='Data', insert_after='building_no')
		    ],
			}

    create_custom_fields(custom_fields, ignore_validate = frappe.flags.in_patch, update=update)

# def setup_report():
# 	report_name = 'Electronic Invoice Register KSA'
# 	frappe.db.set_value("Report", report_name, "disabled", 0)

# 	if not frappe.db.get_value('Custom Role', dict(report=report_name)):
# 		frappe.get_doc(dict(
# 			doctype='Custom Role',
# 			report=report_name,
# 			roles= [
# 				dict(role='Accounts User'),
# 				dict(role='Accounts Manager')
# 			]
# 		)).insert()
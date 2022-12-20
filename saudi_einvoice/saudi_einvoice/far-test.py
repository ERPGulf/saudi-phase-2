import chilkat2
import frappe
import xmlsig
# Create some Chilkat objects and print the versions
@frappe.whitelist(allow_guest=True)
def generate_sign():
    zip = chilkat2.Zip()
    return "zip.Version"


import chilkat2
import frappe
# Create some Chilkat objects and print the versions
# @frappe.whitelist(allow_guest=True)
# def generate_sign():
#     zip = chilkat.CkZip()
#     return ("Zip: " + zip.version())
# @frappe.whitelist(allow_guest=True)
# def generate_signn():
#     return "helo"
zip = chilkat2.CkZip()
print("Zip: " + zip.version())
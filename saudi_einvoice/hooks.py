from . import __version__ as app_version

app_name = "saudi_einvoice"
app_title = "Saudi Einvoice"
app_publisher = "erpgulf"
app_description = "An app for e-invoicing in Saudi Arabia"
app_email = "support@erpgulf.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/saudi_einvoice/css/saudi_einvoice.css"
app_include_js = "/assets/saudi_einvoice/js/saudi_einvoice.js"

# include js, css files in header of web template
# web_include_css = "/assets/saudi_einvoice/css/saudi_einvoice.css"
# web_include_js = "/assets/saudi_einvoice/js/saudi_einvoice.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "saudi_einvoice/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}
doctype_js = {"Sales Invoice" : "saudi_einvoice.saudi_einvoice.sales_invoicesa.js"}
# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "saudi_einvoice.utils.jinja_methods",
#	"filters": "saudi_einvoice.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "saudi_einvoice.install.before_install"
# after_install = "saudi_einvoice.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "saudi_einvoice.uninstall.before_uninstall"
# after_uninstall = "saudi_einvoice.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "saudi_einvoice.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }
doc_events = {
    
    "Sales Invoice": {
        "after_insert": [
            "saudi_einvoice.saudi_einvoice.utils.prepare_and_attach_invoice",
         ],
         
       "on_submit": [
            "saudi_einvoice.saudi_einvoice.utils.generate_sign",
            "saudi_einvoice.saudi_einvoice.utils.generate_invoicehash",
            "saudi_einvoice.saudi_einvoice.utils.api_integrationn"
            
         ] ,
         "before_save": [
            "saudi_einvoice.saudi_einvoice.utils.update_itemised_tax_data",
            "saudi_einvoice.saudi_einvoice.setup.setup"
            
            
         ]
    },
    "Address": {
        "before_save": "saudi_einvoice.saudi_einvoice.setup.setup"
    }
}
# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"saudi_einvoice.tasks.all"
#	],
#	"daily": [
#		"saudi_einvoice.tasks.daily"
#	],
#	"hourly": [
#		"saudi_einvoice.tasks.hourly"
#	],
#	"weekly": [
#		"saudi_einvoice.tasks.weekly"
#	],
#	"monthly": [
#		"saudi_einvoice.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "saudi_einvoice.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "saudi_einvoice.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "saudi_einvoice.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"saudi_einvoice.auth.validate"
# ]

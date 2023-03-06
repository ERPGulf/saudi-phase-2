frappe.ui.form.on("Sales Invoice", "refresh", function(frm) {
    frm.add_custom_button(__("Report API"), function() {
        // When this button is clicked, do this

        console.log("helo")
        // do something with these values, like an ajax request 
        // or call a server side frappe function using frappe.call
        frm.call({
            						method: "saudi_einvoice.saudi_einvoice.utils.api_integrationn",
            						args: {
            							doc: frm.doc.name
            						},
            						callback: function(r) {
            							frm.reload_doc();
            							if(r.message) {
            								console.log(r)
            							}
            						}
            					});
            				

            // read more about $.ajax syntax at http://api.jquery.com/jquery.ajax/

        });
    });

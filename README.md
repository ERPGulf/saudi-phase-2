## Saudi Einvoice

An app for e-invoicing in Saudi Arabia

#### License

MIT

This app enables phase-2 implemetation of Saudi VAT on ERPNext.
More details about Saudi E-Inovicing phase-2 is available on Zatca website.

The purpose of this App is to enable ERPNext user to follow the steps prescribed in the Zatca website.

1- Create XML Document with UBL 2.1 Standard

2- Generate the XML file with Invoice information (Supplier, Customer, Items, calculations)

3- Generate Digest Value for XML hash

4- Generate Digest Value for XADES Signed properties.

5- Generate Signature Value

6- Adding Certificate in UBLextension

7- Generate Xades information

8- Use Zatca API to retrieve
   a- Recieve Compliance CSID from Zatca through API 
   b- Recieve Production CSID from Zatca through API 
   c- API for reporting and Clearance.
   
   Some features are still under development. We will keep updating this document. For any suggestions and support please contact support@ERPGulf.com
   we wll also update the development on on ERPGulf website. 

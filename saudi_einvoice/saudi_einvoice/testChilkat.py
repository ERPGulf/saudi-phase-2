import chilkat2

# Create some Chilkat objects and print the versions

zip = chilkat2.Zip()
print("Zip: " + zip.Version)

imap = chilkat2.Imap()
print("IMAP: " + imap.Version)

ftp = chilkat2.Ftp2()
print("FTP: " + ftp.Version)

mailman = chilkat2.MailMan()
print("POP3/SMTP: " + mailman.Version)

ssh = chilkat2.Ssh()
print("SSH: " + ssh.Version)

sftp = chilkat2.SFtp()
print("SFTP: " + sftp.Version)

rsa = chilkat2.Rsa()
print("RSA: " + rsa.Version)

http = chilkat2.Http()
print("RSA: " + http.Version)

crypt = chilkat2.Crypt2()
print("Crypt: " + crypt.Version)

xml = chilkat2.Xml()
print("XML: " + xml.Version)

sock = chilkat2.Socket()
print("Socket/SSL/TLS: " + sock.Version)

tar = chilkat2.Tar()
print("TAR: " + tar.Version)

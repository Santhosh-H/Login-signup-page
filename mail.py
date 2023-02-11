import smtplib 
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('santhoshpubg13@gmail.com','Santhoshda13')
server.sendmail('santhoshpubg13@gmail.com','santhoshhariharan1393@gmail.com','Checking for otp')
print("got")
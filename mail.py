import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('hmswebapp@gmail.com','hmswebapp123')
message = "model is created and is 97% accuracy"
s.sendmail("hmswebapp@gmail.com", "arjunbaishay89@gmail.com", message)
s.quit()

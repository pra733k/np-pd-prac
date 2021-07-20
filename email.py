#          ---------- How to Send Emails Using Python -----------


import os
import smtplib
 # instead of putting sensitive information directly into the python script,
 # we use enviornment variables
email_id = os.environ.get('gmail_id_fake_for_testing')  # grab enviornment variables from os
email_pass = os.environ.get('gmail_pass_fake_for_testing')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp: 
# using context manager,(connection is closed automatically)
# smtp is class used here with port 587
	smtp.ehlo() 
	# identifies ourselves with mail servers (is automatic, but calling it explicitly, just for security)
	smtp.starttls() 
	# excrypt the traffic
	smtp.ehlo()
	# reidentify ourselves as encrypted connection 
	smtp.login(email_id,email_pass)
	# login into your mail server
	subject = 'Trying auto-emailing system'
	body = 'You can ignore this email and get back to work.'
	msg = f'Subject: {subject}\n\n{body}' # setting up the message
	# put subject as the header
	smtp.sendmail(email_id, 'bhaskarkumar0416@gmail.com', msg) # sender,receiver,message format

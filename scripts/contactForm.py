import urllib
import urllib2

def send_mail(formdata):
  formdata['recipient'] = 'jar@jartraining.com'
   '''This function is called after receiving an HTTP POST. postdata is a dict() containing the form keys and values.'''

   # What you have to do here depends on your framework, but you probably want to filter unexpected fields
   #check for empty keys, also make sure the values are not null or empty strings
  ensure_postdata_is_safe(postdata)
  
  name = formdata['name']
  email = formdata['email']
  subject = formdata['subject']
  message = formdata['message']
  recipient = formdata['recipient']

       
   # urlencode it to the expected format
  urlenc = urllib.urlencode(postdata)
      
  try:
       # Have the server open a connection to formmail and send it on the client's behalf
    response = urllib2.urlopen('http://formmail.dreamhost.com/cgi-bin/formmail.cgi', urlenc, timeout=250)
       # If the server to server connection succeeds, let the client know
    if response.code != 200: # 200 is HTTP OK
           return redirect('failed to send message')
  except urllib2.URLError, e:
    abort(500)  # That is, send an HTTP 500 to the client
       
  return redirect('success page')
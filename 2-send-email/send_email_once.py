import os
from dotenv import load_dotenv
import yagmail

load_dotenv()

sender = 'creative.steve@gmail.com'
receiver = 'creative.steve@gmail.com'
subject = ' send email test'
contents = """
Test 1, 2, 1, 2, proper modulation
"""

yag = yagmail.SMTP(user=sender, password=os.environ['PASSWORD'])
yag.send(to=receiver, subject=subject, contents=contents)
print("Email send to " + receiver)

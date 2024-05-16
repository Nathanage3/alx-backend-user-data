# 1. Examples of Personally Identifiable Information (PII)

Personally Identifiable Information (PII) is any data that could potentially identify a specific individual. Here are some common examples:

Name: Full name, first name, last name, maiden name.

Address: Home address, email address.

Phone Numbers: Home phone number, mobile phone number.

Social Security Number (SSN): Unique identifier used for social security and tax purposes.

Driver's License Number: Issued by the government for driving privileges.

Passport Number: Identification number on a passport.

Financial Information: Credit card numbers, bank account numbers, financial records.

Biometric Data: Fingerprints, facial recognition data, iris scans.

Medical Information: Health records, health insurance details.

Date of Birth: Exact date of birth can uniquely identify an individual.

Employment Information: Employee ID, employment history, professional licenses.

Online Identifiers: IP addresses, login credentials, social media handles, cookie data. 2. How to Implement a Log Filter that Will Obfuscate PII Fields

To protect PII in logs, it is essential to implement a log filter that obfuscates or masks sensitive information. Here's a step-by-step guide on how to do this:

# a. Identify PII Fields

Determine which fields in your logs contain PII. For example, names, email addresses, phone numbers, etc.

# b. Define Obfuscation Rules

Decide how you will obfuscate each PII field. Common methods include:

Masking: Replace part of the information with asterisks (e.g., john.doe@example.com to j**\*.d**@example.com).
Redaction: Completely remove the information from the logs.
Hashing: Replace the PII with a hash value.

# c. Implement Log Filter

You can use logging libraries like log4j for Java, logging for Python, or winston for Node.js, which support custom log filters.

Example in Python using the logging module:

import logging
import re

class PiiFilter(logging.Filter):
def filter(self, record):
record.msg = self.obfuscate_pii(record.msg)
return True

def obfuscate_pii(self, message):

# Example regex patterns for PII

email*pattern = re.compile(r'[a-zA-Z0-9*.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

phone_pattern = re.compile(r'\b\d{3}[-.\s]??\d{2}[-.\s]??\d{4}\b')

message = email_pattern.sub('[EMAIL]', message)

message = phone_pattern.sub('[PHONE]', message)

return message

logger = logging.getLogger('my_logger')
logger.addFilter(PiiFilter())

logger.info('User email is john.doe@example.com and phone is 123-45-6789')
This script filters out email addresses and phone numbers in log messages.

# 3. How to Encrypt a Password and Check the Validity of an Input Password

When dealing with passwords, it is crucial to use secure hashing algorithms and proper techniques. Here's how to do it using Python's bcrypt library:

# a. Encrypt a Password

import bcrypt

def encrypt_password(password):  
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
return hashed

# Example usage

password = 'mysecretpassword'
hashed_password = encrypt_password(password)
print(hashed_password)

# b. Check Password Validity

def check_password(password, hashed):
return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Example usage

password_to_check = 'mysecretpassword'
is_valid = check_password(password_to_check, hashed_password)
print(is_valid)
Using environment variables to store database credentials is a secure practice to avoid hardcoding sensitive information in your source code. Here’s how you can do it:

# a. Set Environment Variables

Set environment variables in your operating system or in a .env file if using a library like dotenv.

In a UNIX-based system, you can set variables in your shell:

export DB_HOST='localhost'
export DB_USER='myuser'
export DB_PASSWORD='mypassword'
export DB_NAME='mydatabase'

# b. Access Environment Variables in Your Application

Here’s an example in Python using the os module to access these environment variables:

import os
import psycopg2

def get_db_connection():
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

    connection = psycopg2.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        dbname=db_name
    )
    return connection

# Example usage

conn = get_db_connection()
print("Database connection established")

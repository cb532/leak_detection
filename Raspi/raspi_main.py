import mysql.connector
import RPi.GPIO as GPIO
from mysql.connector import Error
import datetime
import os
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

db_host = os.getenv('DB_HOST')
db_database = os.getenv('DB_DATABASE')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
api_key = os.getenv('WEATHER_API_KEY')
email_pass = os.getenv('EMAIL_PASS')

# Send email function
def send_email(subject, body):
    sender_email = "INSERT EMAIL #1"
    receiver_email = "INSERT EMAIL #2"
    password = email_pass

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

    print("Email sent!")

# Function to get weather data from API
def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q=Stratford&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
   
    temp = data['main']['temp']
    weather_description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    
    return temp, weather_description, humidity

# Function to insert sensor data into the database
def insert_sensor_weather_data(sensor_value, temp, weather_description, humidity):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=db_host,
            database=db_database,
            user=db_user,
            password=db_pass)

        cursor = connection.cursor()
        query = "INSERT INTO sensor_data (sensor_value, temperature, weather_description, humidity) VALUES (%s, %s, %s, %s)"
        data = (sensor_value, temp, weather_description, humidity)
        cursor.execute(query, data)
        connection.commit()
        print("Sensor and weather data inserted successfully")
        
        if sensor_value:
            email_subject = "Alert: Water Detected!"
            email_body = f"Alert: Water detected at {datetime.datetime.now()} with temperature {temp}C, humidity {humidity}%, and weather condition: {weather_description}."
            send_email(email_subject, email_body)
        
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Sensor setup
SENSOR_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

sensor_value = bool(GPIO.input(SENSOR_PIN))

temp, weather_description, humidity = get_weather()

# Insert the data
insert_sensor_weather_data(sensor_value, temp, weather_description, humidity)

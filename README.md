LEAK DETECTION SYSTEM
Uses a Raspberry Pi water sensor to detect, collect data, and notify of leaks
---
HOW TO SETUP -

- Download contents of 'Raspi' folder onto your raspberry pi
- Install requirements "pip install mysql-connector-python RPi.GPIO requests"

- Download contents of 'MainPC' on whichever local PC you want to run the streamlit application
- Install requirements "pip install streamlit pandas sqlalchemy pymysql"

- Run a MySQL database and connect it to both machines using the enviromental variables DB_USER, DB_PASS, DB_HOST, DB_NAME
- Insert your weather api key on the raspi
- Insert two gmails and gmail app key on the raspi
- Change file paths as needed
- Setup a cron job to run the script hourly "0 * * * * /home/broderickc3/run_final_script.sh"

Now as long as your database is up, it will collect data. To view it run the streamlit application on your MainPC using "streamlit run main.py".

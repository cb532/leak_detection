# Leak Detection System

This system utilizes a Raspberry Pi equipped with a water sensor to detect leaks, collect data, and send email notifications.

## Setup Instructions

### Raspberry Pi Setup

1. **Download the Files:**
   - Download the contents of the `Raspi` folder onto your Raspberry Pi.

2. **Install Dependencies:**
   ```bash
   pip install mysql-connector-python RPi.GPIO requests

3. **Configure Environmental Variables:**
   - Open the `run_script.sh` file and replace placeholder values with your actual MySQL database credentials:
     ```bash
     export DB_HOST='insert host name'
     export DB_DATABASE='insert database name'
     export DB_USER='insert database username'
     export DB_PASS='insert database password'
     ```

4. **API and Email Setup:**
   - In the same `run_script.sh` file, insert your weather API key and email notification details:
     ```bash
     export WEATHER_API_KEY='insert weather api key'
     export EMAIL_PASS='insert email password'
     ```
   - Update the sender and receiver email addresses in the `raspi_main.py` file:
     ```python
     sender_email = "INSERT EMAIL #1"
     receiver_email = "INSERT EMAIL #2"
     ```

5. **Modify File Paths:**
   - Update file paths in the scripts as necessary for your setup.

6. **Cron Job Setup:**
   - Set up a cron job to run the script hourly:
     ```bash
     0 * * * * /home/yourusername/run_final_script.sh
     ```

### Main PC Setup

1. **Download the Files:**
   - Download the contents of the `MainPC` folder onto the PC where you want to run the Streamlit application.

2. **Install Dependencies:**
   ```bash
   pip install streamlit pandas sqlalchemy pymysql

3. **Configure Environmental Variables:**
   - Ensure your MySQL database credentials are set as environmental variables (`DB_USER`, `DB_PASS`, `DB_HOST`, `DB_NAME`).

4. **Running the Application:**
   - To view the collected data, run the Streamlit application:
   ```bash
     streamlit run main.py
     ```

### Database Setup

- Ensure a MySQL database is running and accessible to both the Raspberry Pi and your main PC.

## Troubleshooting

If you encounter issues with the system setup or operation, ensure that:
- All file paths are correctly set in your scripts.
- The MySQL database is running and the credentials provided are correct.
- Cron job is set correctly and has the right permissions to execute.
- Python dependencies are installed without conflicts.

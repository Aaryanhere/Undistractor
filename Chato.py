from plyer import notification
import time
import threading

# Function to send the initial notification
def send_initial_notification():
    title = 'DONT GET DISTRACTED !'
    message = 'Exam in 6 hrs, You better Study'
    notification.notify(
        title=title,
        message=message,
        app_icon=r"C:\Users\Aaryan\Desktop\CODE\Projects\Undistractor\heart.ico",
        timeout=5,  # Notification stays for 5 seconds
        toast=False
    )

# Function to send a follow-up notification if needed
def send_follow_up_notification():
    title = 'CLOSING ME WONT HELP!'
    message = 'You still need to study!, Aaryan cheering you ON!'
    notification.notify(
        title=title,
        message=message,
        app_icon=r"C:\Users\Aaryan\Desktop\CODE\Projects\Undistractor\heart.ico",
        timeout=5,  # Notification stays for 5 seconds
        toast=False
    )

# Function to check and send follow-up notification
def check_and_notify():
    while True:
        send_initial_notification()
        # Wait for 60 seconds before sending follow-up notification
        time.sleep(2)  # Adjust sleep time as needed
        send_follow_up_notification()
        # Sleep for 5 hours before sending the initial notification again
        time.sleep(10)  # 5 hours

# Run the notification checker in a separate thread
thread = threading.Thread(target=check_and_notify)
thread.start()

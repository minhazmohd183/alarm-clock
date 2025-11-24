import datetime
import time

# Optional: You can play a simple sound when the alarm goes off.
# This part is complex to make cross-platform in simple Python, 
# so we'll just use a print message, but you can explain the concept!

def simple_alarm_clock():
    print("--- Simple Python Alarm Clock ---")
    
    # 1. Get Alarm Time from User
    try:
        alarm_hour = int(input("Set Hour (0-23): "))
        alarm_minute = int(input("Set Minute (0-59): "))
        alarm_message = input("Set Alarm Message: ")
    except ValueError:
        print("Invalid input. Please enter whole numbers for hour and minute.")
        return

    # Check for valid time ranges
    if not (0 <= alarm_hour <= 23 and 0 <= alarm_minute <= 59):
        print("Invalid time entered. Hour must be 0-23 and Minute 0-59.")
        return

    print(f"\n✅ Alarm set for {alarm_hour:02d}:{alarm_minute:02d}. Waiting...")
    
    # 2. Start the Real-Time Check Loop
    while True:
        # Get the current time
        now = datetime.datetime.now()
        current_hour = now.hour
        current_minute = now.minute
        current_second = now.second
        
        # 3. Check if the current time matches the alarm time (ignoring seconds)
        if current_hour == alarm_hour and current_minute == alarm_minute:
            
            # --- ALARM ACTIVATION ---
            print("\n" * 5) # Print some blank lines for visual impact
            print("")
            print("🚨 🚨 🚨 ALARM! ALARM! ALARM! 🚨 🚨 🚨")
            print(f"Time is {current_hour:02d}:{current_minute:02d}")
            print(f"MESSAGE: {alarm_message}")
            print("")
            
            # Use the time.sleep() function to pause the alarm message briefly
            time.sleep(5) 
            
            # Exit the loop once the alarm is triggered
            break 

        # 4. Efficiently pause the loop
        # We only need to check the time once per second.
        time.sleep(1) 

# Run the function
simple_alarm_clock()
# triathlon_award.py
# Written by Gower Campbell
# Objective: To enhance skills by focusing on operators, arithmetic operations, and conditional logic.

# ************ Triathlon: Award Receival ************
# This program allows athletes to input their times (in minutes) for swimming, cycling, and running.
# It calculates the total time and determines the appropriate award based on the qualifying criteria.

def get_time(event_name):
    """
    Prompt the user to input the time for a specific event.
    Ensures the input is a valid number (float or int) and non-negative.
    """
    while True:
        try:
            time = float(input(f"Enter the {event_name} time (in minutes, e.g., 65.5 for 65 minutes and 30 seconds): \n"))
            if time >= 0:
                return time
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_total_time(cycling_time, running_time, swimming_time):
    """
    Calculate the total time by summing the times for all events.
    """
    return cycling_time + running_time + swimming_time

def determine_award(total_time):
    """
    Determine the award based on the total time.
    """
    if total_time < 100:
        return "Within the qualifying time: Honorary Colours"
    elif total_time <= 105:
        return "Within five minutes of the qualifying time: Honorary Half Colours"
    elif total_time <= 110:
        return "Within 10 minutes of the qualifying time: Honorary Scroll"
    else:
        return "More than 10 minutes off from the qualifying time: No Award"

def display_total_time(total_time):
    """
    Display the total time in minutes and seconds for better readability.
    """
    minutes = int(total_time)
    seconds = int((total_time - minutes) * 60)
    print(f"\nTotal time: {minutes} minutes and {seconds} seconds")

def main():
    """
    Main function to run the Triathlon Award Receival program.
    """
    print('''Triathlon: Award Receival Program
          ''')

    # Input times for each event
    cycling_time = get_time("cycling")
    running_time = get_time("running")
    swimming_time = get_time("swimming")

    # Calculate total time
    total_time = calculate_total_time(cycling_time, running_time, swimming_time)

    # Display total time
    display_total_time(total_time)

    # Determine and display the appropriate award
    award = determine_award(total_time)
    print(f"\n{award}")

# Run the program
if __name__ == "__main__":
    main()

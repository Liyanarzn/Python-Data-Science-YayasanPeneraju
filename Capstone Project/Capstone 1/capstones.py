from os.path import exists
from datetime import datetime

# Function to read booking data from file
def read_booking_data(file_name):
    bookings = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():  # Check if line is not empty
                booking = line.strip().split('|')
                bookings.append({
                    'Car': booking[0].strip(),
                    'Driver': booking[1].strip(),
                    'Customer': booking[2].strip(),
                    'Start date': booking[3].strip(),
                    'End date': booking[4].strip(),
                    'Rating Status': booking[5].strip()
                })
    return bookings

# Function to write booking data back to file
def write_booking_data(file_name, bookings):
    with open(file_name, 'w') as file:
        for booking in bookings:
            file.write(f"{booking['Car']} | {booking['Driver']} | {booking['Customer']} | {booking['Start date']} | {booking['End date']} | {booking['Rating Status']}\n")

# Function to check if rating can be given based on end date and rating status
def can_rate_booking(booking):
    if booking['Rating Status'] == 'No' and datetime.strptime(booking['End date'], '%d-%m-%Y') > datetime.strptime(booking['Start date'], '%d-%m-%Y'):
        return True
    return False

# Function to update rating status after rating given
def update_rating_status(booking):
    booking['Rating Status'] = 'Yes'

# Function to handle user input and validation
def get_user_input(prompt, data_type=str):
    while True:
        try:
            user_input = data_type(input(prompt).strip())
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")

# Function to handle rating process
def rate_journey(booking):
    rate_car = False
    rate_car = False
    while True:
        print("\nRate your journey:")
        print("==================")
        print("| 0 - Back       |")
        print("| 1 - Rate the driver  |")
        print("| 2 - Rate the car     |")
        print("| 3 - List Ratings     |")
        if rate_driver and rate_car: 
            print("| 4 - Edit Ratings     |")
        print("==================")
        choice = get_user_input("Enter choice (0-4): ", int)
        
        if choice == 0:
            break
        elif choice == 1:
            rate_driver(booking)
        elif choice == 2:
            rate_car(booking)
        elif choice == 3:
            list_ratings(booking)
        elif choice == 4:
            edit_ratings(booking)
        else:
            print("Invalid choice. Please enter a number from 0 to 4.")

# Function to handle driver rating
def rate_driver(booking):
    professionalism = get_user_input("Professionalism (1-5): ", int)
    punctuality = get_user_input("Punctuality (1-5): ", int)
    behavior = get_user_input("Behavior (1-5): ", int)
    average_rating = (professionalism + punctuality + behavior) / 3.0
    print(f"Average rating for driver {booking['Driver']}: {average_rating:.2f}")
    update_driver_rating(booking['Driver'], average_rating)

# Function to handle car rating
def rate_car(booking):
    comfort = get_user_input("Comfort (1-5): ", int)
    cleanliness = get_user_input("Cleanliness (1-5): ", int)
    average_rating = (comfort + cleanliness) / 2.0
    print(f"Average rating for car {booking['Car']}: {average_rating:.2f}")
    update_car_rating(booking['Car'], average_rating)

# Function to list ratings for the driver or car from rating.txt
def list_ratings(booking):
    print(f"\nListing ratings for driver {booking['Driver']} and car {booking['Car']}:")
    try:
        with open("rating.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                if booking['Driver'] in line or booking['Car'] in line:
                    print(line.strip())
    except Exception as e:
        print("Something went wrong when listing the ratings:", e)

# Function to edit ratings for the driver or car
def edit_ratings(booking):
    print(f"\nEditing ratings for driver {booking['Driver']} and car {booking['Car']}:")
    try:
        new_ratings = []
        with open("rating.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                if booking['Driver'] in line or booking['Car'] in line:
                    new_rating = input(f"Current rating: {line.strip()}\nEnter new rating: ").strip()
                    new_ratings.append(new_rating)
                else:
                    new_ratings.append(line.strip())
        with open("rating.txt", 'w') as file:
            for rating in new_ratings:
                file.write(f"{rating}\n")
    except Exception as e:
        print("Something went wrong when editing the ratings:", e)

# Function to update driver rating in rating.txt
def update_driver_rating(driver, rating):
    with open("rating.txt", 'a') as file:
        file.write(f"Driver: {driver} | Average Rating: {rating:.2f}\n")

# Function to update car rating in rating.txt
def update_car_rating(car, rating):
    with open("rating.txt", 'a') as file:
        file.write(f"Car: {car} | Average Rating: {rating:.2f}\n")

# Function to print booking data in a formatted table
def printBookingData(filename):
    try:
        if not exists(filename):
            print(f"The file '{filename}' does not exist.")
            return
        
        lines = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        
        print("=" * 30 + " BOOKING DATA " + "=" * 30)
        print("{:<5}{:<10}{:<15}{:<15}{:<12}{:<12}{:<15}".format(
            "No.", "Car", "Driver", "Customer", "Start date", "End date", "Rating Status"))
        print("=" * 85)
        
        for index, line in enumerate(lines):
            if index == 0:
                continue  # Skip header line
            car, driver, customer, start_date, end_date, rating_status = line.strip().split("|")
            print(f"{index:<5}{car.strip():<10}{driver.strip():<15}{customer.strip():<15}{start_date.strip():<12}{end_date.strip():<12}{rating_status.strip():<15}")

        print("=" * 85)
    except Exception as e:
        print("Something went wrong when printing booking data:", e)

# Function to generate an analytic report
def generate_analytic_report():
    try:
        driver_ratings = {}
        car_ratings = {}
        driver_trips = {}
        car_trips = {}
        
        with open("rating.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                if "Driver" in line:
                    parts = line.strip().split("|")
                    driver = parts[0].split(":")[1].strip()
                    rating = float(parts[1].split(":")[1].strip())
                    if driver in driver_ratings:
                        driver_ratings[driver].append(rating)
                        driver_trips[driver] += 1
                    else:
                        driver_ratings[driver] = [rating]
                        driver_trips[driver] = 1
                elif "Car" in line:
                    parts = line.strip().split("|")
                    car = parts[0].split(":")[1].strip()
                    rating = float(parts[1].split(":")[1].strip())
                    if car in car_ratings:
                        car_ratings[car].append(rating)
                        car_trips[car] += 1
                    else:
                        car_ratings[car] = [rating]
                        car_trips[car] = 1

        print("\nAnalytic Report")
        print("=" * 50)
        print("Driver Ratings:")
        for driver, ratings in driver_ratings.items():
            avg_rating = sum(ratings) / len(ratings)
            print(f"{driver}: Average Rating = {avg_rating:.2f}, Trips = {driver_trips[driver]}")
        
        print("\nCar Ratings:")
        for car, ratings in car_ratings.items():
            avg_rating = sum(ratings) / len(ratings)
            print(f"{car}: Average Rating = {avg_rating:.2f}, Trips = {car_trips[car]}")
        print("=" * 50)
    except Exception as e:
        print("Something went wrong when generating the analytic report:", e)

# Function to run the rating system
def run_rating_system():
    booking_file = "booking.txt"

    while True:
        print("\nMain Menu:")
        print("==================")
        print("| 0 - Exit       |")
        print("| 1 - List       |")
        print("| 2 - Add Rating |")
        print("| 3 - Analytics  |")
        print("==================")
        choice = get_user_input("Choice [0,1,2,3]: ", int)

        if choice == 0:
            print("Thank you for using the rating system.")
            break
        elif choice == 1:
            printBookingData(booking_file)
        elif choice == 2:
            # Read booking data from file
            bookings = read_booking_data(booking_file)

            # Display bookings that can be rated
            print("\nBookings available for rating:")
            for index, booking in enumerate(bookings):
                if can_rate_booking(booking):
                    print(f"{index + 1}. Car: {booking['Car']} | Driver: {booking['Driver']} | Customer: {booking['Customer']} | Start date: {booking['Start date']} | End date: {booking['End date']}")
            
            # Get user input to select a booking to rate
            while True:
                try:
                    choice = int(input("\nEnter the index of the booking you want to rate (1, 2, ...): ").strip()) - 1
                    selected_booking = bookings[choice]
                    if can_rate_booking(selected_booking):
                        break
                    else:
                        print("Invalid selection. Please choose a booking that can be rated.")
                except (ValueError, IndexError):
                    print("Invalid input. Please enter a valid index.")
            
            # Perform rating for the selected booking
            rate_journey(selected_booking)

            # Update rating status in bookings
            update_rating_status(selected_booking)
            
            # Write updated booking data back to file
            write_booking_data(booking_file, bookings)
            
            print("\nAll done. Thank you for your rating!")
        elif choice == 3:
            generate_analytic_report()
        else:
            print("Invalid choice. Please enter a number from 0 to 3.")

# Run the rating system
run_rating_system()
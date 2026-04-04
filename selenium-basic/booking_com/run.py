from booking.booking import Booking

bot = Booking()
bot.web_page()
bot.exit_modals()
bot.change_currency(currency="IDR")

destination = input("Where your destination to go? (e.g. Jakarta): ")
check_in = input("What is your check IN date?" + " (YYYY-MM-DD): ")
check_out = input("What is your check OUT date?" + " (YYYY-MM-DD): ")

adults = int(input("How many adults? "))
children = int(input("How many children? "))

children_age = []
for i in range(children):
    while True:
        age = int(input(f"What is child {i+1} age? "))
        if 0 <= age <= 17:
            children_age.append(age)
            break
        print("Invalid Age. Children age must be between 0-17")

rooms = int(input("How many rooms? "))

bot.select_place_to_go(destination)
bot.select_dates(check_in_date=check_in, check_out_date=check_out)
bot.select_guest(
    adults,
    children,
    children_age=children_age,
    rooms=rooms
)
bot.pets_toggle()
bot.done_button()
bot.click_search()

# bot.exit_modals() # Un-Comment if there is a popup modal 

bot.apply_filtration()

input("Press enter to close...")
bot.quit()
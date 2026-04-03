from booking.booking import Booking

bot = Booking()
bot.web_page()
bot.exit_modals()
bot.change_currency(currency="IDR")

destination = input("Where your destination to go?") # TODO: Clue untuk mengisi tiap input
check_in = input("What is your check IN date?")
check_out = input("What is your check OUT date?")

adults = int(input("How many adults?"))
children = int(input("How many children?"))

children_age = []
for i in range(children):
    age = int(input(f"What is child {i+1} age?"))
    children_age.append(age)
    # TODO: Throw exception for children age > 17 < 18

rooms = int(input("How many rooms?"))

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
bot.exit_modals()

bot.apply_filtration()

input("Press enter to close...")
bot.quit()
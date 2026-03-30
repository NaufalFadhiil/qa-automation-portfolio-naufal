from booking.booking import Booking

bot = Booking()
bot.web_page()
bot.exit_modals()
bot.change_currency(currency="IDR")
bot.select_place_to_go('Jakarta')
bot.select_dates('2026-04-10', '2026-04-12')
bot.select_guest(adults= 4, children= 3, children_age= [8, 15, 17], rooms= 3)
bot.pets_toggle()
bot.done_button()
bot.click_search()

input("Press enter to close...")
bot.quit() 
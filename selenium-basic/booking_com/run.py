from booking.booking import Booking

bot = Booking()
bot.web_page()
bot.exit_modals()
bot.change_currency(currency="IDR")
bot.select_place_to_go('Jakarta')
bot.select_dates('2026-03-27', '2026-04-01')
bot.select_guest(adults= 4, children= 3, children_age= [8, 15, 17])

input("Press enter to close...")
bot.quit() 
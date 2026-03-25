from booking.booking import Booking

bot = Booking()
bot.web_page()
bot.exit_modals()
bot.change_currency(currency="IDR")
bot.select_place_to_go('Jakarta')
bot.select_dates('2026-03-23', '2026-03-25')
bot.select_guest(adults= 5)

input("Press enter to close...")
bot.quit()
from booking.booking import Booking

bot = Booking()
bot.web_page()
bot.exit_modals()
bot.change_currency(currency="IDR")
bot.select_place_to_go('Jakarta')

input("Press enter to close...")
bot.quit()
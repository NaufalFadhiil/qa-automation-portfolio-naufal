from booking.booking import Booking

bot = Booking()
bot.web_page()
bot.exit_modals()
bot.change_currency("USD")

input("Press enter to close...")
bot.quit()

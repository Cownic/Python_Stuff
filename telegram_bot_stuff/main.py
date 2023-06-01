from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5952404736:AAFFTZrmndkMoniSJGVJba2MpnVu-VlDwbA", use_content = "True")

# used to display the first convosation whenever the user press start
def start(update: Update , context: CallbackContext):
  update.message.reply_text("Enter the text you want to show to the user whenever they start the bot")
  
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /youtube - To get the youtube URL
    /linkedin - To get the LinkedIn profile URL
    /gmail - To get gmail URL
    /geeks - To get the GeeksforGeeks URL""")
  
  
def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Your gmail link here (I am not\
        giving mine one for security reasons)")
  
  
def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("Youtube Link =>\
    https://www.youtube.com/")
  
  
def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "LinkedIn URL => \
        https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/")
  
  
def geeks_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "GeeksforGeeks URL => https://www.geeksforgeeks.org/")
  
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))
  
updater.start_polling()


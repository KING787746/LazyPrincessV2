import pymongo
import telebot

# Replace 'your_token' with your actual bot token
bot = telebot.TeleBot('5621047664:AAHFZPz2lGFzUC6gzKZJHiR7syXw_wfCtu8')

# Replace 'your_channel_id' with the actual ID of your channel
channel_id = '-1001939652477'

# Configure MongoDB connection
client = pymongo.MongoClient('mongodb+srv://psychoexpertz78:psychoexpertz78@kingtry.prck45x.mongodb.net/?retryWrites=true&w=majority')
db = client['KINGTRY']
collection = db['Telegram_files']

@bot.message_handler(commands=['getmovies'])
def get_movies(message):
    # Retrieve all movie files from the MongoDB collection
    movies = collection.find()

    # Send each movie file to your channel
    for movie in movies:
        file_url = movie['file_url']
        caption = movie['movie_name']

        bot.send_document(channel_id, file_url, caption=caption)

# Start the bot
bot.polling()


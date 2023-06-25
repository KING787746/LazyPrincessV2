import sqlite3
import telebot

# Replace 'your_database_link' with the actual link or path to your database
database_link = ''mongodb+srv://psychoexpertz78:psychoexpertz78@kingtry.prck45x.mongodb.net/?retryWrites=true&w=majority'

# Replace 'your_channel_id' with the actual ID of your channel
channel_id = '-1001939652477'

# Create a Telegram bot instance
bot = telebot.TeleBot('5621047664:AAHFZPz2lGFzUC6gzKZJHiR7syXw_wfCtu8')

@bot.message_handler(commands=['getmovies'])
def get_movies(message):
    # Establish a connection to the database
    conn = sqlite3.connect(database_link)
    cursor = conn.cursor()

    # Fetch all movies from the database
    cursor.execute("SELECT movie_name FROM movies")
    movies = cursor.fetchall()

    # Close the database connection
    cursor.close()
    conn.close()

    # Send the movies' names to your channel
    if movies:
        movie_list = '\n'.join([movie[0] for movie in movies])
        bot.send_message(channel_id, f"Here are all the movies:\n{movie_list}")
    else:
        bot.send_message(channel_id, "No movies found in the database.")

# Start the bot
bot.polling()

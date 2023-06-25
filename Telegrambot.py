import telebot

# Replace 'your_token' with your actual bot token
bot = telebot.TeleBot('5621047664:AAHFZPz2lGFzUC6gzKZJHiR7syXw_wfCtu8')

# Replace 'your_channel_id' with the actual ID of your channel
channel_id = '-1001939652477'

@bot.message_handler(commands=['getmovies'])
def get_movies(message):
    # Replace 'path_to_movie_files' with the actual path to your movie files directory
    movie_files_path = 'path_to_movie_files'

    # Get a list of all movie files in the directory
    import os
    movie_files = [f for f in os.listdir(movie_files_path) if os.path.isfile(os.path.join(movie_files_path, f))]

    # Send each movie file to your channel
    for movie_file in movie_files:
        # Get the full file path
        file_path = os.path.join(movie_files_path, movie_file)

        # Open and send the movie file
        with open(file_path, 'rb') as file:
            bot.send_document(channel_id, file)

# Start the bot
bot.polling()

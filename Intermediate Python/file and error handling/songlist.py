# Dictionary containing liked songs and artists
liked_songs = {
    'Bad Habits': 'Ed Sheeran',
    "I'm Just Ken": 'Ryan Gosling',
    'Mastermind': 'Taylor Swift',
    'Uptown Funk': 'Mark Ronson ft. Bruno Mars',
    'Ghost': 'Justin Bieber'
}

# Function to write songs to a file
def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, 'w') as file:
        file.write("Liked Songs:\n")  # Write header
        for song, artist in liked_songs.items():
            file.write(f"{song} by {artist}\n")  # Write each song entry

# Write the songs to file
write_liked_songs_to_file(liked_songs, 'liked_songs.txt')

# Read and display the file contents
with open('liked_songs.txt', 'r') as file:
    content = file.read()
    print(content)  # Print the contents to console
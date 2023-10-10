from pytube import Playlist

while True:
    # Prompt the user to enter a YouTube playlist URL
    playlist_url = input("Enter the URL of the YouTube playlist (or type 'exit' to terminate): ")

    if playlist_url.lower() == 'exit':
        break

    try:
        # Create a Playlist object
        playlist_obj = Playlist(playlist_url)

        # Extract video titles along with their numbers
        video_titles = [f"{i+1}. {video.title}" for i, video in enumerate(playlist_obj.videos)]

        # Define the output file name based on the playlist title
        playlist_title = playlist_obj.title
        output_file = f"{playlist_title}_titles.txt"

        # Write video titles to a text file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write("\n".join(video_titles))

        print(f"{len(video_titles)} video titles have been saved to {output_file}.\n")
    except Exception as e:
        print(f"An error occurred: {str(e)}\n")

    # Ask the user if they want to continue
    while True:
        user_choice = input("Do you want to fetch another playlist? (yes/no): ").strip().lower()
        if user_choice in ('yes', 'no'):
            break
        else:
            print("Please enter 'yes' or 'no'.")

    if user_choice == 'no':
        break

print("Script terminated.")

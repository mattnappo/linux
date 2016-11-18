import webbrowser
inputter = input("Enter song name and artist: ")
webbrowser.open("https://www.youtube.com/results?search_query=" + inputter)
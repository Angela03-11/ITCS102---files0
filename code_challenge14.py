print("LIST YOUR FAVORITE ANIME\n")

anime_lists = [ ]

while True:
    title = input("Enter the title of your favorite anime (type 'exit' to finish): ")
    
    if title == "exit":
        print("\nExiting the program... Otaku!")
        break
    else:
        anime_lists.append(title)
        print(f"'{title}' has been successfully added to your anime collection.")
   
print("Lists of your favorite anime: ")
for anime in anime_lists:
        print(f" - {anime}")
        


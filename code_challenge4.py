print("Welcome to the Manga Reader Recommender!")                     
print("Answer a few questions to find your next read.")
genre = input("What genre do you prefer? (sci-fi, romance, horror, action): ")                                                                  
duration = input("Do you want the manga to be (short, medium, or long): ")  
decade = input("From which decade would you like it? (2000s, 2010s, 2020s): ")
reco = ("We Recommend: ")
if (genre == "sci-fi" or genre == "Sci-fi") and (duration == "short" or duration == "Short") and decade == "2000s":
	print(reco, "Alive by Tsutomu Nihei!")
if (genre == "sci-fi" or genre == "Sci-Fi") and (duration == "short" or duration == "Short") and decade == "2010s":
	print(reco, "Biomega! by Tsutomu Nihei")
if (genre == "sci-fi" or genre == "Sci-Fi") and (duration == "short" or duration == "Short") and decade == "2020s":
	print(reco, "The Space-Time Painter! by Hai Ya")
if (genre == "sci-fi" or genre == "Sci-Fi") and (duration == "medium" or duration == "Medium") and decade == "2000s":                             
        print(reco, "Dogs: Prelude! by Shirow Miwa")
if (genre == "sci-fi" or genre == "Sci-Fi") and (duration == "medium" or duration == "Medium") and decade == "2010s":
        print(reco, "Dimension W! by Yūji Iwahara")
if (genre == "sci-fi" or genre == "Sci-Fi") and (duration == "medium" or duration == "Medium") and decade == "2020s":                             
        print("Sorry, As of now, there are no medium-length sci-fi manga from the 2020s. You may choose another.")                                  
if (genre == "sci-fi" or genre == "Sci-Fi") and (duration == "long" or duration == "Long") and decade == "2000s":
        print(reco, "Gantz! by Hiroya Oku")   
if (genre == "sci-fi" or genre == "Sci-Fi") and (duration == "long" or duration == "Long") and decade == "2010s":                                   
        print(reco, "Alice in Borderland! by Haro Aso")
if (genre == "sci-fi" or genre == "Sci-Fi") and (duration == "long" or duration == "Long") and decade == "2020s":                                  
        print(reco, "Chainsaw Man! by Tatsuki Fujimoto")                                                                   
if (genre == "romance" or genre == "Romance") and (duration == "short" or duration == "Short") and decade == "2000s":                               
        print(reco, "Kare First Love! by Kaho Miyasaka")                                                                                           
if (genre == "romance" or genre == "Romance") and (duration == "short" or duration == "Short") and decade == "2010s":                               
        print(reco, "Ojousama no Untenshu! by Keiko Ishihara")                                                                                     
if (genre == "romance" or genre == "Romance") and (duration == "short" or duration == "Short") and decade == "2020s":                              
        print(reco, "Kimi wa Girlfriend! by Aya Oda")
if (genre == "romance" or genre == "Romance") and (duration == "medium" or duration == "Medium") and decade == "2000s":                            
        print(reco, "Lovely Complex! by Aya Oda")                                                                                                   
if (genre == "romance" or genre == "Romance") and (duration == "medium" or duration == "Medium") and decade == "2010s":                             
        print(reco, "Ao Haru Ride! by lo Sakisaka")                                                                                                 
if (genre == "romance" or genre == "Romance") and (duration == "medium" or duration == "Medium") and decade == "2020s":                            
        print(reco, "My Dress-Up Darling! by Shinichi Fukuda")
if (genre == "romance" or genre == "Romance") and (duration == "long" or duration == "Long") and decade == "2000s":
        print(reco, "Boys Over Flowers! by Yoko Kamio")
if (genre == "romance" or genre == "Romance") and (duration == "long" or duration == "Long") and decade == "2010s":
        print(reco, "Kaguya-sama: Love is War! by Aka Akasaka")
if (genre == "romance" or genre == "Romance") and (duration == "long" or duration == "Long") and decade == "2020s":
	print(reco, "Oshi no Ko! by Aka Akasaka, and Mengo Yokoyari")
if (genre == "horror" or genre == "Horror") and (duration == "short" or duration == "Short") and decade == "2000s":
        print(reco, "Fuan no Tane! by Masaaki Nakayama")
if (genre == "horror" or genre == "Horror") and (duration == "short" or duration == "Short") and decade == "2010s":
        print(reco, "Tomie! by Funji lto ")
if (genre == "horror" or genre == "Horror") and (duration == "short" or duration == "Short") and decade == "2020s":
        print(reco, "Junji Ito Collection! by Junji lto")
if (genre == "horror" or genre == "Horror") and (duration == "medium" or duration == "Medium") and decade == "2000s":
        print(reco, "Uzumaki! by Junji lto")
if (genre == "horror" or genre == "Horror") and (duration == "medium" or duration == "Medium") and decade == "2010s":
        print(reco, "Parasyte! by Hitoshi Iwaaki")
if (genre == "horror" or genre == "Horror") and (duration == "medium" or duration == "Medium") and decade == "2020s":
        print(reco, "Chainsaw Man! by Tatsuki Fujimoto")
if (genre == "horror" or genre == "Horror") and (duration == "long" or duration == "Long") and decade == "2000s":
        print(reco, "Hellsing! by Kouta Hirano")
if (genre == "horror" or genre == "Horror") and (duration == "long" or duration == "Long") and decade == "2010s":
        print(reco, "Ajin! by Gamon Sakurai")
if (genre == "horror" or genre == "Horror") and (duration == "long" or duration == "Long") and decade == "2020s":
        print(reco, "The Ghostly Doctor! by Geum Mi-kyung")
if (genre == "action" or genre == "Action") and (duration == "short" or duration == "Short") and decade == "2000s":
        print(reco, "Trigun! by Yasuhiro Nightow")
if (genre == "action" or genre == "Action") and (duration == "short" or duration == "Short") and decade == "2010s":
        print(reco, "One Punch Man! by ONE, and Yusuke Murata")
if (genre == "action" or genre == "Action") and (duration == "short" or duration == "Short") and decade == "2020s":
        print(reco, "Jujutsu Kaisen! by Gege Akutamk")
if (genre == "action" or genre == "Action") and (duration == "medium" or duration == "Medium") and decade == "2000s":
        print(reco, "Fullmetal Alchemist! by Hiromu Arakawa")
if (genre == "action" or genre == "Action") and (duration == "medium" or duration == "Medium") and decade == "2010s":
        print(reco, "Attack on Titan! by Hajime Isayama")
if (genre == "action" or genre == "Action") and (duration == "medium" or duration == "Medium") and decade == "2020s":
        print(reco, "Demon Slayer! by Koyoharu Gotouge")
if (genre == "action" or genre == "Action") and (duration == "long" or duration == "Long") and decade == "2000s":
        print(reco, "Naruto! by Masahi Kishimoto")
if (genre == "action" or genre == "Action") and (duration == "long" or duration == "Long") and decade == "2010s":
        print(reco, "Bleach! by Tite Kubo")
if (genre == "action" or genre == "Action") and (duration == "long" or duration == "Long") and decade == "2020s":
        print(reco, "My Hero Academia! by Kohei Horikoshi")

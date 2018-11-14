# -*- coding: utf-8 -*-

#importing media.py file 
import media
#importing fresh_tomatoes.py file
import fresh_tomatoes

EkThaTiger = media.Movie("Ek Tha Tiger",
	"The plot centers on an Indian spy (RAW) code-named Tiger who falls in love with a Pakistani spy (ISI) during an investigation and how Tiger's ideology and principles change over time",
	"https://upload.wikimedia.org/wikipedia/en/2/2d/Ek_Tha_Tiger_theatrical_poster.jpg",
	"https://www.youtube.com/watch?v=5-nmEOyF_tc","15 August 2012","133 minutes","350 crore")

TigerZindaHai = media.Movie("Tiger Zinda Hai",
	"RAW Agent Tiger joins forces with Zoya, a Pakistani spy, in order to rescue a group of nurses who are held hostage by a terrorist organisation.",
	"https://upload.wikimedia.org/wikipedia/en/5/5e/Tiger_Zinda_Hai_-_Poster.jpg",
	"https://www.youtube.com/watch?time_continue=1&v=ePO5M5DE01I","22 December 2017","161 minutes","570.32 crore")

Kick=media.Movie("Kick",
	"A slippery thief (Salman Khan) plays an important part in the lives of a psychiatrist (Jacqueline Fernandez) and her prospective husband (Randeep Hooda), a police officer from India.",
	"https://upload.wikimedia.org/wikipedia/en/b/b6/Kick_%282014_film%29_Official_release_poster.jpg",
	"https://www.youtube.com/watch?v=u-j1nx_HY5o","25 July 2014","146 minutes","4.02 billion")

Sultan=media.Movie("Sultan",
	"After the death of his son, Sultan Ali Khan, a middle-aged wrestler, gives up the sport. Years later, he sets out to revive his career as he needs the prize money and wants to regain his lost respect.",
	"https://upload.wikimedia.org/wikipedia/en/1/1f/Sultan_film_poster.jpg",
	"https://www.youtube.com/watch?v=wPxqcq6Byq0","6 July 2016","170 minutes","589.25 crore")

BajrangiBhaijaan=media.Movie("Bajrangi Bhaijaan",
	"Pavan, a devoted follower of Lord Hanuman, faces numerous challenges when he tries to reunite Munni with her family in Pakistan after she gets lost while travelling back home with her mother.",
	"https://upload.wikimedia.org/wikipedia/en/d/dd/Bajrangi_Bhaijaan_Poster.jpg",
	"https://www.youtube.com/watch?v=vyX4toD395U","17 July 2015","159 minutes","839.19 crore")

Wanted=media.Movie("Wanted",
	"Radhe is a ruthless gangster who will kill anyone for money. He is attracted towards Jhanvi, a middle class girl, who does not approve of his work and wants him to change.",
	"https://upload.wikimedia.org/wikipedia/en/2/26/Wanted7.jpg",
	"https://www.youtube.com/watch?v=fxm4KcKDQl0","18 September 2009","154 minutes","130 crore")

movies = [EkThaTiger, TigerZindaHai, Kick, Sultan, BajrangiBhaijaan, Wanted]

fresh_tomatoes.open_movies_page(movies)

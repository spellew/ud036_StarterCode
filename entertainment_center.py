# coding: utf-8
import fresh_tomatoes
import media

# The following lines store a Movie instance in a variable. These
# instances are initiated with data, which will be later available from
# the object. For each instance, the data we pass will be the movie title,
# then the rating, then the description, then the poster, then the
# trailer. We then store all of these instances in a list.
the_avengers = media.Movie(
    "The Avengers",
    media.Movie.VALID_RATINGS[2],
    "When Thor's evil brother, Loki (Tom Hiddleston), gains access to the "
    "unlimited power of the energy cube called the Tesseract, Nick Fury "
    "(Samuel L. Jackson), director of S.H.I.E.L.D., initiates a superhero "
    "recruitment effort to defeat the unprecedented threat to Earth. Joining "
    "Fury's \"dream team\" are Iron Man (Robert Downey Jr.), Captain America "
    "(Chris Evans), the Hulk (Mark Ruffalo), Thor (Chris Hemsworth), the "
    "Black Widow (Scarlett Johansson) and Hawkeye (Jeremy Renner).",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
    "https://www.youtube.com/watch?v=VnLnkwpIBpA")
star_wars = media.Movie(
    "Star Wars: Episode IV – A New Hope",
    media.Movie.VALID_RATINGS[1],
    "The Imperial Forces -- under orders from cruel Darth Vader "
    "(David Prowse) -- hold Princess Leia (Carrie Fisher) hostage, in their "
    "efforts to quell the rebellion against the Galactic Empire. Luke "
    "Skywalker (Mark Hamill) and Han Solo (Harrison Ford), captain of the "
    "Millennium Falcon, work together with the companionable droid duo R2-D2 "
    "(Kenny Baker) and C-3PO (Anthony Daniels) to rescue the beautiful "
    "princess, help the Rebel Alliance, and restore freedom and justice to "
    "the Galaxy.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/8/87/StarWarsMoviePoster1977.jpg/220px-StarWarsMoviePoster1977.jpg",  # noqa
    "https://www.youtube.com/watch?v=1g3_CFmnU7k")
harry_potter = media.Movie(
    "Harry Potter and the Deathly Hallows – Part 2",
    media.Movie.VALID_RATINGS[2],
    "A clash between good and evil awaits as young Harry (Daniel Radcliffe), "
    "Ron (Rupert Grint) and Hermione (Emma Watson) prepare for a final "
    "battle against Lord Voldemort (Ralph Fiennes). Harry has grown into a "
    "steely lad on a mission to rid the world of evil. The friends must "
    "search for the Horcruxes that keep the dastardly wizard immortal. "
    "Harry and Voldemort meet at Hogwarts Castle for an epic showdown where "
    "the forces of darkness may finally meet their match.",
    "https://m.media-amazon.com/images/M/MV5BMjIyZGU4YzUtNDkzYi00ZDRhLTljYzctYTMxMDQ4M2E0Y2YxXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_UX182_CR0,0,182,268_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=5NYt1qirBWg")
batman = media.Movie(
    "The Dark Knight Rises",
    media.Movie.VALID_RATINGS[2],
    "It has been eight years since Batman (Christian Bale), in collusion "
    "with Commissioner Gordon (Gary Oldman), vanished into the night. "
    "Assuming responsibility for the death of Harvey Dent, Batman "
    "sacrificed everything for what he and Gordon hoped would be the greater "
    "good. However, the arrival of a cunning cat burglar (Anne Hathaway) and "
    "a merciless terrorist named Bane (Tom Hardy) force Batman out of exile "
    "and into a battle he may not be able to win.",
    "https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=GokKUqLcvD8")
transformers = media.Movie(
    "Transformers: Dark of the Moon",
    media.Movie.VALID_RATINGS[2],
    "Sam Witwicky (Shia LaBeouf) and his new girlfriend, Carly (Rosie "
    "Huntington-Whiteley), join the fray when the evil Decepticons renew "
    "their longstanding war against the Autobots. Optimus Prime (Peter "
    "Cullen) believes that resurrecting ancient Transformer Sentinel Prime "
    "(Leonard Nimoy), once the leader of the Autobots, may lead to victory. "
    "That decision, however, has devastating consequences; the war appears "
    "to tip in favor of the Decepticons, leading to a climactic battle in "
    "Chicago.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/b/bf/Transformers_dark_of_the_moon_ver5.jpg/220px-Transformers_dark_of_the_moon_ver5.jpg",  # noqa
    "https://www.youtube.com/watch?v=kHRf01Gjosk")
toy_story_3 = media.Movie(
    "Toy Story 3",
    media.Movie.VALID_RATINGS[0],
    "With their beloved Andy preparing to leave for college, Woody (Tom "
    "Hanks), Buzz Lightyear (Tim Allen), Jessie (Joan Cusack), and the rest "
    "of the toys find themselves headed for the attic but mistakenly wind up "
    "on the curb with the trash. Woody's quick thinking saves the gang, but "
    "all but Woody end up being donated to a day-care center. Unfortunately, "
    "the uncontrollable kids do not play nice, so Woody and the gang make "
    "plans for a great escape.",
    "https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=ZZv1vki4ou4")
coco = media.Movie(
    "Coco",
    media.Movie.VALID_RATINGS[1],
    "Despite his family's generations-old ban on music, young Miguel dreams "
    "of becoming an accomplished musician like his idol Ernesto de la Cruz. "
    "Desperate to prove his talent, Miguel finds himself in the stunning and "
    "colorful Land of the Dead. After meeting a charming trickster named "
    "Héctor, the two new friends embark on an extraordinary journey to "
    "unlock the real story behind Miguel's family history.",
    "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=Rvr68u6k5sI")
titanic = media.Movie(
    "Titanic",
    media.Movie.VALID_RATINGS[2],
    "James Cameron's \"Titanic\" is an epic, action-packed romance set "
    "against the ill-fated maiden voyage of the R.M.S. Titanic; the pride "
    "and joy of the White Star Line and, at the time, the largest moving "
    "object ever built. She was the most luxurious liner of her era -- the "
    "\"ship of dreams\" -- which ultimately carried over 1,500 people to "
    "their death in the ice cold waters of the North Atlantic in the early "
    "hours of April 15, 1912.",
    "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
    "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")
spider_man_3 = media.Movie(
    "Spider-Man 3",
    media.Movie.VALID_RATINGS[2],
    "Peter Parker (Tobey Maguire) and M.J. (Kirsten Dunst) seem to finally "
    "be on the right track in their complicated relationship, but trouble "
    "looms for the superhero and his lover. Peter's Spider-Man suit turns "
    "black and takes control of him, not only giving Peter enhanced power "
    "but also bringing out the dark side of his personality. Peter must "
    "overcome the suit's influence as two supervillains, Sandman and Venom, "
    "rise up to destroy him and all those he holds dear.",
    "https://upload.wikimedia.org/wikipedia/en/7/7a/Spider-Man_3%2C_International_Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=wPosLpgMtTY")
shrek_2 = media.Movie(
    "Shrek 2",
    media.Movie.VALID_RATINGS[1],
    "After returning from their honeymoon and showing home movies to their "
    "friends, Shrek and Fiona learn that her parents have heard that she has "
    "married her true love and wish to invite him to their kingdom, called "
    "Far Far Away. The catch is: Fiona's parents are unaware of the curse "
    "that struck their daughter and have assumed she married Prince "
    "Charming, not a 700-pound ogre with horrible hygiene and a talking "
    "donkey pal.",
    "https://upload.wikimedia.org/wikipedia/en/b/b9/Shrek_2_poster.jpg",
    "https://www.youtube.com/watch?v=1_uc1s3kLzo")
finding_nemo = media.Movie(
    "Finding Nemo",
    media.Movie.VALID_RATINGS[0],
    "Marlin (Albert Brooks), a clown fish, is overly cautious with his son, "
    "Nemo (Alexander Gould), who has a foreshortened fin. When Nemo swims "
    "too close to the surface to prove himself, he is caught by a diver, and "
    "horrified Marlin must set out to find him. A blue reef fish named Dory "
    "(Ellen DeGeneres) -- who has a really short memory -- joins Marlin and "
    "complicates the encounters with sharks, jellyfish, and a host of ocean "
    "dangers. Meanwhile, Nemo plots his escape from a dentist's fish tank.",
    "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
    "https://www.youtube.com/watch?v=SPHfeNgogVs")
the_lion_king = media.Movie(
    "The Lion King",
    media.Movie.VALID_RATINGS[0],
    "This Disney animated feature follows the adventures of the young lion "
    "Simba (Zoe Leader), the heir of his father, Mufasa (Ernie Sabella). "
    "Simba's wicked uncle, Scar (Rowan Atkinson), plots to usurp Mufasa's "
    "throne by luring father and son into a stampede of wildebeests. But "
    "Simba escapes, and only Mufasa is killed. Simba returns as an adult "
    "(Jeremy Irons) to take back his homeland from Scar with the help of "
    "his friends Timon (Jonathan Taylor Thomas) and Pumbaa (Cheech Marin).",
    "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
    "https://www.youtube.com/watch?v=zx3LT_G3cIA")
movies = [
    the_avengers,
    star_wars,
    harry_potter,
    batman,
    transformers,
    toy_story_3,
    coco,
    titanic,
    spider_man_3,
    shrek_2,
    finding_nemo,
    the_lion_king]

# This line uses the open_movies_page function we imported from
# fresh_tomatoes.py. This function takes the movies list as an argument,
# then displays each movie on a custom made html page, using the
# webbrowser module. Some functions from fresh_tomatoes.py were edited.
# Now, a movie's rating will be shown, and CSS grid is used to display
# movies.
fresh_tomatoes.open_movies_page(movies)

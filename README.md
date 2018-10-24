This is a simple movie trivia app made with Python, HTML, Flask and Redis.
The CreateEntry page asks for a movie title, the year it was made and the rating it received.
Once this info is submitted, you can enter more movies by refreshing the page or by directing 
your browser to '/createEntry, or you can go to the quiz page by typing '/quiz/<movie title>' into the browser(insert 
your movie title in side angle brackets). If you answer correctly it congratulates you, if you answer incorrectly, it
informs you that you were wrong and provides the correct answer.
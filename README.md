## Flask Application Design for Marathi Learning Website

## HTML Files

- **index.html**: Home page of the website, providing an introduction to the Marathi language and the learning journey ahead.
- **lessons.html**: Lists all available Marathi lessons, with links to each lesson.
- **lesson1.html**: First lesson on Marathi basics, including alphabet, pronunciation, and grammar fundamentals. (Consider creating similar HTML files for subsequent lessons.)
- **exercises.html**: Collection of interactive exercises to practice Marathi skills learned in the lessons.

## Routes

- **@app.route('/')**: Home page (index.html)
- **@app.route('/lessons')**: Lessons page (lessons.html)
- **@app.route('/lesson1')**: First lesson (lesson1.html)
- **@app.route('/exercises')**: Exercises page (exercises.html)

## Additional Features (Optional)

- **Database integration**: Use a database to store user progress, lesson content, and exercise answers.
- **Authentication**: Allow users to create accounts and track their learning journey.
- **Lesson completion tracking**: Provide visual representation of lesson progress and completion.
- **Gamification**: Introduce interactive elements and rewards to enhance the learning experience.
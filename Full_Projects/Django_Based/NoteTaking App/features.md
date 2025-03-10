📌 Features for the Notes App (MVP - Minimum Viable Product)

pseudo code
1. make a html page for new_note that creates a page for that option
2. make a list html page that shows all objects in that users note dictionary
3. We want a model of notes that is a foreign key to a user which is a one to many connection one user can produce many notes
4. we need a html that we use to update/ edit an existing page that allows you to a view a note and make put request that changes already had data although i hear another post request is probably more secure
5.  We need a delete html page that confirms a files deletion and deletes it if confirmed
6. for the user thing we need a login html page that allows you to create or log in to a user
7.  we want to create a different attribute called tag that you can add a list of entries into that can be update in the update page
8. need a search function created that would search your notes with a loop and return pages with either said word or tag
9. save or load pages in either json to md or just to md and find a way to render theminto html
10. need more help on the django pages i know urls is how the pages connect to each other.  I don't remember views or model i do know template is the front end like the html pages and static for css or java script.


✅ Create a new note (title, content, optional tags).
✅ Read a list of all notes.
✅ Update an existing note (edit title/content).
✅ Delete a note.

📌 Optional Features (If You Want to Expand Later)

🚀 User Authentication (so users only see their own notes).
🚀 Tagging System (categorize notes by tags like “Work” or “Ideas”).
🚀 Search Functionality (find notes by title or content).
🚀 Markdown Support (write notes in markdown and render them as HTML).

📌 Django Components You’ll Use
	•	Model: Stores notes in the database.
	•	Form: Handles note creation and editing.
	•	View: Manages how notes are displayed.
	•	Template: Defines the frontend layout.
	•	URLs: Routes requests to the correct view.
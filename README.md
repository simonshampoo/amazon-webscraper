# amazon-webscraper
A simple webscraper that sends an email when the tracked product's price drops to a certain amount set by user. 

In order to use this project, edit ```URL``` to be the product you want to track, then change ```headers``` to be your current browser's user agent. 

To use a safer way of logging into gmail to send an email to yourself/others, you will need to configure App Passwords for Google, specifically Mail. Line 32 will be the email you want to log in from, and the second parameter will be the app password you have configured. 

Edit the subject, body, and message to your liking. 

Line 38 will take in the email you have logged in from, and the second parameter will be the email you want the message sent to. 

This is an active project, and goals are to remove the liability of configuring it yourself by utilizing a GUI where you can input the product, email, and automatically configure an app password using the Requests library.

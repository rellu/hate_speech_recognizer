# Hate speech recognizer

This is a demo app I used to explore how to use IBM watson services. This was quickly hacked together in couple of hours in hackathon so the code quality is not top notch here.

# Setup

- install python2
- install python requirements in backend directory: `pip install -r requirements.txt`
- register to IBM bluemix and activate Watson service called "Tone Analyzer" 
- configure your "Tone Analyzer" API credentials in `server.py`
- start backend
    - in backend directory run `python server.py`
- install plugin as chromer plugin.
    - Open chrome and go to chrome://extensions/
    - Load unpacked expansion from plugin directory
    - Restart chrome and don't disable the plugin

# Usage

Go to a web page and click "hate speech recognizer" plugin icon on right side of the address bar and click "check this page now button". Wait for a while and observe a notification that indicates whether the page contains hate speech.

Note: the plugin will send the content of the page to 3rd Party. ie. IBM Watson.
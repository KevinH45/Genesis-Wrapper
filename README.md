# Python Desktop Wrapper for Genesis Gradebook

Genesis's website is difficult to use, and just a general eyesore. This is a desktop app that uses Selenium and BS4 in
an effort to fix this issue. This is HEAVILY inspired off of [Zenesus](https://github.com/Zenesus), a Flutter app that does more or less the same thing
(with tons more features). This is meant to be a more lightweight version of Zenesus, that runs on the desktop.

Currently, this app only supports Genesis gradebook. If you are looking for more, use Zenesus.
### Note: This code was rushed and only meant for my personal use (not any form of production).

# Credit and Dependencies
- HUGE Credit to [Zenesus](https://github.com/Zenesus) and [ed.xyz](https://github.com/EDED2314) for the scraping code/general inspiration
- Selenium WebDriver and BS4 for getting the data.
- https://github.com/rdbende/Azure-ttk-theme
- Full list of dependencies found in requirements.txt

# Setup

This was made for fun and learning, so please excuse the tedious setup.

1. Download Python3
2. Download Edge
3. Clone the repo: ```git clone https://github.com/KevinH45/Genesis-Wrapper.git```
4. Install requirements: ```pip install requirements.txt -r```
5. Run app.py: ```python3 app.py```
6. Send a GET request: ```curl -i -x GET localhost:5000/grades?username="USERNAME"&password="PASSWORD"```



# Dev Notes
- Flask API Done, though it might be scrapped
- Need to actually work on the frontend

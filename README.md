``` Deprecated due to website changes ```

# MD Vaccine Finder

Use the power of Python and Selenium to scrape the nearest MD vaccine appointments from the [MassVax MD](https://massvax.maryland.gov/) official site.

For use by eligble groups **ONLY**.

## How to Use

- download Selenium requirement `ChromeDriver` [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- install Python reqs with `requirements.txt`
- adjust `ADDRESS` and `AGE_RANGE` variables as desired

## If an appointment is...

### found

- the screen will display all avaible appointment, make your selection as needed
- the program terminates scraping, waits `100000` seconds, and then closes
- an alert sound will play followed by an extended tone *only on Windows*

### not found

- the portion of the browser will turn red, signifying no vaccines are available near you
- the program will continue to run until a vaccine is found

# HamiltonHub

This is code from the 2018 Hack the Hammer hackathon in Hamilton, ON on December 8th and 9th.
The hackathon participants were given access to the City of Hamilton Open Data dataset collection and tasked with developing applications that use Hamilton's open source data to tackle issues stemming from urban development.

Our Hamilton Hub team decided to develop an application that helps people with isolation and other mental health struggles to very easily find a variety of points of interest within short walking distance of their location and to make leaving the house and getting some simple exercise and fresh air as simple as possible. The app is also quite useful for newcomers to the city, tourists, and even longterm residents to find something interesting to see and do (predominantly for free) in their immediate vicinity.

The app, entitled <em>Step Outside</em>, took in a geolocation from the user and served up all of the points of interest within 0.01 deg of lat/long (~1km in Hamilton) in 15+ open source datasets, as well as scraping the day's events from the City of Hamilton events page, on a Google Fusion map. The datasets included many points of interest not available on Google Maps, such as public works of art, local events, and heritage properties.

Our code standardises the heterogeneous format of these datasets, extracts lat/long co-ordinates or geolocates street addresses, extracts basic site/event information, and generates a CSV for import to the (sadly, very shortly thereafter defunct) Google Fusion Tables API. The code identifies all entries located within 0.01 degrees of the user's supplied location and was intended to serve up all of the points of interest within that radius.

Feel free to read our code but it doesn't run off of a singular file :)

UH18.py runs first
read_write_open_data.py runs second
Step Outside folder contains our interface and runs last

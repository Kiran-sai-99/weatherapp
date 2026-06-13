# Weather Application

A modern and responsive Weather Application built using **Django**, **Python**, **HTML**, **CSS**, and the **OpenWeatherMap API**. This application allows users to search for any city and get real-time weather information including temperature, humidity, wind speed, pressure, visibility, cloud coverage, and weather conditions. The project demonstrates API integration, JSON data processing, Django template rendering, and responsive UI design.

---

## Features

- Search weather by city name
- Real-time weather updates using OpenWeatherMap API
- Default city set to **Bangalore** on application startup
- Displays current temperature in Celsius
- Shows minimum and maximum temperatures
- Weather description with dynamic weather icons
- Humidity percentage
- Wind speed and wind direction
- Cloud coverage information
- Atmospheric pressure details
- Visibility measurement
- Error handling for invalid city names
- Modern Glassmorphism user interface
- Responsive design for different screen sizes

---

## Technologies Used

- Python
- Django
- HTML5
- CSS3
- OpenWeatherMap API

---

## Project Structure

```text
weatherapp/
│
├── weather/
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   └── partials/
│   │       └── navbar.html
│   │
│   └── static/
│       └── css/
│           └── style.css
│
├── screenshots/
│   ├── default-weather.png
│   ├── weather-result.png
│   └── city-not-found.png
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## Screenshots

### Default Weather (Bangalore)

When the application loads for the first time, it automatically displays the weather information for Bangalore.

![Default Weather](screenshots/default-weather.png)

---

### Valid City Search

Weather information displayed successfully when a valid city name is entered.

![Weather Result](screenshots/weather-result.png)

---

### Invalid City Search

Displays an error message when the entered city is not found.

![City Not Found](screenshots/city-not-found.png)

---

## Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/Kiran-sai-99/weatherapp.git
cd weatherapp
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install django requests
```

### Configure API Key

Get your free API key from:

https://openweathermap.org/api

Replace the API key in `views.py`:

```python
API_KEY = "YOUR_API_KEY"
```

### Run the Project

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

## 🔄 Application Workflow

1. User enters a city name.
2. Django receives the request.
3. The backend sends a request to the OpenWeatherMap API.
4. The API returns weather data in JSON format.
5. Django processes the response.
6. Weather information is passed to the template.
7. Dynamic weather details are displayed on the webpage.

---

## 🎨 User Interface Highlights

- Modern Glassmorphism Design
- Attractive Background Image
- Dynamic Weather Icons
- Smooth Hover Effects
- Responsive Layout
- User-Friendly Dashboard
- Clean and Minimal Design

---

## Error Handling

The application handles:

- Invalid city names
- Empty search inputs
- API request failures
- Unexpected runtime errors

Appropriate error messages are displayed to improve user experience.

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Django Web Development
- REST API Integration
- JSON Data Processing
- HTTP Requests and Responses
- Django Template Rendering
- Error Handling
- Responsive Web Design
- Real-Time Data Processing

---

## Project Summary

This Weather Application is a beginner-friendly full-stack web development project that demonstrates how to integrate external APIs with Django to provide real-time weather information through a modern and responsive user interface. It showcases backend development, API integration, dynamic content rendering, error handling, and responsive frontend design.

# 🌦️ Weather Application

A modern and responsive Weather Application built using **Django**, **Python**, **HTML**, **CSS**, and the **OpenWeatherMap API**. This application allows users to search for any city and get real-time weather information including temperature, humidity, wind speed, pressure, visibility, cloud coverage, and weather conditions. The project demonstrates API integration, JSON data processing, Django template rendering, and responsive UI design.

---

## 🚀 Features

- Search weather by city name
- Real-time weather updates using OpenWeatherMap API
- Displays current temperature in Celsius
- Shows minimum and maximum temperatures
- Humidity percentage
- Wind speed and wind direction
- Cloud coverage information
- Atmospheric pressure details
- Visibility measurement
- Dynamic weather icons
- Error handling for invalid city names
- Modern Glassmorphism user interface
- Responsive design for different screen sizes

---

## 🛠️ Technologies Used

- Python
- Django
- HTML5
- CSS3
- OpenWeatherMap API
- Requests Library

---

## 📂 Project Structure

```text
weather_app/
│
├── weather/
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   └── partials/
│   │       └── navbar.html
│
├── static/
│   └── css/
│       └── style.css
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

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

### Run the Application

```bash
python manage.py runserver
```

Visit:

```text
http://127.0.0.1:8000/
```

---

## 🔄 Application Workflow

1. User enters a city name.
2. Django receives the request from the frontend.
3. The backend sends an API request to OpenWeatherMap.
4. Weather data is returned in JSON format.
5. Django processes the response.
6. Weather information is passed to the template.
7. Dynamic weather details are displayed on the webpage.

---

## 📊 Weather Information Displayed

- Current Temperature
- Minimum Temperature
- Maximum Temperature
- Weather Description
- Humidity
- Wind Speed
- Wind Direction
- Cloud Coverage
- Atmospheric Pressure
- Visibility

---

## 🎨 User Interface Highlights

- Modern Glassmorphism Design
- Fully Responsive Layout
- Dynamic Weather Icons
- Attractive Background Design
- Smooth Hover Effects
- User-Friendly Dashboard

---

## ❌ Error Handling

The application handles:

- Invalid city names
- Empty search inputs
- API request failures
- Unexpected runtime errors

User-friendly error messages are displayed to improve the overall experience.

---

## 📈 Future Enhancements

- 5-Day Weather Forecast
- Hourly Weather Forecast
- Current Location Detection
- Air Quality Index (AQI)
- Weather Maps Integration
- Dark/Light Theme Toggle
- Multi-language Support

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Django Web Development
- REST API Integration
- JSON Data Handling
- HTTP Requests and Responses
- Django Template Rendering
- Error Handling
- Responsive Web Design
- Real-Time Data Processing

---

## 👨‍💻 Author

**Kiran Sai**

Python Developer | Django Enthusiast

---

## ⭐ Project Summary

This Weather Application is a beginner-friendly full-stack web development project that demonstrates how to integrate external APIs with Django to provide real-time weather information through a modern, responsive, and user-friendly interface.

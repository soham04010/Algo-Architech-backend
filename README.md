📝 Backend README: Commodity Price API (Django)
This document explains the setup and functionality of the Django REST Framework (DRF) backend for the Algo Architech internship assignment.

📁Project Overview
The primary role of this backend is to act as a reliable data intermediary. It handles the integration with the external Alpha Vantage API and processes that raw data into a clean JSON format. This separation ensures the frontend dashboard only interacts with a local, dedicated API, making the application more robust and easier to maintain.

🗓️Technical Choices
I chose Django for its stability and comprehensive features, paired with Django REST Framework for quick API creation. The application is structured around a single app, algo_app.

📂Key Implementation Details
1)API Endpoint: The processed commodity data is served via a single, unauthenticated GET request at the path: /api/commodities/.

2)Data Handling: The code in algo_app/views.py uses the standard requests library to fetch the Alpha Vantage data. I implemented logic to handle and clean missing values (the . entries), converting all valid prices into numerical format (float) required for the charting library.

3)Cross-Origin (CORS) Setup: The django-cors-headers package was configured to allow the separate Next.js frontend application (running on a different port) to access this API without security blocking.

🎯How to Run
1)Clone the repository and set up a Python virtual environment.

2)Install dependencies using pip install.

3)Start the server with python manage.py runserver.

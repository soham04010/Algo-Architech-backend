import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# The external API URL provided in the assignment
API_URL = "https://www.alphavantage.co/query?function=ALL_COMMODITIES&interval=monthly&apikey=demo"

@api_view(['GET'])
def get_commodities_data(request):
    """
    Fetches raw data from the Alpha Vantage API, processes it, and serves it as JSON.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status() 
        raw_data = response.json()

        if 'Error Message' in raw_data:
             return Response({'error': raw_data['Error Message']}, 
                             status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        processed_data = []
        commodity_series = raw_data.get('data', [])

        for entry in commodity_series:
            value = entry.get('value')

            if value == '.':
                value_float = 0.0
            else:
                try:
                    value_float = float(value)
                except ValueError:
                    value_float = 0.0
            
            processed_data.append({
                'date': entry.get('date'),
                'price': value_float
            })

        return Response(processed_data[::-1]) 

    except requests.exceptions.RequestException as e:
        return Response({'error': f"Failed to fetch external data: {e}"}, 
                        status=status.HTTP_503_SERVICE_UNAVAILABLE)
    except Exception as e:
        return Response({'error': f"An unexpected server error occurred: {e}"}, 
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
from django.shortcuts import render
import requests

def currency_converter(request):
    conversion_result = None
    error_message = None

    if request.method == 'POST':
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')
        amount = request.POST.get('amount')

        url = f'https://v6.exchangerate-api.com/v6/1bdf0aedbc627d395a05ec40/pair/{from_currency}/{to_currency}/{amount}'

        try:
            response = requests.get(url)
            response.raise_for_status()  # Check if the request was successful

            # Assuming the response is in JSON format
            data = response.json()

            if isinstance(data, dict):
                # Extract the conversion_result
                conversion_result = data.get("conversion_result", None)

                if conversion_result is not None:
                    return render(request, 'converter_form.html', {'conversion_result': conversion_result})
            else:
                error_message = 'Invalid or incomplete API response'

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            error_message = 'Failed to fetch currency data'

    return render(request, 'converter_form.html', {'error_message': error_message})

"""
This module contains the views for handling USSD requests, user interaction, and integration with 
Africa's Talking API for SMS and payment processing.
"""


# Standard library imports
import requests

# Third-party imports
import africastalking
from rest_framework import generics
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# Local application imports
from .models import Contact
from .serializers import ContactSerializer


africastalking.initialize(settings.USSD_USERNAME, settings.USSD_API_KEY)
USSD = africastalking.USSD

# Static menu data
menu_data = {
    "boxes": [
        {"id": 1, "name": "Box 1", "price": "KES 8000"},
        {"id": 2, "name": "Box 2", "price": "KES 10000"},
        {"id": 3, "name": "Box 3", "price": "KES 200"},
        {"id": 4, "name": "Box 4", "price": "KES 0"},
        {"id": 5, "name": "Box 5", "price": "KES 13000"}
    ],
    "payment": {
        "min": 20,
        "max": 1000
    }
}

# Helper function to process payments
def process_payment(amount, menu_id):
    """
    Simulate sending a payment request to a backend payment API.
    """
    payment_api_url = "https://your-backend.com/mpesa-payment"
    response = requests.post(
        payment_api_url, data={"amount": amount, "menu_id": menu_id},
        timeout=30
    )
    return response.json()


# Generate the USSD menu dynamically
def generate_ussd_menu():
    """
    Generates the main USSD menu text.
    """
    menu_text = "Welcome to the USSD service. Please choose an option:\n"
    for box in menu_data['boxes']:
        menu_text += f"{box['id']}. {box['name']} - {box['price']}\n"
    menu_text += "6. Withdraw\n"
    return menu_text


def handle_first_time_user():
    """
    Handles the USSD interaction for a first-time user.

    Returns:
        HttpResponse: A response with the initial USSD menu.
    """
    return HttpResponse(f"CON {generate_ussd_menu()}")



def handle_level_one_choice(choice):
    """
    Handles the USSD interaction for a first-time user.

    Returns:
        HttpResponse: A response with the initial USSD menu.
    """
    if choice in ['1', '2', '3', '4', '5']:
        selected_box = menu_data['boxes'][int(choice) - 1]
        return HttpResponse(
            f"CON You selected {selected_box['name']} for {selected_box['price']}."\
            "\nPlease enter the amount (min KES 20):"
        )
    elif choice == '6':  # Withdraw option
        return HttpResponse("CON Please enter the amount to withdraw (min KES 20):")
    else:
        return HttpResponse(
            "CON Invalid choice, please select a valid option.\n"\
            + generate_ussd_menu()
        )

def handle_level_two_input(choice, amount):
    """
    Handles the USSD interaction for a first-time user.

    Returns:
        HttpResponse: A response with the initial USSD menu.
    """
    if not amount.isdigit() or int(amount) < 20:
        return HttpResponse(
            "CON Invalid amount. Amount must be at least KES 20. Please try again:"
        )
    if choice in ['1', '2', '3', '4', '5']:
        selected_box = menu_data['boxes'][int(choice) - 1]
        return HttpResponse(f"END Processing your payment of KES {amount}. Please wait...")
    elif choice == '6':
        return HttpResponse(f"END Processing your withdrawal of KES {amount}. Please wait...")
    else:
        return HttpResponse("END An error occurred. Please try again.")


@csrf_exempt
def ussd_menu(request):
    """
    Handles the USSD interaction for a first-time user.

    Returns:
        HttpResponse: A response with the initial USSD menu.
    """
    if request.method == "POST":
        try:
            data = request.POST
            text = data.get("text", "")
            input_parts = text.split('*')

            if not text:
                return handle_first_time_user()

            if len(input_parts) == 1:
                return handle_level_one_choice(input_parts[0])

            if len(input_parts) == 2:
                return handle_level_two_input(input_parts[0], input_parts[1])

            return HttpResponse("END An error occurred. Please try again.")

        except (KeyError, ValueError, TypeError) as e:
            print(f"Specific error: {e}")
            return HttpResponse("END An error occurred while processing your request.")

        except Exception as e:
            print(f"Unexpected error: {e}")
            return HttpResponse("END An unexpected error occurred.")
    else:
        return HttpResponse("END Invalid request method.")


# Contact creation view
class ContactCreateView(generics.CreateAPIView):
    """
    API view for creating contact entries.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

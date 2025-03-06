import requests
import logging
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import openai
# Initialize OpenAI API
openai.api_key = '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'  # Replace with your actual OpenAI API key

# Function to fetch ticket information and format the response
def get_ticket_info(event: Text, location: Text) -> Text:
    try:
        # Fetch ticket data from Ticketmaster
        ticket_data = fetch_ticket_data(event, location)

        if 'Ticketmaster' in ticket_data:
            tm_events = ticket_data['Ticketmaster'].get('_embedded', {}).get('events', [])
            if tm_events:
                response = "Website Name: Ticketmaster\n"
                for event in tm_events:
                    name = event['name']
                    date = event['dates']['start']['localDate']
                    venue = event['_embedded']['venues'][0]['name']
                    price_range = event['priceRanges'][0]['min'] if 'priceRanges' in event else "N/A"
                    price_range_max = event['priceRanges'][0]['max'] if 'priceRanges' in event else "N/A"
                    event_url = event['url']

                    response += f"Event: {name}\n"
                    response += f"Date: {date}\n"
                    response += f"Venue: {venue}\n"
                    response += f"Ticket Price Range: {price_range} - {price_range_max} USD\n"
                    response += f"URL: {event_url}\n\n"
                return response
            else:
                return "No events found on Ticketmaster for your query."
        else:
            return "Could not fetch data from Ticketmaster."

    except Exception as e:
        logging.error(f"Error in get_ticket_info: {e}")
        return "Sorry, something went wrong while fetching ticket information."

# Helper function to fetch ticket data from Ticketmaster
def fetch_ticket_data_from_ticketmaster(event, location):
    url = "https://app.ticketmaster.com/discovery/v2/events.json"
    params = {
        'apikey': 'GFaDqGrEbXuVFMpqKPjjH9ujR43iVeJv',  # Your API Key
        'keyword': event,
        'city': location
    }
    response = requests.get(url, params=params)
    logging.info(f"Ticketmaster API Response: {response.status_code} - {response.text}")
    if response.status_code == 200:
        return response.json()
    else:
        logging.error(f"Error fetching data from Ticketmaster: {response.status_code} {response.text}")
        return None

def fetch_ticket_data(event, location):
    ticket_data = {}

    # Fetch data from Ticketmaster
    ticketmaster_data = fetch_ticket_data_from_ticketmaster(event, location)
    if ticketmaster_data:
        ticket_data['Ticketmaster'] = ticketmaster_data

    return ticket_data

# Custom action to retrieve ticket information
class ActionGetTicketInfo(Action):

    def name(self) -> Text:
        return "action_get_ticket_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        event = tracker.get_slot("event")
        location = tracker.get_slot("location")

        logging.info(f"Slot values - Event: {event}, Location: {location}")

        if not event or not location:
            if not event:
                dispatcher.utter_message(text="Which event are you looking for tickets to?")
            if not location:
                dispatcher.utter_message(text="Where is the event located?")
            return []

        # Get ticket information
        ticket_info = get_ticket_info(event, location)
        
        # Send the response to the user
        dispatcher.utter_message(text=ticket_info)
        return []



# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

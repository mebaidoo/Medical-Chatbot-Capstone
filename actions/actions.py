# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from terms import Terms


class TermsAndDefinitions(Action):

    def name(self) -> Text:
        return "action_term_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        term = next(tracker.get_latest_entity_values("term_name"), None)
        term = term[1:] #Taking out the @ character
        try:
            definition = str(Terms(term))
            dispatcher.utter_message(response="utter_definition", term=term, definition=definition)
        except:
            dispatcher.utter_message(response="utter_correct_term")

        return []


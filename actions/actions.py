# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from aiormq import DuplicateConsumerTag

from rasa_sdk import Action, Tracker, ValidationAction, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from terms import Terms
from locations import hospitals, pharmacies, labs

#Action for returning the medical terms definitions
from diseases import disease_repo


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
            dispatcher.utter_message(response="utter_anything_next")
        except:
            dispatcher.utter_message(response="utter_no_term")
            dispatcher.utter_message(response="utter_anything_next")

        return []
        
########################################################################################
#  DISEASES CLASS                                                                      #
########################################################################################
class DiseasesAndSymptoms(Action):

    def name(self) -> Text:
        return "action_disease_checker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        bad_chars = ["[","'","]","'"]
        disease_name = next(tracker.get_latest_entity_values("disease"), None)
        data = disease_repo()
        data_two= disease_repo()
        
        if data['name'].str.contains(disease_name).any():
            data= data[data.name == disease_name]
            data = data.to_dict()
            data = list(data.values())[1]
            data = list(data.values())[0]

            data_two = data_two.loc[data_two["name"]==disease_name]
            data_two= data_two.to_dict()
            data_two = list(data_two.values())[2]
            data_two = list(data_two.values())[0]
            for i in bad_chars:
                data = data.replace(i,"")
                data_two = data_two.replace(i,"")
            dispatcher.utter_message(response="utter_disease", data=data, data_two=data_two, disease_name=disease_name)
            dispatcher.utter_message(response="utter_anything_next")
        else:
            dispatcher.utter_message(response="utter_no_disease", disease_name=disease_name)
        return []


#Action for returning a list of hospitals/pharmacies/labs
class ListOfPlaces(Action):
    
    def name(self) -> Text:
        return "action_places_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        place_type = tracker.get_intent_of_latest_message()
        if place_type == 'locate_hosp':
            hospitals_list = []
            for pair in zip(hospitals["name"], hospitals["area"]):
                pair_str = "({})".format(",".join(pair))
                hospitals_list.append(pair_str)
            hospitals_list = '\n'.join(hospital.strip('()') for hospital in hospitals_list)

            dispatcher.utter_message(response="utter_hospitals", hospitals = hospitals_list)
        
        elif place_type == 'locate_pharm':
            pharm_list = []
            for pair in zip(pharmacies["name"], pharmacies["area"]):
                pair_str = "({})".format(",".join(pair))
                pharm_list.append(pair_str)
            pharm_list = '\n'.join(pharm.strip('()') for pharm in pharm_list)

            dispatcher.utter_message(response="utter_pharmacies", pharmacies = pharm_list)

        elif place_type == 'locate_lab':
            lab_list = []
            for pair in zip(labs["name"], labs["area"]):
                pair_str = "({})".format(",".join(pair))
                lab_list.append(pair_str)
            lab_list = '\n'.join(lab.strip('()') for lab in lab_list)

            dispatcher.utter_message(response="utter_labs", labs = lab_list)

        return []

#Action for returning links to google map locations
class MapLocations(Action):
    
    def name(self) -> Text:
        return "action_map_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        place_type = tracker.get_intent_of_latest_message()

        if place_type == "hospital_name":
            place = next(tracker.get_latest_entity_values("hosp_name"), None)
            place = place.title() #ensuring name matches format in dataframe
            map = hospitals.map_location[hospitals['name'] == place].to_list()
            dispatcher.utter_message(response="utter_map_location", place_name = place, map_link = map[0])
            dispatcher.utter_message(response="utter_anything_next")

        elif place_type == "pharmacy_name":
            place = next(tracker.get_latest_entity_values("pharm_name"), None)
            place = place.title()
            map = pharmacies.map_location[pharmacies['name'] == place].to_list()
            dispatcher.utter_message(response="utter_map_location", place_name = place, map_link = map[0])
            dispatcher.utter_message(response="utter_anything_next")

        elif place_type == "laboratory_name":
            place = next(tracker.get_latest_entity_values("lab_name"), None)
            place = place.title()
            map = labs.map_location[labs['name'] == place].to_list()
            dispatcher.utter_message(response="utter_map_location", place_name = place, map_link = map[0])
            dispatcher.utter_message(response="utter_anything_next")

        return []

# Fallback action
# class MyFallback(Action):
    
#     def name(self) -> Text:
#         return "action_my_fallback"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         dispatcher.utter_message(template="utter_fallback")

#         return []


# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, utils
from rasa_sdk.executor import CollectingDispatcher
from terms import Terms
from locations import hospitals, pharmacies, labs
import string
from bs4 import BeautifulSoup
import re
import requests

#Action for dispatching definitions to medical terms using Merriam-Webster medical dictionary API
class TermsAndDefinitions(Action):

    def name(self) -> Text:
        return "action_term_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        term = next(tracker.get_latest_entity_values("term_name"), None)
        term = term[1:] #Taking out the @ character
        term = term.lower()
        try:
            #Using the Terms function from terms.py
            definition = str(Terms(term))
            dispatcher.utter_message(response="utter_definition", term=term, definition=definition)
            dispatcher.utter_message(text = "\n")
            dispatcher.utter_message(response="utter_anything_next")
        except:
            dispatcher.utter_message(response="utter_no_term")
            dispatcher.utter_message(text = "\n")
            dispatcher.utter_message(response="utter_anything_next")

        return []

#Action for dispatching disease information
class DiseasesAndSymptoms(Action):
    
    def name(self) -> Text:
        return "action_disease_checker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        disease_name = next(tracker.get_latest_entity_values("disease"), None)
        disease_name = disease_name[1:] #Taking off the underscore
        disease_name = disease_name.lower()
        u_i = string.capwords(disease_name)
        lists = u_i.split()
        word = "_".join(lists)
        url = "https://en.wikipedia.org/wiki/" + word
        url_open = requests.get(url)
        soup = BeautifulSoup(url_open.content, 'html.parser')
        virus_info = soup('table', {'class':'biota'}) #information on viruses like coronavirus which is not a disease and will be omitted
        details = soup('table', {'class':'infobox'})

        if details and not virus_info:
            dispatcher.utter_message(response="utter_pre_disease", disease=disease_name)
            dispatcher.utter_message(text = "\n")
            for i in details:
                h = i.find_all('tr')
                for j in h:
                    heading = j.find_all('th')
                    detail = j.find_all('td')
                    if heading is not None and detail is not None:
                        for x, y in zip(heading, detail):
                            #Cleaning the data
                            title = re.sub(r"\[[0-9]*\]", "", x.text)
                            sub = re.sub(r"\[[0-9]*\]", "", y.text)
                            if title not in ["Pronunciation", "Frequency", "Deaths"]:
                                dispatcher.utter_message(response="utter_disease", title=title, data=sub)
            dispatcher.utter_message(text = "\n")
            dispatcher.utter_message(response="utter_adverse")
            
        else:
            dispatcher.utter_message(response="utter_no_disease")
            dispatcher.utter_message(text = "\n")
            dispatcher.utter_message(response="utter_adverse")

        return []

#Action for dispatching adverse drug reaction information for a specific drug
class AdverseDrugReactions(Action):
    
    def name(self) -> Text:
        return "action_adverse_drug"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        drug_name = next(tracker.get_latest_entity_values("name_of_drug"), None)
        drug_name = drug_name[1:] #Taking off &
        drug_name = drug_name.lower()
        u_i_drug = string.capwords(drug_name)
        lists_drug = u_i_drug.split()
        word_drug = "_".join(lists_drug)
        drug_url = "https://en.wikipedia.org/wiki/" + word_drug
        drug_url_open = requests.get(drug_url)
        drug_soup = BeautifulSoup(drug_url_open.content, 'html.parser')

        try:
            #Getting the information from the adverse effects section of the page
            span = drug_soup.select("span#Adverse_effects.mw-headline")[0]
            all_p_after = span.find_all_next("p")
            info = all_p_after[0].text
            #Cleaning the data
            info = re.sub(r"\[[0-9]*\]", "", info)
            dispatcher.utter_message(response="utter_adverse_info", drug=drug_name, data=info)
            if len(info.split()) < 50:
                if all_p_after[1]:
                    info_2 = all_p_after[1].text
                    info_2 = re.sub(r"\[[0-9]*\]", "", info_2)
                    dispatcher.utter_message(text = "\n")
                    dispatcher.utter_message(response="utter_adverse_info", drug=drug_name, data=info_2)
            dispatcher.utter_message(text = "\n")
            dispatcher.utter_message(response="utter_anything_next")
        except:
            try:
                #Getting the information from the side effects section of the page if there is no adverse effects
                span = drug_soup.select("span#Side_effects.mw-headline")[0]
                all_p_after = span.find_all_next("p")
                info = all_p_after[0].text
                info = re.sub(r"\[[0-9]*\]", "", info)
                dispatcher.utter_message(response="utter_adverse_info", drug=drug_name, data=info)
                if len(info.split()) < 50:
                    if all_p_after[1]:
                        info_2 = all_p_after[1].text
                        info_2 = re.sub(r"\[[0-9]*\]", "", info_2)
                        dispatcher.utter_message(text = "\n")
                        dispatcher.utter_message(response="utter_adverse_info", drug=drug_name, data=info_2)
                dispatcher.utter_message(text = "\n")
                dispatcher.utter_message(response="utter_anything_next")
            except:
                dispatcher.utter_message(response="utter_no_drug")
                dispatcher.utter_message(text = "\n")
                dispatcher.utter_message(response="utter_anything_next")

        return []

#Action for returning a list of hospitals/pharmacies/labs
# class ListOfPlaces(Action):
    
#     def name(self) -> Text:
#         return "action_places_list"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         place_type = tracker.get_intent_of_latest_message()
#         if place_type == 'locate_hosp':
#             hospitals_list = []
#             for pair in zip(hospitals["name"], hospitals["area"]):
#                 pair_str = "({})".format(",".join(pair))
#                 hospitals_list.append(pair_str)
#             hospitals_list = '\n'.join(hospital.strip('()') for hospital in hospitals_list)

#             dispatcher.utter_message(response="utter_hospitals", hospitals = hospitals_list)
        
#         elif place_type == 'locate_pharm':
#             pharm_list = []
#             for pair in zip(pharmacies["name"], pharmacies["area"]):
#                 pair_str = "({})".format(",".join(pair))
#                 pharm_list.append(pair_str)
#             pharm_list = '\n'.join(pharm.strip('()') for pharm in pharm_list)

#             dispatcher.utter_message(response="utter_pharmacies", pharmacies = pharm_list)

#         elif place_type == 'locate_lab':
#             lab_list = []
#             for pair in zip(labs["name"], labs["area"]):
#                 pair_str = "({})".format(",".join(pair))
#                 lab_list.append(pair_str)
#             lab_list = '\n'.join(lab.strip('()') for lab in lab_list)

#             dispatcher.utter_message(response="utter_labs", labs = lab_list)

#         return []

# #Action for returning links to google map locations
# class MapLocations(Action):
    
#     def name(self) -> Text:
#         return "action_map_location"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         place_type = tracker.get_intent_of_latest_message()

#         if place_type == "hospital_name":
#             place = next(tracker.get_latest_entity_values("hosp_name"), None)
#             place = place.title() #ensuring name matches format in dataframe
#             map = hospitals.map_location[hospitals['name'] == place].to_list()
#             dispatcher.utter_message(response="utter_map_location", place_name = place, map_link = map[0])
#             dispatcher.utter_message(text = "\n")
#             dispatcher.utter_message(response="utter_anything_next")

#         elif place_type == "pharmacy_name":
#             place = next(tracker.get_latest_entity_values("pharm_name"), None)
#             place = place.title()
#             map = pharmacies.map_location[pharmacies['name'] == place].to_list()
#             dispatcher.utter_message(response="utter_map_location", place_name = place, map_link = map[0])
#             dispatcher.utter_message(text = "\n")
#             dispatcher.utter_message(response="utter_anything_next")

    

#         elif place_type == "laboratory_name":
#             place = next(tracker.get_latest_entity_values("lab_name"), None)
#             place = place.title()
#             map = labs.map_location[labs['name'] == place].to_list()
#             dispatcher.utter_message(response="utter_map_location", place_name = place, map_link = map[0])
#             dispatcher.utter_message(text = "\n")
#             dispatcher.utter_message(response="utter_anything_next")

#         return []

#Default knowledge-based action for dispatching location information
class MyKnowledgeBaseAction(ActionQueryKnowledgeBase):
    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("data.json")
        super().__init__(knowledge_base)

    #Overwriting the default responses
    async def utter_objects(
        self,
        dispatcher,
        object_type,
        objects,
    ):
        if objects:
            dispatcher.utter_message(text=f"Found the following {object_type}:")
            dispatcher.utter_message(text="\n")
            repr_function = await utils.call_potential_coroutine(
                self.knowledge_base.get_representation_function_of_object(object_type)
            )
            for i, obj in enumerate(objects,1):
                dispatcher.utter_message(text=f"{i}: {repr_function(obj)}")
            dispatcher.utter_message(text="\n")
            dispatcher.utter_message(text="Which of them would you like directions for? \nPlease begin your statement with \"directions to\", e.g. directions to the first one.")
        else:
            dispatcher.utter_message(text=f"I didn't find any {object_type}")
            dispatcher.utter_message(text="\n")
            dispatcher.utter_message(response="utter_anything_next")

    def utter_attribute_value(
        self,
        dispatcher,
        object_name,
        attribute_name,
        attribute_value,
    ):
        if attribute_value:
            dispatcher.utter_message(text=f"This is the link to the {attribute_name} of {object_name}: {attribute_value}. Hope you find what you need.")
            dispatcher.utter_message(text="\n")
            dispatcher.utter_message(response="utter_anything_next")
        else:
            dispatcher.utter_message(text=f"I didn't find a {attribute_name} for {object_name}.")
            dispatcher.utter_message(text="\n")
            dispatcher.utter_message(response="utter_anything_next")
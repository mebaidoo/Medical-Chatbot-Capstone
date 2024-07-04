
# Medical-Chatbot-Capstone
This goal of this project is to design a conversational chatbot (using rasa) for a local community which will provide healthcare assistance to users. The bot is able to provide medical information including disease symptoms, diagnostics, available treatments, and adverse drug reaction. Also, directions to medical facilities such as hospitals, pharmacies and labs and simple interpretation to medical terminologies such as bmi, hypertension, benign, malignant, etc.

To make the bot user-friendly, the bot asks about the health of the user before asking what they would like to do. The users then have to choose an option between the type of information they would like to receive: directions to medical facilities, interpretation to medical terms they do not understand, or information about a disease they would like to learn more about.

**Installation:**
A virtual environment was created where rasa and its dependencies were installed successfully.

**Interpretation to medical terminologies:**
The Merriam-Webster's medical dictionary API was used to provide medical terms definitions to users. In a case a user provides a wrong or non-existent medical term, the bot lets the user know there is no such medical term, and gives them the option to quit or return to the main menu.

**Directions to medical facilities:**
For the directions to medical facilities, the bot focused on medical facilities in Sekondi-Takoradi, Ghana. The user makes an option between locating a hospital, pharmacy or lab, then the bot provides them with a list of hospitals, pharmacies or labs, depending on which option they chose. The user then lets the bot know the specific medical facility they would like directions to, and the bot provides them with a Google map link to the location of that medical facility. Rasa's knowledge-based action is applied here.
All other map APIs did not have enough coverage of medical facilities in Sekondi-Takoradi except Google map, whose APIs were priced. Because the chatbot was not meant to be used for production/commercial purposes, the directions were not sourced directly from the API. Instead, Google map links to locations of these medical facilities was used, which will further provide the user with the directions to the medical facility they chose.

**Information about diseases:**
When a user selects this option, they are asked to enter the name of the disease they would like to learn more about, then the bot provides them with some information associated with that disease, including symptoms, diagnostics, treatment and medication.
The python module bs4 which contains BeautifulSoup was used to scrape information about diseases from Wikipedia.
After the disease information is dispatched to the user, they are again given the option to ask for the adverse reaction of any drug probably mentioned in the medication data that came along with the disease information. BeautifulSoup is again used to scrape the adverse reaction/side effects of drugs from Wikipedia.

**Extras:**
After the chatbot provides the user with the information they required, it gives them the option to either return to the main menu where they can go on to ask for other information, or quit.

**Fallback:**
The rasa default fallback intent and action was used, so in cases where a user enters a wrong/non-existent medical facility/disease name, or when they deviate, the bot gives them the option to correct it and the conversation continues.

**Deployment on social media apps:**
The bot was finally deployed on Facebook and Whatsapp to make it accessible to users. Facebook supports the use of buttons and therefore the user only needs to select an option where there are buttons unlike Whatsapp where the user needs to type their message.

## Chatbot deployed on Facebook Messenger
![1](https://github.com/SeyramDiaba/Medical-Chatbot-Capstone/blob/main/pics/Screenshot_20220330_073929_com.facebook.orca.jpg?raw=true)
![1](https://github.com/SeyramDiaba/Medical-Chatbot-Capstone/blob/main/pics/Screenshot_20220330_073945_com.facebook.orca.jpg?raw=true)

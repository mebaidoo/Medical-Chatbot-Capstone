from qwikidata.linked_data_interface import get_entity_dict_from_api
from qwikidata.entity import WikidataItem, WikidataProperty, WikidataLexeme

p557_dict = get_entity_dict_from_api('P557')
p557 = WikidataProperty(p557_dict)



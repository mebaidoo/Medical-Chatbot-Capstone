# from qwikidata.sparql import return_sparql_query_results

# query_string = """
# SELECT ?disease ?diseaseLabel
# WHERE{
#   ?item wdt:P2176 ?disease .
#   SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
# }
# """

# results = return_sparql_query_results(query_string)
# drugs = {}  #contains 1819 different drugs and their wikidata values
# for i in range(len(results['results']['bindings'])):
#     key = results['results']['bindings'][i]['diseaseLabel']['value']
#     value = results['results']['bindings'][i]['disease']['value']
#     value = value.strip('http://www.wikidata.org/entity/')
#     if key not in drugs.keys():
#         drugs[key] = value

# query_string = """
# SELECT ?drug ?drugLabel
# WHERE{
#   ?drug wdt:P769 wd:Q410061 .
#   SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
# }
# """

# results = return_sparql_query_results(query_string)

# for i in range(len(results['results']['bindings'])):
#     print(results['results']['bindings'][i]['drugLabel']['value'])


#for diseases
# SELECT ?item ?itemLabel
# WHERE{
#   ?item wdt:P2176 ?drug .
#   SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
# }


import wikipedia

disease = input("Enter disease: ")

#print(wikipedia.search(disease))

#print(wikipedia.summary(disease))

results = wikipedia.page(disease).content
results_list = results.split("==")
print(results_list)

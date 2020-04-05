# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/

import sys
from SPARQLWrapper import SPARQLWrapper, JSON

endpoint_url = "https://query.wikidata.org/sparql"

# SPARQL fetching all objects of type Q18333556 "Sveriges distrikt "
query = """SELECT ?BygdebandID ?WD ?distrikt ?kommunWDID ?kommun ?distriktkod  WHERE {
    ?WD wdt:P31 wd:Q18333556.
    ?WD wdt:P625 ?coord.
    OPTIONAL {?WD wdt:P6192 ?BygdebandID}
    OPTIONAL {?WD wdt:P1841 ?distriktkod}
    OPTIONAL {?WD wdt:P131 ?kommunWDID}
    BIND(
      IF(BOUND(?BygdebandID), "BygdebandID","-")
    AS ?layer).
    BIND (URI(CONCAT("https://www.hembygd.se/shf/plats/" ,?BygdebandID)) AS ?Bygdeband)
SERVICE wikibase:label { bd:serviceParam wikibase:language "sv,en".
      ?kommunWDID rdfs:label ?kommun.
      ?WD rdfs:label ?distrikt}
} order by xsd:integer(?BygdebandID)"""


def get_results(endpoint_url, query):
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


results = get_results(endpoint_url, query)

for result in results["results"]["bindings"]:
    print(result)

import xml.dom.minidom
import xml.sax
from datetime import datetime


# We need to check these three GO ontologies.
# For each ontology, store the GO term with the largest number of <is_a> elements.
ontologies = [
    "molecular_function",
    "biological_process",
    "cellular_component"
]


def make_results():
    # Create an empty dictionary.
    # Each ontology starts with no GO ID, no name, and zero <is_a> elements.
    results = {}

    for ontology in ontologies:
        results[ontology] = {
            "id": "",
            "name": "",
            "number_of_is_a": 0
        }

    return results


def get_text_from_tag(element, tag_name):
    # Find the first tag with this tag name.
    # Return the text inside this tag.
    tag_list = element.getElementsByTagName(tag_name)

    if tag_list.length > 0:
        if tag_list[0].firstChild is not None:
            return tag_list[0].firstChild.nodeValue.strip()

    return ""


def update_results(results, namespace, go_id, name, number_of_is_a):
    # If this GO term belongs to one of the three ontologies,
    # compare its number of <is_a> elements with the current maximum.
    # If it is larger, replace the stored result.
    if namespace in results:
        if number_of_is_a > results[namespace]["number_of_is_a"]:
            results[namespace]["id"] = go_id.strip()
            results[namespace]["name"] = name.strip()
            results[namespace]["number_of_is_a"] = number_of_is_a


def print_results(api_name, results):
    print("\n" + api_name + " results")

    for ontology in ontologies:
        print("\nOntology:", ontology)
        print("GO ID:", results[ontology]["id"])
        print("Name:", results[ontology]["name"])
        print("Number of <is_a> elements:", results[ontology]["number_of_is_a"])


def use_dom(xml_file):
    # DOM steps:
    # 1. Read the whole XML file into a DOM tree.
    # 2. Get all <term> elements.
    # 3. For each <term>, get id, name, namespace, and count <is_a>.
    # 4. Update the result if this term has the largest number of <is_a> so far.

    results = make_results()

    DOMTree = xml.dom.minidom.parse(xml_file)
    collection = DOMTree.documentElement

    terms = collection.getElementsByTagName("term")

    for term in terms:
        go_id = get_text_from_tag(term, "id")
        name = get_text_from_tag(term, "name")
        namespace = get_text_from_tag(term, "namespace")

        is_a_list = term.getElementsByTagName("is_a")
        number_of_is_a = is_a_list.length

        update_results(results, namespace, go_id, name, number_of_is_a)

    return results


class GOHandler(xml.sax.ContentHandler):

    def __init__(self):
        # Set up storage for final results.
        # Set up temporary variables for the current <term>.
        self.results = make_results()

        self.current_data = ""
        self.in_term = False

        self.go_id = ""
        self.name = ""
        self.namespace = ""
        self.number_of_is_a = 0

    def startElement(self, tag, attributes):
        # When a new tag starts, remember its name.
        # If it is <term>, reset all temporary variables.
        # If it is <is_a>, add 1 to the current count.

        self.current_data = tag

        if tag == "term":
            self.in_term = True

            self.go_id = ""
            self.name = ""
            self.namespace = ""
            self.number_of_is_a = 0

        elif self.in_term and tag == "is_a":
            self.number_of_is_a = self.number_of_is_a + 1

    def characters(self, content):
        # SAX may read text in small pieces.
        # Therefore, use += to collect all text inside id, name, and namespace.

        if self.in_term:
            if self.current_data == "id":
                self.go_id = self.go_id + content

            elif self.current_data == "name":
                self.name = self.name + content

            elif self.current_data == "namespace":
                self.namespace = self.namespace + content

    def endElement(self, tag):
        # When a </term> ends, we have finished reading one GO term.
        # Now compare it with the current best result for that ontology.

        if tag == "term":
            update_results(
                self.results,
                self.namespace,
                self.go_id,
                self.name,
                self.number_of_is_a
            )

            self.in_term = False

        self.current_data = ""


def use_sax(xml_file):
    # SAX steps:
    # 1. Make a SAX parser.
    # 2. Turn off XML namespaces.
    # 3. Attach our GOHandler.
    # 4. Parse the XML file.
    # 5. Return the results stored in the handler.

    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    Handler = GOHandler()
    parser.setContentHandler(Handler)

    parser.parse(xml_file)

    return Handler.results


def main():
    xml_file = "go_obo.xml"

    # Run DOM version and record time.
    dom_start = datetime.now()
    dom_results = use_dom(xml_file)
    dom_end = datetime.now()
    dom_time = dom_end - dom_start

    # Run SAX version and record time.
    sax_start = datetime.now()
    sax_results = use_sax(xml_file)
    sax_end = datetime.now()
    sax_time = sax_end - sax_start

    print_results("DOM", dom_results)
    print_results("SAX", sax_results)

    print("\nTiming")
    print("DOM time:", dom_time)
    print("SAX time:", sax_time)

    if dom_results == sax_results:
        print("\nDOM and SAX results are the same.")
    else:
        print("\nDOM and SAX results are different. Check your code.")

    if dom_time < sax_time:
        print("DOM was faster.")
    elif sax_time < dom_time:
        print("SAX was faster.")
    else:
        print("DOM and SAX took the same time.")

    # SAX was faster than DOM in my run.


main()
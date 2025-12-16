"""
GraphRAG placeholder module.

This simulates how public-sector entities (policies, procedures, risks)
could be represented in a knowledge graph (e.g. Neo4j, Neptune).

Used for demonstration and future extension.
"""

# Example in-memory graph representation
GRAPH = {
    "Data Handling Policy": {
        "type": "policy",
        "links": ["Model Usage Guidance"],
    },
    "Model Usage Guidance": {
        "type": "guidance",
        "links": ["Incident Response SOP"],
    },
    "Incident Response SOP": {
        "type": "procedure",
        "links": [],
    },
}

def get_related_entities(entity: str) -> list[str]:
    node = GRAPH.get(entity)
    if not node:
        return []
    return node.get("links", [])
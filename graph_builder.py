from neo4j import GraphDatabase
import os

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def insert_question(tx, question_id, text):
    tx.run("MERGE (q:Question {id: $id}) SET q.text = $text", id=question_id, text=text)

def insert_relation(tx, from_id, to_id, relation):
    tx.run(f"""
        MATCH (a:Question {{id: $from_id}}), (b:Question {{id: $to_id}})
        MERGE (a)-[r:{relation}]->(b)
    """, from_id=from_id, to_id=to_id)

def build_graph(questions):
    with driver.session() as session:
        for q in questions:
            session.write_transaction(insert_question, q["id"], q["text"])
            for rel in q.get("relations", []):
                session.write_transaction(insert_relation, q["id"], rel["target"], rel["type"])

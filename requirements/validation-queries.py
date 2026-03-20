from rdflib import Graph
import re

GRAPH_FILE = "output-hospital.ttl"
GRAPH_FORMAT = "turtle"
QUERIES_FILE = "queries.rq"

def extract_prefixes(text: str) -> str:
    return "\n".join(
        line for line in text.splitlines()
        if line.strip().upper().startswith("PREFIX")
    )

def split_queries_with_titles(text: str):
    pattern = re.compile(
        r'#\s*\d+\.\s*(.*?)\n.*?(SELECT|ASK|CONSTRUCT|DESCRIBE)\b.*?(?=\n\s*#\s*-{3,}|\Z)',
        flags=re.IGNORECASE | re.DOTALL
    )

    queries = []
    for match in pattern.finditer(text):
        title = match.group(1).strip()
        query_start = match.start(2)
        query_text = text[query_start:match.end()].strip()
        queries.append((title, query_text))

    return queries

def main():
    g = Graph()
    g.parse(GRAPH_FILE, format=GRAPH_FORMAT)

    print(f"Grafo cargado\n")

    with open(QUERIES_FILE, encoding="utf-8") as f:
        content = f.read()

    prefix_block = extract_prefixes(content)
    queries = split_queries_with_titles(content)

    for i, (title, q) in enumerate(queries, start=1):
        print("=" * 80)
        print(f"QUERY {i} - {title}")
        print("=" * 80)

        full_query = prefix_block + "\n\n" + q

        try:
            results = g.query(full_query)

            if results.type == "ASK":
                print(bool(results))
            else:
                rows = list(results)
                if not rows:
                    print("Sin resultados")
                else:
                    for row in rows[:10]:
                        print(" | ".join(str(v) for v in row))
                    if len(rows) > 10:
                        print(f"... {len(rows) - 10} filas más")
        except Exception as e:
            print("Error:", e)

        print()

if __name__ == "__main__":
    main()
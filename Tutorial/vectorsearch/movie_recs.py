import pymongo
import requests

client = pymongo.MongoClient("mongodb+srv://rajharsh209:SYHYLy4Pik2OIJ1n@cluster0.16ovg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.sample_mflix
collection = db.movies

# print(collection.find().limit(5))

# items = collection.find().limit(5)
# for item in items:
#     print(item)

hf_token = "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"
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

def generate_embedding(text:str) -> list[float]:

    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {hf_token}"},
        json={"inputs": text}
    )

    if response.status_code != 200:
        raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")
    
    return response.json()

for doc in collection.find({
'plot': {"$exists": True}
}).limit(50):
    doc['plot_embedding_hf'] = generate_embedding(doc['plot'])
    collection.replace_one({'_id': doc['_id']}, doc)

# print(generate_embedding("Vector search with mongodb"))

query = "imaginary characters from outer space at war"

results = collection.aggregate([
    {
        "$vectorSearch": {
            "queryVector":generate_embedding(query),
            "path": "plot_embedding_hf",
            "numCandidates": 100,
            "limit": 4,
            "index": "PlotSemanticSearch",
        }
    }
])

for document in results:
    print(f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')
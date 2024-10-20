from RAG import getTopKDocs
from query_db import getTopChunks
from query_db import gemini, geminiWithReferences

# orchestrates the two-level RAG Filtering
# gets top k (5) research papers based on the query
# retrieves top relevant chunks from these 5 research papers
# generates the answer 

def getFinalAnswer(query):
    """Get Final Query Response

    Args:
        query (str): input query

    Returns:
        finalResult: consolidated answer to the query 
    """
    doc_ids = getTopKDocs(query)
    totalChunks = []
    collectionName = "research-paper-"
    for id in doc_ids:
        topChunks = getTopChunks(query, collectionName + str(id))
        totalChunks.extend(topChunks)
    
    #finalResult = gemini(query, totalChunks)
    finalResult = geminiWithReferences(query, totalChunks, doc_ids)
    return finalResult

# print("--------------------------")
# print("FINAL ANSWER")
# #ans = getFinalAnswer("What are Transformers?")
# ans = getFinalAnswer("How do GLU variants improve transformer?")
# #ans = getFinalAnswer("Techniques to prune deep neural networks")
# print(ans)
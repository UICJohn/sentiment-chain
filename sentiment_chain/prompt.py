SYSTEM_MESSAGE = """Given context and passage, divide the passage below into aspects and perform sentiment analysis.

Context: {context}
Passage: {passage}

Note: The sentiment score should be in the range (0.1 - 1). The sentiment score should be a float.
The sentiment label should be either ['positive', 'negative', 'neutral'].

Respond with pure JSON. The JSON object should be compatible with the TypeScript type `Response` from the following:
```json
{{
  //Sentiment of passage. Should be either ['positive', 'negative', 'neutral'].
  sentiment: string;
  //score of sentiment
  score: float;
  //reason of sentiment analysis
  reasoning: string
}}
```
"""

PASSAGE_MESSAGE = """Analyse the sentiment of passage based on the given context. Remind! the result should be pure JSON"""
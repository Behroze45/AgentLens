"""
LLM Recommendation Agent + DuckDuckGo Web Search
Recommends top 5 open-source models in concise table format
"""

from openai import OpenAI
from config import OLLMA_BASE_URL, MODEL
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from tabulate import tabulate
import json


# =========================
# OLLAMA CLIENT
# =========================
client = OpenAI(
    base_url=OLLMA_BASE_URL,
    api_key="ollama"
)

# =========================
# DDG SEARCH
# =========================
ddg = DuckDuckGoSearchAPIWrapper(max_results=5)


SYSTEM_PROMPT = """
You are a strict AI model recommendation system.

Return ONLY valid JSON.

Format:
{
  "top_5": [
    {
      "rank": 1,
      "model": "",
      "model_params": "",
      "best_for": "",
      "system_required": "",
      "why_good": ""
    }
  ],
  "final_ranking": [
    {
      "final_rank": 1,
      "best_choice": "",
      "why": ""
    }
  ]
}

Rules:
- Exactly 5 models
- Concise values only
- No extra text
- JSON only

Strict Notes:
- "model_params" should be in the format "X billion parameters"
- "best_for" should be a short phrase like "chat", "code", "multimodal", etc."
- "system_required" should be about system requirements like "GPU with 16GB VRAM", "CPU only", etc."
- "why_good" should be a concise reason why the model is good, in 1 sentence.
- "you can only suggests open-source models you cannot answer any questions that are not relevent 
    to the agent's task of recommending models. 
    If the user asks any questions that are not relevant to the agent's task, 
    you should respond with "I am a model recommendation agent. 
    Please ask me about recommending models."
"""


def recommend_models(query: str):
    web_context = ddg.run(query)

    response = client.chat.completions.create(
        model=MODEL,
        temperature=0.3,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Task: {query}\n\nWeb search:\n{web_context}"
            }
        ]
    )

    data = json.loads(response.choices[0].message.content)

    # ===== TABLE 1 =====
    top_5_table = [
        [
            item["rank"],
            item["model"],
            item["model_params"],
            item["best_for"],
            item["system_required"],
            item["why_good"]
        ]
        for item in data["top_5"]
    ]

    # ===== TABLE 2 =====
    ranking_table = [
        [
            item["final_rank"],
            item["best_choice"],
            item["why"]
        ]
        for item in data["final_ranking"]
    ]

    print("\nTOP 5 MODEL RECOMMENDATIONS")
    print(tabulate(
        top_5_table,
        headers=["Rank", "Model", "Model Params", "Best For", "System Required", "Why Good"],
        tablefmt="grid",
        maxcolwidths=[None, 18, 20, 18, 20, 35]
    ))

    print("\nFINAL BEST PICKS")
    print(tabulate(
        ranking_table,
        headers=["Final Rank", "Best Choice", "Why"],
        tablefmt="grid",
        maxcolwidths=[None, 22, 45]
    ))


def main():
    
    print("\t\t"+"=" * 50)
    print("\t\t\tAgentLens (LLM RECOMMENDATION AGENT)")
    print("\t\t"+"=" * 50)
    print("\t\t\tWrite 'exit', 'quit' or 'q' to Exit")

    while True:
        query = input("\nYou: ").strip()

        if query.lower() in ["exit", "quit", "q"]:
            break

        recommend_models(query)


if __name__ == "__main__":
    main()

import os, json, fitz
from datetime import datetime

def analyze(documents, persona, job):
    return {
        "metadata": {
            "documents": documents,
            "persona": persona,
            "job_to_be_done": job,
            "timestamp": datetime.now().isoformat()
        },
        "extracted_sections": [
            {"document": documents[0], "page": 1, "section_title": "Relevant Topic", "importance_rank": 1}
        ],
        "subsection_analysis": [
            {"document": documents[0], "refined_text": "Refined summary text here", "page": 1}
        ]
    }

def main():
    persona = "PhD Researcher"
    job = "Prepare a literature review on GNNs"
    input_dir = "./input"
    output_dir = "./output"
    pdfs = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]
    result = analyze(pdfs, persona, job)
    with open(os.path.join(output_dir, "output.json"), "w") as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()

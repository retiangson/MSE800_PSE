"""
AI CV Reader & Analyzer (GPT-4o)
--------------------------------
Reads your CV file directly as bytes, uploads it to GPT-4o,
and lets the AI interpret, translate (if needed), and recommend improvements.
Displays results in a clean, readable text format.

Supports PDF, DOCX, TXT.
"""

import json
import re
from pathlib import Path
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def clean_json_output(text: str):
    """Extract and clean JSON from GPT responses (handles ```json``` blocks)."""
    codeblock = re.search(r"```(?:json)?(.*?)```", text, re.DOTALL)
    if codeblock:
        text = codeblock.group(1)
    text = text.strip()

    # Try to parse JSON safely
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start, end = text.find("{"), text.rfind("}")
        if start != -1 and end > start:
            try:
                return json.loads(text[start:end + 1])
            except Exception:
                pass
        return {"raw_output": text}


def format_as_text(result: dict) -> str:
    """Pretty-print GPT analysis as readable text."""
    if "raw_output" in result:
        return result["raw_output"]

    output = []
    output.append("CV ANALYSIS REPORT\n" + "=" * 60)

    if "summary" in result:
        output.append(f"\nSummary:\n{result['summary']}")

    if "strengths" in result:
        output.append("Strengths:")
        for s in result["strengths"]:
            output.append(f"  • {s}")

    if "improvement_areas" in result:
        output.append("\nAreas for Improvement:")
        for s in result["improvement_areas"]:
            output.append(f"  • {s}")

    if "recommendations" in result:
        output.append("\nRecommendations:")
        for s in result["recommendations"]:
            output.append(f"  • {s}")

    if "suggested_keywords" in result:
        output.append("\nSuggested Keywords:")
        output.append("  " + ", ".join(result["suggested_keywords"]))

    if "sample_bullet_rewrite" in result:
        rewrite = result["sample_bullet_rewrite"]
        output.append("\n Sample Bullet Rewrite:")
        output.append(f"  Before: {rewrite.get('before', '')}")
        output.append(f"  After : {rewrite.get('after', '')}")

    output.append("\n" + "=" * 60)
    return "\n".join(output)


def analyze_cv_bytes(file_path: str, target_role: str, region: str, translate_to: str = "English"):
    """Convert CV to bytes and let GPT-4o read + analyze + recommend."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    print(f"Uploading '{path.name}' to GPT-4o for analysis...")

    with open(path, "rb") as f:
        file_bytes = f.read()

    uploaded = client.files.create(file=(path.name, file_bytes), purpose="assistants")

    prompt = f"""
You are a multilingual AI career coach and CV reviewer.
Read the uploaded file and, if it is not in {translate_to}, translate it first.

Then provide:
1. A short professional summary of the candidate.
2. Strengths (bullet list).
3. Areas for improvement.
4. Concrete recommendations to align the CV with current technology trends
   (AI, Cloud, DevOps, Data, Security, Full-Stack, etc.).
5. Suggested keywords and tools to add.
6. A sample bullet rewrite (before → after) for better impact.

Target role: {target_role}
Region: {region}

Return ONLY valid JSON with the following keys:
summary, strengths, improvement_areas, recommendations, suggested_keywords, sample_bullet_rewrite.
"""

    response = client.responses.create(
        model="gpt-4o",
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": prompt},
                    {"type": "input_file", "file_id": uploaded.id},
                ],
            }
        ],
    )

    raw_output = response.output[0].content[0].text.strip()
    return clean_json_output(raw_output)


def main():
    print("AI CV READER & ANALYZER (GPT-4o)")
    print("------------------------------------")

    file_path = input("Enter CV file path (PDF/DOCX/TXT): ").strip().strip('"')
    target_role = input("Target role (e.g., Software Engineer, Cloud Architect): ").strip() or "Software Engineer"
    region = input("Region / market (e.g., New Zealand, Global): ").strip() or "Global"
    translate_to = input("Translate CV to (default: English): ").strip() or "English"

    print("\nProcessing file... Please wait...\n")
    result = analyze_cv_bytes(file_path, target_role, region, translate_to)

    print("Analysis complete!\n")
    print(format_as_text(result))


if __name__ == "__main__":
    main()

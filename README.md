# Paper Extractor

Reads a research paper PDF and uses the Gemini API to produce a
summary, a Mermaid flowchart, 3 project ideas and paper metadata.

## How to run
1. pip install pypdf google-genai
2. Set the GEMINI_API_KEY environment variable
3. Put your paper in this folder as paper.pdf
4. python extractor.py
5. Read output.md
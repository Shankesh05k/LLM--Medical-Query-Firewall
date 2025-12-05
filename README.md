A Python-based medical safety filter analyzes user queries. It identifies harmful, unsafe, or dosage-related medical questions before they reach a medical AI model.
This firewall prevents the chatbot from responding to unsafe queries such as self-medication, dosage instructions, prescription misuse, or harmful medical intent.
Built with Tkinter GUI and a keyword-based rule engine, this tool shows how a language model can be equipped with a safety layer.

1. Firewall Rule Engine

The classifier blocks queries that include:
- Medication dosage (mg, ml, "how much", "how many")
- Self-medication intent ("prescribe", "give me medicine")
- Medicine names ("dolo", "paracetamol", "amoxicillin")
- Numeric values indicating possible dosage (e.g., "650")
Each block provides a clear reason and a safe alternative suggestion.

2. Safe/Blocked Classification

Your code classifies queries into:
- Result: Allowed; Meaning: Safe to send to an LLM
- Result: Blocked; Meaning: Potentially harmful medical question

3. Tkinter GUI-Based Chat Interface

The application features:
- Multi-line query input box
- "Run Firewall" button
- Color-coded safety results
- Scrollable output window for explanations
- No external dependencies (standard Python only)

4. LLM Simulation Mode

If the query is safe, the app displays a simulated LLM response. You can easily replace this with:
- OpenAI API
- HuggingFace model
- Local LLM

-> How It Works (Internal Logic)

1. The user enters a medical question.
Example: Is Dolo good for fever?

2. The firewall checks using four rule sets:
=> Rule 1: Detect numeric dosage
if token.isdigit():

=> Rule 2: Danger keywords
Checks words like:
dose, dosage, mg, ml, tablet, pill, self medicate

=> Rule 3: Unsafe intent
give me dosage
recommend medicine
how much should I take

=> Rule 4: Medicine names
paracetamol, dolo, amoxicillin, ibuprofen

3. If unsafe → BLOCK
The GUI displays:

"Query BLOCKED"

Reason: which keyword triggered it

=> Safe alternative guidance

4. If safe → ALLOW

The firewall displays:

Query is SAFE.
Simulated LLM response: I can help with general health information.

Installation & Usage
=> Requirements
Python 3.8+
Tkinter (included in standard Python on Windows/Mac/Linux)
=> Run the App
python medical_firewall.py

Project Structure
Medical-LLM-Firewall

--- medical_firewall.py    
--- README.md               

-> Screenshot (Add if needed)
(Optional: Insert a screenshot of your Tkinter UI here)

Extending the Firewall
You can easily upgrade the system by adding:

=> More keyword categories
Emergency symptoms
Drug interactions
Illegal drugs
Sensitive procedures

=> ML-based classification

Replace rules with:
BERT-based intent classifier
spaCy NER for drug names
FastText keyword embeddings

=> Connect to a real LLM

Replace the simulated response with OpenAI:
# Replace simulated response with an API call
api_response = llm_client.chat(query)

📄 Smart Resume Parser

A Python-based NLP web application that extracts structured information from resumes in PDF and DOCX formats.

This project uses spaCy, Regex, and Streamlit to automatically parse resumes and convert them into structured data formats like JSON and CSV.

🚀 Features

Upload resumes in PDF or DOCX format

Extract:

👤 Name

📧 Email

📱 Phone Number

💼 Skills

🎓 Education

🧠 Experience

Display structured output

Download results as JSON

Download results as CSV

Clean and simple Streamlit UI

🛠️ Tech Stack

Python

Streamlit

spaCy

PyMuPDF

python-docx

Pandas

Regular Expressions

📂 Project Structure
smart_resume_parser/
│
├── app.py                # Streamlit UI
├── parser.py             # NLP extraction logic
├── extractor.py          # PDF/DOCX text extraction
├── utils.py              # Text cleaning
├── requirements.txt      # Dependencies
├── test_resumes/         # Sample resumes for testing
└── outputs/              # Exported files
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/smart-resume-parser.git
cd smart-resume-parser
2️⃣ (Optional) Create Virtual Environment
python -m venv venv

Activate it:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Download spaCy Model
python -m spacy download en_core_web_sm
▶️ Run the Application
streamlit run app.py

Open your browser at:

http://localhost:8501

Upload a resume and view extracted information.

🧪 Testing the Application

Add 5 sample resumes inside:

test_resumes/

Upload them one by one in the Streamlit UI.

Recommended test cases:

Fresher resume

2+ years experience

5+ years experience

Technical resume

Non-technical resume

📤 Sample Output Format
{
  "Name": "John Doe",
  "Email": "john.doe@gmail.com",
  "Phone": "+91-9876543210",
  "Skills": ["Python", "SQL", "Machine Learning"],
  "Education": ["B.Tech"],
  "Experience": [["3", "years"]]
}
📈 Future Improvements

Total experience calculation

Resume ranking based on job description

Advanced section detection

Database integration

REST API support

Cloud deployment

🎯 Use Cases

HR Resume Screening

Applicant Tracking Systems (ATS)

NLP Academic Projects

Portfolio Projects

Automation Tools

👨‍💻 Author

Varun Kumar

📜 License

This project is open-source and available under the MIT License.

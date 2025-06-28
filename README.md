# Resume-Analyzer-CLI-Tool
Resume Analyzer CLI Tool
A powerful Python command-line tool that analyzes PDF resumes to extract skills, count keyword mentions, and provide actionable improvement suggestions based on industry standards.
Features

PDF Text Extraction: Uses PyMuPDF for robust text extraction from PDF resumes
Skill Detection: Identifies 80+ technical skills across 6 major categories
Skill Scoring: Provides an overall skill diversity score (0-100)
Smart Suggestions: Generates personalized improvement recommendations
Multiple Output Formats: Console display or JSON export
Cross-Platform: Works on Windows, macOS, and Linux with colored output

Skill Categories Analyzed

Programming Languages: Python, Java, JavaScript, C++, etc.
Web Technologies: React, Angular, Node.js, Django, etc.
Databases: SQL, PostgreSQL, MongoDB, Redis, etc.
Cloud & DevOps: AWS, Docker, Kubernetes, Jenkins, etc.
Data Science & ML: TensorFlow, Pandas, Machine Learning, etc.
Tools & Frameworks: Git, Linux, REST API, Agile, etc.

Installation
Option 1: Clone and Install
bashgit clone https://github.com/yourusername/resume-analyzer.git
cd resume-analyzer
pip install -r requirements.txt
Option 2: Direct Installation
bashpip install PyMuPDF colorama
Option 3: Development Installation
bashgit clone https://github.com/yourusername/resume-analyzer.git
cd resume-analyzer
pip install -e .
Usage
Basic Usage
bashpython resume_analyzer.py /path/to/resume.pdf
Advanced Usage
bash# JSON output
python resume_analyzer.py resume.pdf --output json

# Save results to file
python resume_analyzer.py resume.pdf --save-json results.json

# View help
python resume_analyzer.py --help
Example Output
============================================================
                    RESUME ANALYSIS REPORT
============================================================
File: john_doe_resume.pdf
Overall Skill Score: 75/100

SKILLS FOUND:
----------------------------------------

Programming Languages:
  • Python (3 mentions)
  • Javascript (2 mentions)
  • Java (1 mention)

Web Technologies:
  • React (2 mentions)
  • Node.js (1 mention)
  • Html (1 mention)

Databases:
  • Sql (4 mentions)
  • Postgresql (1 mention)

Cloud & DevOps:
  • Aws (2 mentions)
  • Docker (1 mention)
  • Git (1 mention)

Data Science & ML: No skills found

Tools & Frameworks:
  • Rest Api (1 mention)
  • Linux (1 mention)

Total unique skills found: 12

IMPROVEMENT SUGGESTIONS:
----------------------------------------
1. Consider adding skills from these categories: Data Science & ML
2. Consider adding popular Data Science & ML skills: Machine Learning, Pandas, TensorFlow
3. Cloud skills (AWS, Azure, Docker) are highly valued in today's market
============================================================
Project Structure
resume-analyzer/
├── resume_analyzer.py      # Main CLI tool
├── requirements.txt        # Python dependencies
├── setup.py               # Package setup
├── README.md              # This file
├── examples/              # Example resumes (optional)
└── tests/                 # Unit tests (optional)
Requirements

Python 3.7+
PyMuPDF (for PDF processing)
colorama (for colored terminal output)

How It Works

Text Extraction: Uses PyMuPDF to extract text from PDF files
Text Cleaning: Normalizes text and removes special characters
Skill Matching: Uses regex patterns to find skill mentions
Scoring Algorithm:

Category coverage (50 points max)
Total unique skills (50 points max)


Suggestion Engine: Analyzes gaps and recommends improvements

Customization
You can easily customize the skill categories by modifying the skill_categories dictionary in the ResumeAnalyzer class:
pythonself.skill_categories = {
    'Your Category': ['skill1', 'skill2', 'skill3'],
    # Add more categories...
}
Contributing

Fork the repository
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request

Roadmap

 Support for Word documents (.docx)
 Integration with job posting APIs for targeted suggestions
 Machine learning-based skill extraction
 Web interface version
 ATS (Applicant Tracking System) compatibility scoring
 Industry-specific skill recommendations

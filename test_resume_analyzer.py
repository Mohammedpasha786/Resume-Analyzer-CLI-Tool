#!/usr/bin/env python3
"""
Test script for the Resume Analyzer CLI tool.
"""

import unittest
import tempfile
import os
import json
from unittest.mock import patch, mock_open
from resume_analyzer import ResumeAnalyzer


class TestResumeAnalyzer(unittest.TestCase):
    """Test cases for ResumeAnalyzer class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.analyzer = ResumeAnalyzer()
        self.sample_text = """
        John Doe
        Software Engineer
        
        Skills: Python, JavaScript, React, SQL, AWS, Docker, Machine Learning
        
        Experience:
        - Developed web applications using React and Node.js
        - Implemented machine learning models with TensorFlow and Pandas
        - Managed cloud infrastructure on AWS with Docker containers
        - Database design and optimization using PostgreSQL
        """
    
    def test_clean_text(self):
        """Test text cleaning functionality."""
        dirty_text = "  Text  with   extra    spaces\n\nand\tspecial@#$%characters  "
        clean = self.analyzer.clean_text(dirty_text)
        self.assertIn("text with extra spaces", clean)
        self.assertNotIn("@#$%", clean)
    
    def test_find_skills(self):
        """Test skill detection in text."""
        skill_counts = self.analyzer.find_skills(self.sample_text.lower())
        
        # Check that skills are found
        prog_langs = skill_counts['Programming Languages']
        self.assertIn('python', prog_langs)
        self.assertIn('javascript', prog_langs)
        
        web_tech = skill_counts['Web Technologies']
        self.assertIn('react', web_tech)
        
        databases = skill_counts['Databases']
        self.assertIn('sql', databases)
        self.assertIn('postgresql', databases)
        
        cloud = skill_counts['Cloud & DevOps']
        self.assertIn('aws', cloud)
        self.assertIn('docker', cloud)
        
        ml = skill_counts['Data Science & ML']
        self.assertIn('machine learning', ml)
        self.assertIn('tensorflow', ml)
        self.assertIn('pandas', ml)
    
    def test_calculate_skill_score(self):
        """Test skill score calculation."""
        # Test with good skill distribution
        good_skills = {
            'Programming Languages': {'python': 2, 'javascript': 1},
            'Web Technologies': {'react': 1, 'node.js': 1},
            'Databases': {'sql': 2, 'postgresql': 1},
            'Cloud & DevOps': {'aws': 1, 'docker': 1},
            'Data Science & ML': {'machine learning': 1, 'tensorflow': 1},
            'Tools & Frameworks': {'git': 1, 'linux': 1}
        }
        score = self.analyzer.calculate_skill_score(good_skills)
        self.assertGreater(score, 70)  # Should get a good score
        
        # Test with poor skill distribution
        poor_skills = {
            'Programming Languages': {'python': 1},
            'Web Technologies': {},
            'Databases': {},
            'Cloud & DevOps': {},
            'Data Science & ML': {},
            'Tools & Frameworks': {}
        }
        score = self.analyzer.calculate_skill_score(poor_skills)
        self.assertLess(score, 30)  # Should get a low score
    
    def test_suggest_improvements(self):
        """Test improvement suggestions generation."""
        # Test with missing categories
        skills_with_gaps = {
            'Programming Languages': {'python': 2},
            'Web Technologies': {},
            'Databases': {'sql': 1},
            'Cloud & DevOps': {},
            'Data Science & ML': {},
            'Tools & Frameworks': {}
        }
        suggestions = self.analyzer.suggest_improvements(skills_with_gaps)
        self.assertGreater(len(suggestions), 0)
        
        # Check that suggestions mention missing categories
        suggestions_text = ' '.join(suggestions).lower()
        self.assertIn('categories', suggestions_text)
    
    @patch('fitz.open')
    def test_extract_text_from_pdf_success(self, mock_fitz_open):
        """Test successful PDF text extraction."""
        # Mock PyMuPDF document
        mock_page = mock_fitz_open.return_value.__enter__.return_value.__getitem__.return_value
        mock_page.get_text.return_value = "Sample resume text"
        mock_fitz_open.return_value.__enter__.return_value.page_count = 1
        
        result = self.analyzer.extract_text_from_pdf("dummy.pdf")
        self.assertEqual(result, "Sample resume text")
    
    @patch('fitz.open')
    def test_extract_text_from_pdf_failure(self, mock_fitz_open):
        """Test PDF text extraction failure."""
        mock_fitz_open.side_effect = Exception("File not found")
        
        result = self.analyzer.extract_text_from_pdf("nonexistent.pdf")
        self.assertEqual(result, "")
    
    def test_skill_categories_completeness(self):
        """Test that all skill categories are properly defined."""
        expected_categories = [
            'Programming Languages',
            'Web Technologies', 
            'Databases',
            'Cloud & DevOps',
            'Data Science & ML',
            'Tools & Frameworks'
        ]
        
        for category in expected_categories:
            self.assertIn(category, self.analyzer.skill_categories)
            self.assertGreater(len(self.analyzer.skill_categories[category]), 0)
    
    def test_all_skills_mapping(self):
        """Test that all_skills mapping is correctly generated."""
        # Check that skills from categories are in all_skills
        for category, skills in self.analyzer.skill_categories.items():
            for skill in skills:
                self.assertIn(skill.lower(), self.analyzer.all_skills)
                self.assertEqual(self.analyzer.all_skills[skill.lower()], category)
    
    @patch.object(ResumeAnalyzer, 'extract_text_from_pdf')
    def test_analyze_resume_integration(self, mock_extract):
        """Test the complete analyze_resume workflow."""
        mock_extract.return_value = self.sample_text
        
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            results = self.analyzer.analyze_resume(tmp_path, output_format='json')
            
            # Check that results contain expected keys
            expected_keys = ['file_path', 'skill_counts', 'score', 'suggestions', 'total_skills']
            for key in expected_keys:
                self.assertIn(key, results)
            
            # Check that some skills were found
            self.assertGreater(results['total_skills'], 0)
            self.assertGreater(results['score'], 0)
            
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)


class TestCLIIntegration(unittest.TestCase):
    """Test CLI functionality."""
    
    @patch('sys.argv', ['resume_analyzer.py', '--help'])
    def test_help_argument(self):
        """Test that help argument works."""
        from resume_analyzer import main
        with self.assertRaises(SystemExit):
            main()
    
    @patch('sys.argv', ['resume_analyzer.py', '--version'])
    def test_version_argument(self):
        """Test that version argument works."""
        from resume_analyzer import main
        with self.assertRaises(SystemExit):
            main()


def create_sample_pdf_text():
    """Create sample text that would be extracted from a PDF."""
    return """
    Jane Smith
    Senior Software Developer
    Email: jane.smith@email.com
    Phone: (555) 123-4567
    
    TECHNICAL SKILLS
    Programming Languages: Python, Java, JavaScript, TypeScript, C++
    Web Technologies: React, Angular, Node.js, Express, HTML, CSS
    Databases: PostgreSQL, MongoDB, Redis, MySQL
    Cloud & DevOps: AWS, Docker, Kubernetes, Jenkins, Git
    Data Science: Pandas, NumPy, Scikit-learn, TensorFlow
    Tools: Linux, Vim, Postman, JIRA, Agile
    
    PROFESSIONAL EXPERIENCE
    
    Senior Software Developer | TechCorp Inc. | 2020 - Present
    • Developed scalable web applications using React and Node.js
    • Implemented machine learning models with TensorFlow and Python
    • Managed cloud infrastructure on AWS using Docker and Kubernetes
    • Designed and optimized PostgreSQL databases for high-performance applications
    • Led agile development teams and mentored junior developers
    
    Software Developer | StartupXYZ | 2018 - 2020  
    • Built REST APIs using Java Spring framework
    • Developed responsive frontend applications with Angular and TypeScript
    • Implemented CI/CD pipelines using Jenkins and Git
    • Worked with MongoDB for document-based data storage
    
    EDUCATION
    Bachelor of Science in Computer Science
    University of Technology | 2014 - 2018
    
    PROJECTS
    • E-commerce Platform: Full-stack application using React, Node.js, and PostgreSQL
    

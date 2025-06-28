from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="resume-analyzer",
    version="1.0.0",
    author="Resume Analyzer Developer",
    description="A CLI tool for analyzing PDF resumes and providing skill-based improvement suggestions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/resume-analyzer",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "PyMuPDF>=1.23.0",
        "colorama>=0.4.6",
    ],
    entry_points={
        "console_scripts": [
            "resume-analyzer=resume_analyzer:main",
        ],
    },
)

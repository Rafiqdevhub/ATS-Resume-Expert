# ATS Resume Expert 📑

An AI-powered Resume Analysis Tool that helps job seekers optimize their resumes for Applicant Tracking Systems (ATS) using Google's Gemini AI.

## Features

- **Resume Analysis**: Upload your resume and get detailed feedback
- **Job Description Matching**: Compare your resume against specific job descriptions
- **AI-Powered Insights**: Leverages Google's Gemini AI for intelligent analysis
- **PDF Support**: Handles PDF resume uploads with smart image processing
- **Dual Analysis Modes**:
  - Detailed Resume Analysis
  - ATS Match Percentage

## Key Capabilities

1. **Detailed Resume Analysis**
   - Overall Match Assessment
   - Key Strengths Identification
   - Areas for Improvement
   - Technical Skills Alignment
   - Professional Experience Review
   - Personalized Recommendations

2. **ATS Match Analysis**
   - Overall Match Percentage
   - Key Matching Keywords Detection
   - Missing Keywords Identification
   - Format and Structure Analysis
   - Improvement Suggestions

## Technology Stack

- Python
- Streamlit
- Google Gemini AI
- PDF2Image
- Python Imaging Library (PIL)
- python-dotenv

## Setup and Installation

1. Clone the repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your Google API key:
   ```
   GOOGLE_API_KEY="your-api-key"
   ```
4. Run the application:
   ```
   streamlit run main.py
   ```

## Usage

1. Launch the application
2. Paste the job description in the left panel
3. Upload your resume (PDF format) in the right panel
4. Choose your analysis type:
   - Click "Detailed Resume Analysis" for comprehensive feedback
   - Click "Match Percentage" for ATS-focused analysis
5. Review the generated insights and recommendations

## Requirements

- Python 3.7+
- Google Gemini AI API key
- PDF resume file

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
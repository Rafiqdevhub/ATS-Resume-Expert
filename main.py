from dotenv import load_dotenv
import streamlit as st
import os
import PyPDF2 as pdf
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, resume_text, prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([input_text, resume_text, prompt])
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

st.set_page_config(
    page_title="ATS Resume Expert",
    page_icon="📑",
    layout="wide"
)

st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📑 ATS Resume Expert")
st.markdown("### Your AI-powered Resume Analysis Tool")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Job Description")
    input_text = st.text_area(
        "Paste the job description here:",
        height=200,
        key="input",
        help="Copy and paste the job description you want to match against"
    )

with col2:
    st.subheader("Upload Resume")
    uploaded_file = st.file_uploader(
        "Upload your resume (PDF format)",
        type=["pdf"],
        help="Please ensure your resume is in PDF format"
    )
    
    if uploaded_file is not None:
        st.success("✅ Resume uploaded successfully!")

st.markdown("---")
st.subheader("Analysis Options")

col1, col2, col3, col4 = st.columns(4)

with col1:
    submit1 = st.button("🔍 Detailed Resume Analysis", use_container_width=True)
with col2:
    submit3 = st.button("📊 Match Percentage", use_container_width=True)
with col3:
    submit2 = st.button("🔑 Missing Keywords", use_container_width=True)
with col4:
    submit4 = st.button("📚 Skill Improvement", use_container_width=True)

# Input prompts
input_prompt1 = """
You are an experienced Technical Human Resource Manager. Please provide a detailed analysis of the resume against the job description in the following format:

1. Overall Match Assessment
2. Key Strengths
3. Areas for Improvement
4. Technical Skills Alignment
5. Professional Experience Relevance
6. Recommendations
"""

input_prompt2 = """
As an ATS (Applicant Tracking System) expert, focus specifically on identifying missing keywords and gaps. Please analyze and provide:

1. Critical Missing Keywords
2. Industry-Specific Terms Not Present
3. Technical Skills Gaps
4. Action Verbs That Should Be Added
5. Specific Recommendations for Adding Keywords
"""

input_prompt3 = """
As an ATS (Applicant Tracking System) expert, please analyze the resume against the job description and provide:

1. Overall Match Percentage
2. Key Matching Keywords Found
3. Missing Important Keywords
4. Suggestions for Improvement
5. Format and Structure Analysis
"""

input_prompt4 = """
As a Career Development and Technical Skills Expert, analyze the resume against the job description and provide detailed recommendations for skill improvement:

1. Core Skills Gap Analysis
2. Learning Resources and Certifications
3. Practical Project Suggestions
4. Career Development Path
5. Timeline for Skill Acquisition
6. Industry-Standard Tools to Learn
"""

if submit1 or submit2 or submit3 or submit4:
    if not uploaded_file:
        st.error("⚠️ Please upload your resume first!")
    elif not input_text:
        st.warning("⚠️ Please provide a job description!")
    else:
        try:
            with st.spinner("Analyzing your resume..."):
                resume_text = input_pdf_text(uploaded_file)
                if submit1:
                    response = get_gemini_response(input_prompt1, resume_text, input_text)
                elif submit2:
                    response = get_gemini_response(input_prompt2, resume_text, input_text)
                elif submit3:
                    response = get_gemini_response(input_prompt3, resume_text, input_text)
                else:
                    response = get_gemini_response(input_prompt4, resume_text, input_text)
                
                st.markdown("### Analysis Results")
                st.markdown("---")
                st.markdown(response)
        except Exception as e:
            st.error(f"An error occurred during analysis: {str(e)}")









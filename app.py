from dotenv import load_dotenv
import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

# Load API keys
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text


def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert the PDF to images
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")


def generate_final_review(pdf_content, job_description):
    # Input prompts for AI to analyze resume against job description
    review_prompt = f"""
    You are an experienced recruiter or hiring manager. Your task is to review a resume based on a given job description.
    Highlight any key qualifications and experiences that align well with the job description.
    Mention any missing skills, keywords, or qualifications that could be added to better match the role.
    Evaluate how well the candidate’s past experience matches the requirements outlined in the job description.
    Suggest any improvements to better emphasize relevant experience (e.g., specific achievements, projects, or leadership roles).
    List any important keywords or industry-specific terminology from the job description that should be present in the resume but are missing.
    Suggest keywords that should be added to improve the resume’s alignment with the job description and increase its chances of passing through an Applicant Tracking System (ATS).

    Job Description: {job_description}

    Resume (in PDF form): {pdf_content}
    """

    response = get_gemini_response("Review the resume against the job description", pdf_content, review_prompt)
    return response


# Streamlit App with customized UI
st.set_page_config(page_title="ATS Resume Expert", page_icon=":briefcase:", layout="wide")

# Add custom CSS
st.markdown(
    """
    <style>
        /* Background gradient */
        body {
            background: linear-gradient(to right, #1e3c72, #2a5298);
            color: white;
        }
        
        /* Header style */
        .stHeader {
            color: #ffffff;
            text-align: center;
        }
        
        /* Main container */
        .stApp {
            border-radius: 15px;
            padding: 20px;
            background-color: #ffffff;
            color: #333333;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.25);
        }

        /* Button style */
        button {
            background-color: #1e90ff !important;
            color: white !important;
            border-radius: 8px !important;
        }

        /* Text Area */
        textarea {
            border: 1px solid #ccc;
            border-radius: 8px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.header("🎯 ATS Resume Expert", anchor="center")
st.subheader("Polish your resume and ensure it stands out!")

# User input: Job description
st.write("### 📝 Enter the Job Description:")
input_text = st.text_area(
    "Job Description:", 
    placeholder="Paste the job description here...",
    height=150,
    key="input"
)

# User upload: Resume PDF
st.write("### 📤 Upload Your Resume:")
uploaded_file = st.file_uploader(
    "Upload your resume (PDF)...", 
    type=["pdf"],
    help="Ensure the file is in PDF format."
)

if uploaded_file is not None:
    st.success("PDF Uploaded Successfully!")

# Buttons for interaction
st.write("### 🚀 Actions")
col1, col2, col3 = st.columns(3)

with col1:
    submit1 = st.button("🧐 Analyze Resume")

with col2:
    submit2 = st.button("📊 Match Percentage")

with col3:
    submit3 = st.button("📋 Final Review")

# Input prompts
input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are an ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
Your task is to evaluate the resume against the provided job description. 
Give me the percentage of match if the resume matches the job description. First, the output should come as percentage, 
followed by keywords missing, and then final thoughts.
"""

# Handle button actions
if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("🔍 The Analysis Result is:")
        st.write(response)
    else:
        st.error("Please upload your resume to proceed.")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        final_review = generate_final_review(pdf_content, input_text)
        st.subheader("📋 Final Review Based on Job Description and Resume:")
        st.write(final_review)
    else:
        st.error("Please upload your resume to proceed.")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("📊 Match Percentage Result:")
        st.write(response)
    else:
        st.error("Please upload your resume to proceed.")

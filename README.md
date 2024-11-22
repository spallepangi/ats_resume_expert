# **ATS Resume Expert**

## **Who Should Use This Tool?**
This tool is designed for:
- **Job seekers** who want to optimize their resumes for specific job descriptions.
- **Recruiters** and **hiring managers** who need quick insights into the alignment of a candidate’s resume with the job role.
- **Career coaches** who provide resume improvement suggestions to their clients.
- Anyone looking to enhance their resumes to pass **Applicant Tracking Systems (ATS)**.

---

## **Why Use ATS Resume Expert?**
In today’s competitive job market, ensuring your resume aligns with a job description is crucial. Many companies use ATS to filter resumes based on keyword matches. This tool:
1. **Analyzes resumes against job descriptions** to identify strengths and weaknesses.
2. Highlights **missing skills, keywords, and qualifications** that are vital for the role.
3. Offers actionable **suggestions to optimize resumes** for better ATS compatibility.
4. Generates a **final review with percentage alignment**, keyword suggestions, and detailed evaluation.

---

## **Key Features**
- **Resume Evaluation:** Assesses uploaded resumes against a job description.
- **Percentage Match Analysis:** Provides a match percentage along with missing keywords.
- **Final Review:** Offers an in-depth critique, including strengths, weaknesses, and actionable recommendations.

---

## **Workflow**
### **1. Upload Resume**
- Users upload their resume in **PDF format**.
- The first page of the PDF is processed using the `pdf2image` library.

### **2. Enter Job Description**
- Users provide the job description via a text box in the app.

### **3. Generate Insights**
- **Option 1:** Get a detailed evaluation of the resume's alignment with the job description.
- **Option 2:** Generate a percentage match, list missing keywords, and receive final thoughts.
- **Option 3:** Generate a comprehensive final review summarizing alignment, ATS improvements, and suggestions.

### **4. Receive Results**
- Results are displayed in the app interface, providing actionable feedback in real-time.

---

## **Tech Stack**
### **Backend:**
- **Python**: The core programming language.
- **Libraries Used:**
  - `dotenv`: For loading environment variables securely.
  - `base64`: For encoding PDF content.
  - `streamlit`: For building the web application.
  - `pdf2image`: For converting PDF resumes to images.
  - `Pillow (PIL)`: For handling image manipulation.
  - `google.generativeai`: For integrating with Gemini AI (Generative AI for content analysis).

### **Frontend:**
- **Streamlit**: Provides an interactive and intuitive user interface.

### **Environment Management:**
- **python-dotenv**: Securely loads API keys from a `.env` file.

### **Deployment:**
- **Streamlit Cloud**: Simplifies hosting and scaling the application.
- **System Dependency:** `Poppler` is required for PDF processing (installed via `packages.txt`).

### **Version Control:**
- **GitHub**: For managing the source code and collaborative development.
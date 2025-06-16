# Maktoob: Arabic Keyword-to-Text Generation System

Maktoob is a Python project that generates coherent Arabic paragraphs based on three user-provided Arabic keywords. It leverages the Hugging Face Transformers library for text generation.

## 🏗 Architecture

The system follows a modular architecture as depicted in the diagram:

1.  **User Input**: The user provides 3 Arabic keywords.
2.  **Prompt Construction**: A module selects a random Arabic sentence template and inserts the keywords into it to form a prompt.
3.  **Text Generation**: The Hugging Face `aubmindlab/aragpt2-medium` model generates a paragraph based on the constructed prompt.
4.  **Post-processing**: The generated text is refined by limiting its length and removing repetitions.
5.  **Final Output**: The processed Arabic paragraph is displayed to the user.

## 📂 Project Structure

```
Maktoob/
├── main.py
├── templates.py
├── postprocess.py
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

Follow these instructions to set up and run the Maktoob project.

### Prerequisites

*   Python 3.9+
*   `pip` (Python package installer)

### Installation

1.  **Clone the repository (or create the project structure manually):**

    ```bash
    git clone https://github.com/your-username/Maktoob.git
    cd Maktoob
    ```

    (Note: If you are not using git, create the `Maktoob` directory and the files within it manually.)

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### How to Run

1.  **Ensure your virtual environment is activated.**
2.  **Run the main script:**

    ```bash
    python main.py
    ```

3.  **When prompted, enter three Arabic keywords separated by commas.**

    Example: `الطاقة الشمسية, المناخ, البيئة`

## 💡 Example Usage

```
(venv) PS C:\Users\jasse\OneDrive\Bureau\Projects\Master Degree\Maktoob> python main.py
Loading model: aubmindlab/aragpt2-medium...
Model loaded successfully.
Please provide 3 Arabic keywords, separated by commas.
Enter keywords: الطاقة الشمسية, المناخ, البيئة

Constructed Prompt: تُعَدّ الطاقة الشمسية من المواضيع المهمة في مجال المناخ، لما لها من تأثير على البيئة.

Generating text...
Raw Generated Text: تُعَدّ الطاقة الشمسية من المواضيع المهمة في مجال المناخ، لما لها من تأثير على البيئة. وتُعدّ الطاقة الشمسية من أهم المصادر المتجددة للطاقة، حيث تُستخدم في توليد الكهرباء وتدفئة المياه. وتُساهم في الحد من ظاهرة الاحتباس الحراري، كما تُساهم في الحفاظ على البيئة من التلوث.

Applying post-processing...

--- Final Output ---
وتُعدّ الطاقة الشمسية من أهم المصادر المتجددة للطاقة، حيث تُستخدم في توليد الكهرباء وتدفئة المياه. وتُساهم في الحد من ظاهرة الاحتباس الحراري، كما تُساهم في الحفاظ على البيئة من التلوث.
Keywords found in output: الطاقة الشمسية, المناخ, البيئة
``` 
# 📚 Jupyter Notebooks - Learning Repository

**Developer:** Java Developer Learning Python & AI/ML  
**Last Updated:** December 4, 2025  
**Note:** Large gaps between sessions (quarterly) - documentation helps retention

---

## 🗂️ Projects Overview

| Notebook | Status | Topic | Difficulty | Time to Complete |
|----------|--------|-------|------------|------------------|
| `jyp-test.ipynb` | ✅ Complete | Python Basics | Beginner | 10 min |
| `HELLO.DS/hello.ipynb` | 🔄 In Progress | ML - Titanic Prediction | Intermediate | 1-2 hours |
| `langchain.ipynb` | ✅ Complete | LangChain + OpenAI | Intermediate | 30-45 min |
| `langchain_gregkamradt_yt.ipynb` | 🔄 Incomplete | LangChain Tutorial | Intermediate | 30 min |
| `speech-to-text-huggingface.ipynb` | 🚧 Started | Audio ML | Advanced | TBD |

---

## 📖 Quick Guide for Each Notebook

### 1️⃣ **jyp-test.ipynb** - Python Basics
**Purpose:** Hello World & Pandas introduction  
**When to use:** First time learning Python syntax  
**Key Concepts:**
- Basic print statements
- Pandas DataFrame creation
- Reading CSV files

**Quick Start:**
```bash
cd jupyter-notebook
# Open in VS Code or run: jupyter notebook jyp-test.ipynb
```

---

### 2️⃣ **HELLO.DS/hello.ipynb** - Titanic ML Project
**Purpose:** Complete machine learning pipeline - predict Titanic survival  
**Dataset:** `titanic3.csv` (1309 passengers)  
**Models:** Gaussian Naive Bayes, Neural Network (TensorFlow)

**What You'll Learn:**
- Data cleaning & preprocessing
- Exploratory Data Analysis (EDA) with visualizations
- Feature engineering
- Train/test split
- Model evaluation
- Neural network basics

**Quick Start:**
```bash
cd jupyter-notebook/HELLO.DS
# Run cells 1-15 for basic ML model
# Run cells 16+ for neural network
```

**Key Files:**
- `hello.ipynb` - Main notebook
- `titanic3.csv` - Dataset
- `HELLO.DS-README.md` - Detailed documentation

**Dependencies:**
```bash
pip install pandas numpy seaborn matplotlib scikit-learn tensorflow
```

**Current Progress:**
- ✅ Data exploration complete
- ✅ Naive Bayes model trained (accuracy: check cell 15)
- 🔄 Neural network in development

---

### 3️⃣ **langchain.ipynb** - LangChain Tutorial
**Purpose:** Learn LangChain framework with OpenAI integration  
**API Required:** OpenAI API Key ($5 credit purchased)

**What You'll Learn:**
- OpenAI ChatGPT integration (gpt-4o-mini)
- LangChain chains and parsers
- Prompt templates
- LangServe (REST API for LLM chains)
- Remote chain execution

**Quick Start:**
```bash
cd jupyter-notebook
# Set API key in cell 5
# Run cells sequentially
```

**Key Concepts:**
- `ChatOpenAI` model wrapper
- `StrOutputParser` for clean output
- `ChatPromptTemplate` for reusable prompts
- Chain composition with `|` operator
- `RemoteRunnable` for client-server pattern

**Related Files:**
- `serve.py` - FastAPI server for LangChain
- Start server: `python serve.py`
- Access playground: http://localhost:8000/chain/playground/

**Dependencies:**
```bash
pip install langchain langchain-openai langchain-core langserve fastapi uvicorn
```

---

### 4️⃣ **langchain_gregkamradt_yt.ipynb** - Greg Kamradt Tutorial
**Purpose:** Alternative LangChain tutorial from YouTube  
**Status:** Similar to `langchain.ipynb` but different approach

**When to use:** If you want a different perspective on LangChain

---

### 5️⃣ **speech-to-text-huggingface.ipynb** - Audio ML
**Purpose:** Convert speech to text using Hugging Face Transformers  
**Status:** 🚧 Early stage / Experimental

**What You'll Learn:**
- Hugging Face Transformers library
- Wav2Vec2 model for audio transcription
- PyTorch audio processing

**Dependencies:**
```bash
pip install transformers torchaudio torch
```

**Note:** Incomplete - exploratory project

---

## 🚀 Getting Started (After Long Gap)

### Step 1: Activate Virtual Environment
```bash
cd /Users/vishnuparandhaman/code/python2024
source .venv/bin/activate
```

### Step 2: Update Dependencies (If Needed)
```bash
pip install --upgrade pip
pip install -r requirements.txt  # if exists
```

### Step 3: Choose Your Path

**Path A: Start from Basics** → `jyp-test.ipynb`  
**Path B: Traditional ML** → `HELLO.DS/hello.ipynb`  
**Path C: Modern AI/LLMs** → `langchain.ipynb`  
**Path D: Audio ML** → `speech-to-text-huggingface.ipynb`

---

## 🔑 Python Concepts for Java Developers

| Python | Java Equivalent | Notes |
|--------|----------------|-------|
| `pandas DataFrame` | ResultSet / List<Map> | Like SQL table in memory |
| `list = [1,2,3]` | `ArrayList<>` | Dynamic arrays |
| `dict = {"key":"val"}` | `HashMap<>` | Key-value pairs |
| `lambda x: x*2` | `x -> x*2` | Anonymous functions |
| `with open() as f:` | `try-with-resources` | Auto resource management |
| `for item in list:` | `for(Item i : list)` | For-each loop |
| No semicolons | Semicolons required | Python uses indentation |
| `import pandas as pd` | `import java.util.*` | Import statement |
| `pip install` | Maven dependency | Package management |

---

## 📦 Common Dependencies

**Data Science Stack:**
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

**AI/ML Stack:**
```bash
pip install tensorflow keras torch transformers
```

**LangChain Stack:**
```bash
pip install langchain langchain-openai langserve
```

---

## 🐛 Common Issues & Solutions

### Issue: Module not found
```bash
# Solution: Install missing package
pip install <package-name>
```

### Issue: Kernel won't start
```bash
# Solution: Restart VS Code or reinstall ipykernel
pip install --upgrade ipykernel
```

### Issue: OpenAI API errors
- Check API key is set correctly
- Verify you have credits: https://platform.openai.com/account/billing
- Current credit: $5 (purchased Dec 4, 2025)

### Issue: Can't find CSV files
- Ensure you're in the correct directory
- CSV files must be in same folder as notebook

---

## 📝 Learning Log

**2024-12-04:**
- ✅ Set up LangChain with OpenAI API
- ✅ Purchased $5 OpenAI credits
- ✅ Fixed package compatibility issues
- ✅ Created documentation structure
- 📍 Currently: Understanding Titanic ML project

**Next Session TODO:**
- [ ] Complete Neural Network section in hello.ipynb
- [ ] Compare Naive Bayes vs NN accuracy
- [ ] Explore LangServe deployment
- [ ] Review prompt engineering techniques

---

## 🎯 Learning Path Recommendation

1. **Week 1:** `jyp-test.ipynb` → Python basics
2. **Week 2-3:** `HELLO.DS/hello.ipynb` → Traditional ML
3. **Week 4:** `langchain.ipynb` → Modern LLM applications
4. **Week 5+:** Advanced topics, build your own project

---

## 📚 External Resources

**Python for Java Developers:**
- https://docs.python.org/3/
- Real Python tutorials

**Machine Learning:**
- Scikit-learn documentation
- Kaggle tutorials

**LangChain:**
- https://python.langchain.com/docs/
- Greg Kamradt YouTube channel

**OpenAI API:**
- https://platform.openai.com/docs/

---

## 🔒 Security Notes

- ⚠️ **Never commit API keys to Git**
- Use environment variables or `getpass.getpass()` for sensitive data
- Current OpenAI key is embedded in notebooks - rotate if sharing code

---

## 💾 Project Structure

```
jupyter-notebook/
├── README.md (this file)
├── jyp-test.ipynb
├── langchain.ipynb
├── langchain_gregkamradt_yt.ipynb
├── speech-to-text-huggingface.ipynb
├── serve.py (LangServe FastAPI server)
└── HELLO.DS/
    ├── hello.ipynb
    ├── titanic3.csv
    └── HELLO.DS-README.md
```

---

**Last Review Date:** December 4, 2025  
**Next Review:** March 2026 (or whenever you return!)

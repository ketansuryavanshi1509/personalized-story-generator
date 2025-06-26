
# 🧚 Personalized Children's Story Generator

An NLP-powered application that generates **customized, age-appropriate children's stories** based on user inputs. Built with **Streamlit** and powered by **Hugging Face's `flan-t5-large` model**, this app aims to make storytelling fun, interactive, and personal for kids.

---

## 🚀 Features

- 👶 Accepts child’s name, age, favorite animal, and preferred theme
- 📚 Supports 5 themes: Adventure, Friendship, Fantasy, Mystery, Science
- ✂️ Choose story length: Short, Medium, Long
- 📝 Age-appropriate, imaginative storytelling
- 🔁 Post-processing to remove repetitive sentences
- 📄 Download generated story as PDF or TXT
- 🎨 Simple, interactive Streamlit UI

---

## 🖥️ Demo Screenshot

> *(Add your own screenshot and update the image path)*  
![Screenshot](screenshot.png)

---

## 📦 Installation

### Step 1: Clone the repository
```bash
git clone https://github.com/your-username/personalized-story-generator.git
cd personalized-story-generator
````

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the app

```bash
streamlit run app.py
```

---

## 🧠 How It Works

* Uses Hugging Face’s `google/flan-t5-large` model for story generation.
* Prompts are designed to guide the model to generate stories with a beginning, middle, and happy ending.
* A post-processing function removes repeated sentences to improve readability.
* Stories can be saved as PDF or TXT for easy sharing and reading.

---

## 🔧 Project Structure

```
.
├── app.py                  # Streamlit frontend
├── story_generator.py      # Prompting + generation logic
├── utils.py                # PDF and TXT file generation
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

## 📋 Sample Input

| Field           | Example   |
| --------------- | --------- |
| Name            | Ketan     |
| Age             | 7         |
| Favorite Animal | Dog       |
| Theme           | Adventure |
| Length          | Medium    |

---

## 📝 Sample Output

> Ketan was a 7-year-old who loved adventures. One sunny day, he and his dog Max set out on a magical quest to find a hidden treasure in the nearby forest...
> *(Full story shown inside the app)*

---

## ✅ Future Improvements

* 🔊 Add text-to-speech narration
* 🌍 Multi-language support (e.g., Hindi, Spanish)
* 🎨 AI-generated illustrations
* 🔄 Interactive story continuation feature

---

## 📄 License

MIT License © 2025 — [Your Name](https://github.com/your-username)

---

## 🙏 Acknowledgments

* [Hugging Face Transformers](https://huggingface.co/)
* [Streamlit](https://streamlit.io/)
* [FLAN-T5 Model](https://huggingface.co/google/flan-t5-large)

---

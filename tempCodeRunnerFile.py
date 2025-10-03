from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text, max_sentences=3):
    # Split text into chunks of max 900 words (to fit model input)
    words = text.split()
    chunk_size = 900
    chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summarized_text = summary[0]['summary_text']
        sentences = summarized_text.split('. ')
        summaries.append('. '.join(sentences[:max_sentences]) + ".")
    return '\n'.join(summaries)

if __name__ == "__main__":
    print("Paste your article or blog post (end with Ctrl+Z + Enter):")
    text = ""
    try:
        while True:
            line = input()
            text += line + " "
    except EOFError:
        pass
    if text.strip():
        print("\n--- Summary (3 sentences) ---")
        print(summarize_text(text))
    else:
        print("No input detected.")





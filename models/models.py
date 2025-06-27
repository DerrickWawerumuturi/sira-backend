
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

facebook_model_name = "facebook/blenderbot-400M-distill"
google_model_name = "google/flan-t5-base"
bart_model_name = "facebook/bart-base"


# Load the models and tokenizers
fb_model = AutoModelForSeq2SeqLM.from_pretrained(facebook_model_name)
google_model = AutoModelForSeq2SeqLM.from_pretrained(google_model_name)
bart_model = AutoModelForSeq2SeqLM.from_pretrained(bart_model_name)

# Tokenizers
fb_tokenizer = AutoTokenizer.from_pretrained(facebook_model_name)
google_tokenizer = AutoTokenizer.from_pretrained(google_model_name)
bart_tokenizer = AutoTokenizer.from_pretrained(bart_model_name)

# define chat function


def chat_with_bots(input_text, model_name="google"):
    if model_name == "google":
        inputs = google_tokenizer.encode(input_text, return_tensors='pt')
        outputs = google_model.generate(inputs, max_new_tokens=1000)
        response = google_tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        ).strip()

        return response
    elif model_name == "facebook":
        inputs = fb_tokenizer.encode(input_text, return_tensors='pt')
        outputs = fb_model.generate(inputs, max_new_tokens=1000)
        response = fb_tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        ).strip()
        return response

    elif model_name == "bart":
        inputs = bart_tokenizer.encode(input_text, return_tensors='pt')
        outputs = bart_model.generate(inputs, max_new_tokens=1000)
        response = bart_tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        ).strip()
        return response
    else:
        response = "No model selected"
        return response

# example
# print(chat_with_bots("hi, what your name", model_name="facebook"))

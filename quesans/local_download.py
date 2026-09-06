from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from constants import *
def download_model():
        tokenizer = AutoTokenizer.from_pretrained(TOKENIZER)
        model = AutoModelForQuestionAnswering.from_pretrained(MODEL)

        model.save_pretrained(SAVE_DIR)
        tokenizer.save_pretrained(SAVE_DIR)

if __name__=="__main__":
        download_model()
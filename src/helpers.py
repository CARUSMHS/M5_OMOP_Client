from transformers import MarianMTModel, MarianTokenizer
import requests

def translate_column(df, column_name):
        """
        Littler helper to translate pandas column from german to english using Hlesinki-NLP model
        """
        # model config
        model_name = "Helsinki-NLP/opus-mt-de-en"  # Pre-trained translation model for German to English
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)

        translated_column = []

        for index, value in df[column_name].items():
            try:
                # Tokenize input text
                inputs = tokenizer(value, return_tensors="pt", padding=True, truncation=True, max_length=512)
                # Translate input text
                translated = model.generate(**inputs)
                translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)[0]
            except Exception as e:
                print(f"Error translating '{value}': {e}")
                translated_text = value
            translated_column.append(translated_text)
        df['en_' + column_name] = translated_column
        return df


def extract_keyValues(api_endpoint):

    req = requests.get(api_endpoint).json()

    def extract_values(json_dict):
        result = []
        for key , value in json_dict.items():
            if isinstance(value, dict):
                result += [
                    (f'{key}_{val[0]}', val[1]) for val in extract_values(value)
                    ]
            elif isinstance(value, str):
                result.append((key, value))
            elif isinstance(value, list):
                result += [
                    (f'{key}_{val[0]}', val[1]) for i in range(len(value)) 
                    for val in extract_values(value[i])
                    ]
            else:
                continue 

        return result
    
    return extract_values(req)


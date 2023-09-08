import numpy as np
import torch
from src.seamless_communication.models.inference.translator import Translator, load_unity_model, StringLike

device = torch.device("cpu")

translator = Translator(model_name_or_card="seamlessM4T_large", vocoder_name_or_card="vocoder_36langs", device=device, dtype=torch.float16)
translator.load_model_for_inference(model_name_or_card="seamlessM4T_medium",load_model_fn=load_unity_model, device=device, dtype=torch.float16)

def process_text(
    input_text: str,
    source_language: str,
    target_language: str
) -> StringLike:
    translated_text, wav, sr = translator.predict(
        input=input_text,
        task_str="S2ST",
        tgt_lang=target_language,
        src_lang=source_language,
    )
    return translated_text
    
if __name__ == "__main__":
    #print(process_text("Hello", "en", "fr"))
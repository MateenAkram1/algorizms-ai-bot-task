import gradio as gr
from voice_input import recognize_speech_from_mic
from intent_parser import parse_intent
from response_generator import generate_response
from text_to_speech import speak

def handle_voice_command():
    text = recognize_speech_from_mic(duration=5)
    if not text:
        return "Could not hear anything.", ""
    intent_data = parse_intent(text)
    response = generate_response(intent_data)
    speak(response)  
    return text, response

with gr.Blocks() as demo:
    gr.Markdown("## Uqaab Voice Assistant for Truckers")

    with gr.Row():
        mic_button = gr.Button("🎙️ Press to Speak", variant="primary")
    
    recognized_text = gr.Textbox(label="Recognized Text")
    system_response = gr.Textbox(label="System Response")

    mic_button.click(fn=handle_voice_command, outputs=[recognized_text, system_response])

demo.launch()

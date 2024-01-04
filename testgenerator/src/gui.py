import tkinter as tk
from tkinter import font
from openai import OpenAI
import re

# API anahtarınızı ve prompt metnini girin
api_key = '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'

def create_window():
    window = tk.Tk()
    window.title("Unit Test Generator")
    window.config(background="#6495ed")
    # Pencere boyutunu ve ekranın ortasına yerleştirme ayarları
    window_width = 1400
    window_height = 850
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    

    # İçerik için bir Frame oluştur ve pencerenin ortasına yerleştir
    content_frame = tk.Frame(window)
    content_frame.place(relx=0.5, rely=0.07, anchor='n')
    content_frame.config(background=("#6495ed"))

    # Label widget'ı oluştur
    label = tk.Label(content_frame, text="Aşağıdaki alana program kodlarınızı yazınız!")
    bold_font = font.Font(family="Arial", size=20, weight="bold")
    label.config(background="#6495ed", foreground="#000000", font=bold_font )
    label.grid(row=0, column=0, padx=10, pady=0, sticky="nsew")  # Label widget'ını pencereye yerleştir
    
    # Metin girişi için Text widget'ı
    text_area = tk.Text(content_frame, height=20, width=60)
    text_area.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
    
    # Scrollbar widget'ı oluştur ve yanına yerleştir
    scrollbar = tk.Scrollbar(content_frame, command=text_area.yview)
    scrollbar.grid(row=1, column=1, sticky="nsew")

    # Scrollbar'ı Text widget'ı ile ilişkilendir
    text_area.config(yscrollcommand=scrollbar.set)
    
    # Output Text widget'ı
    output_text_area = tk.Text(content_frame, height=30, width=80)
    output_text_area.grid(row=3, column=0, padx= 0, pady=0, sticky="nsew")
    
    scrollbar = tk.Scrollbar(content_frame, command=output_text_area.yview)
    scrollbar.grid(row=3, column=1, sticky="nsew")

    # Scrollbar'ı Text widget'ı ile ilişkilendir
    output_text_area.config(yscrollcommand=scrollbar.set)
    
    # Kullanıcının girdiği metni alacak fonksiyon
    def get_input():
        user_input = text_area.get("1.0", tk.END)
        
        def send_to_chatgpt(prompt):
            apikey = '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'
            client = OpenAI(api_key=apikey)
    
            completion = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "user", 
                        "content": prompt + "\n Can you write only unit test this code?"
                    }
                ]
            )
            return completion.choices[0].message.content
        
        response_from_gpt = send_to_chatgpt(user_input)
        
        def extract_code_from_response(response_from_chatgpt):
            # Kod bloklarını ``` işaretleri arasında ara
            code_blocks = re.findall('```(.*?)```', response_from_chatgpt, re.DOTALL)
            # Tüm bulunan kod bloklarını birleştir
            code = '\n'.join(code_blocks)
            return code
        
        unit_test = extract_code_from_response(response_from_gpt)
        output_text_area.delete("1.0", tk.END)
        output_text_area.insert("1.0", unit_test)

    # Metni almak için bir buton
    submit_button = tk.Button(content_frame, text="Birim Testini Yazdır", command=get_input)
    submit_button.grid(row=2, column= 0, padx=525, pady=20, sticky="nsew")
    ft = font.Font(family='Arial',size=14)
    submit_button.config(background="#228b22", foreground="#ffffff", font=ft, borderwidth="5px")
    
    # Metni temizlemek için bir fonksiyon
    def clear_text():
        text_area.delete("1.0", tk.END)
    
    # Metni temizlemek için bir buton
    clear_button = tk.Button(content_frame, text="Temizle", command=clear_text)
    clear_button.grid(row=2, column=0, padx=550, pady=20, sticky="nsew")
    clear_button.config(background="#FF0000", foreground="#ffffff", font=ft, borderwidth="5px")
    
    
    return window





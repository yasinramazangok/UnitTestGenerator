import tkinter as tk
from tkinter import PhotoImage, font
from openai import OpenAI
import re

# API KEY
api_key = ''

def create_window():
    window = tk.Tk()
    window.title("Unit Test Generator")
    window.config(background="#c0c0c0")
    window_width = 1400
    window_height = 850
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    ft = font.Font(family='Arial',size=14)
    
    # Frame
    content_frame = tk.Frame(window)
    content_frame.place(relx=0.5, rely=0.07, anchor='n')
    content_frame.config(background="#c0c0c0")

    # Label Widget
    label = tk.Label(content_frame, text="Aşağıdaki alana program kodlarınızı yazınız!")
    bold_font = font.Font(family="Arial", size=20, weight="bold")
    label.config(background="#c0c0c0", foreground="#000000", font=bold_font )
    label.grid(row=0, column=0, padx=10, pady=0, sticky="nsew")  
    
    # Text Widget for input
    text_area = tk.Text(content_frame, height=20, width=60)
    text_area.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")
    
    # Scrollbar Widget
    scrollbar = tk.Scrollbar(content_frame, command=text_area.yview)
    scrollbar.grid(row=1, column=1, sticky="nsew")

    text_area.config(yscrollcommand=scrollbar.set)
    
    # Output Text Widget
    output_text_area = tk.Text(content_frame, height=30, width=80)
    output_text_area.grid(row=3, column=0, padx= 0, pady=0, sticky="nsew")
    
    scrollbar = tk.Scrollbar(content_frame, command=output_text_area.yview)
    scrollbar.grid(row=3, column=1, sticky="nsew")
    
    # Buton Hover Effect
    def on_enter(e):
        submit_button.config(background="#14A44D")
    def on_enter1(e):
        submit_button1.config(background="#1e0bd0")
    def on_enter2(e):
        submit_button2.config(background="#E4A11B")
        
    def on_leave(e):
        submit_button.config(background="#54B4D3")
    
    def on_leave1(e):
        submit_button1.config(background="#54B4D3")
    
    def on_leave2(e):
        submit_button2.config(background="#54B4D3")

    output_text_area.config(yscrollcommand=scrollbar.set)
    
    # Function for unit test
    def get_input_for_unit_test():
        user_input = text_area.get("1.0", tk.END)
       
        def send_to_chatgpt_for_unit_test(prompt):
            apikey = ''
            client = OpenAI(api_key=apikey)
    
            completion = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "user", 
                        "content": prompt + "\n Can you write only unit test for this code?"
                    }
                ]
            )
            return completion.choices[0].message.content
        
        response_from_gpt = send_to_chatgpt_for_unit_test(user_input)
        
        def extract_code_from_response(response_from_chatgpt):
           
            code_blocks = re.findall('```(.*?)```', response_from_chatgpt, re.DOTALL)

            code = '\n'.join(code_blocks)
            return code
            
        unit_test1 = extract_code_from_response(response_from_gpt)
        output_text_area.delete("1.0", tk.END)
        output_text_area.insert("1.0", unit_test1)
    
    # Function for dom tree
    def get_input_for_dom_tree():
        user_input = text_area.get("1.0", tk.END)
        
        # DOM Tree 
        def send_to_chatgpt_for_dom_tree(prompt):
            apikey = ''
            client = OpenAI(api_key=apikey)
    
            completion = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "user", 
                        "content": prompt + "\n Can you write dom tree for this code?"
                    }
                ]
            )
            return completion.choices[0].message.content
        
        response_from_gpt1 = send_to_chatgpt_for_dom_tree(user_input)
        
        def extract_code_from_response1(response_from_chatgpt):
            
            code_blocks1 = re.findall('```(.*?)```', response_from_chatgpt, re.DOTALL)

            code1 = '\n'.join(code_blocks1)
            return code1
            
        dom_tree1 = extract_code_from_response1(response_from_gpt1)
        output_text_area.delete("1.0", tk.END)
        output_text_area.insert("1.0", dom_tree1)  
    
    # Function for test scenario
    def get_input_for_test_scenario():
        user_input = text_area.get("1.0", tk.END)
        
        # Test Scenario 
        def send_to_chatgpt_for_test_scenario(prompt):
            apikey = ''
            client = OpenAI(api_key=apikey)
    
            completion = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "user", 
                        "content": prompt + "\n Can you write 3 different test scenarios for this code like Senaryo 1: ... Senaryo 2: ... Senaryo 3: ... in Turkish?"
                    }
                ]
            )
            return completion.choices[0].message.content
        
        response_from_gpt2 = send_to_chatgpt_for_test_scenario(user_input)
        
        def extract_code_from_response2(response_from_chatgpt):

            scenario_pattern = r"(Senaryo \d+: .+?)(?=\nSenaryo \d+: |\Z)"
            code_blocks1 = re.findall(scenario_pattern, response_from_chatgpt, re.DOTALL)

            code1 = '\n'.join(code_blocks1)
            return code1
            
        test_scenario = extract_code_from_response2(response_from_gpt2)
        output_text_area.delete("1.0", tk.END)
        output_text_area.insert("1.0", test_scenario) 
    
    # Button frame
    button_frame = tk.Frame(content_frame, background="#c0c0c0")
    button_frame.grid(row=2, column=0, pady=20, sticky="nsew")

    # Unit Test button
    submit_button = tk.Button(button_frame, text="Birim Testini Yazdır", command=get_input_for_unit_test)
    submit_button.grid(row=0, column=0, padx=5, pady=20, sticky="ew")
    submit_button.config(background="#54B4D3", foreground="#ffffff", font=ft, borderwidth="5px")
    
    # Test Scenario button
    submit_button1 = tk.Button(button_frame, text="Test Senaryoları", command=get_input_for_test_scenario)
    submit_button1.grid(row=0, column=1, padx=5, pady=20, sticky="ew")
    submit_button1.config(background="#54B4D3", foreground="#ffffff", font=ft, borderwidth="5px")
    
    # DOM Tree button
    submit_button2 = tk.Button(button_frame, text="Ağaç Yapısı", command=get_input_for_dom_tree)
    submit_button2.grid(row=0, column=2, padx=5, pady=20, sticky="ew")
    submit_button2.config(background="#54B4D3", foreground="#ffffff", font=ft, borderwidth="5px")
    
    # Function for clean text
    def clear_text():
        text_area.delete("1.0", tk.END)
        output_text_area.delete("1.0", tk.END)
        text_area.focus()  
     
    # Button for clean text
    clear_button = tk.Button(button_frame, text="Temizle", command=clear_text)
    clear_button.grid(row=0, column=3, padx=5, pady=20, sticky="ew")
    clear_button.config(background="#FF0000", foreground="#ffffff", font=ft, borderwidth="5px")

    # Buton hover and click
    submit_button.bind("<Enter>", on_enter)
    submit_button.bind("<Leave>", on_leave)
    
    # Buton hover and click
    submit_button1.bind("<Enter>", on_enter1)
    submit_button1.bind("<Leave>", on_leave1)
    
    # Buton hover and click 
    submit_button2.bind("<Enter>", on_enter2)
    submit_button2.bind("<Leave>", on_leave2)
    
    return window





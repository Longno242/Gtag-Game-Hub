import tkinter as tk
import webbrowser

class GameLauncherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gtag Menu Temps")
        self.root.geometry("400x300")

        self.games = {
            "Synx Temp Fix": "https://cdn.discordapp.com/attachments/1153290729565737020/1160400246921240576/Synx_Temp_Remasterd_Better_By_kfjfjfj.rar?ex=653485f2&is=652210f2&hm=01527deb225af0f4a4285f078693a344dd3f1aee8fcfac29b0eb96f263d37286&",
            "Oxai Temp": "https://cdn.discordapp.com/attachments/1153290729565737020/1159175333434638376/Oxai_Temp.zip?ex=65394ba7&is=6526d6a7&hm=687a7bb39c573af3b25ae7241a0adc5c360a62ff63d21d2ca3cc140e7a74f123&",
            "OutSpect Temp": "https://cdn.discordapp.com/attachments/1153290729565737020/1154191422048702564/MenuTemp-V1.zip?ex=65399f06&is=65272a06&hm=d44e149c575e32725863273fcf9614535a85ce6af609108fd37bedd9d90f1e64&",
            "KMan Temp": "https://cdn.discordapp.com/attachments/1153290729565737020/1153437910855602248/Template.zip?ex=6536e143&is=65246c43&hm=0eef5520378ccc9cec599e311695bedfba5d2b670441e7751dea35f3fbe9c11f&",
            "Soon": "",
            "Soon": "",
            "Menu TuT": "https://youtu.be/6uOY6SmTyEk?si=grkgu6oeNClDNv6s",
        }

        self.create_gui()

    def create_gui(self):
        self.title_bar = tk.Frame(self.root, bg="blue")
        self.title_bar.pack(fill="x")

        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas = tk.Canvas(self.root, yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar.config(command=self.canvas.yview)

        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.populate_game_buttons()

        self.canvas.bind("<Configure>", self.on_canvas_configure)

        self.hover_menu = None
        self.hover_button = tk.Button(self.title_bar, text="≡", bg="gray", fg="white", command=self.show_hover_menu)
        self.hover_button.pack(side="left")

    def populate_game_buttons(self):
        for game_name, game_url in self.games.items():
            game_button = tk.Button(self.frame, text=game_name, command=lambda url=game_url: self.open_game_link(url))
            game_button.pack(pady=5)
            game_button.configure(
                background="#5D30AF",  # Hexadecimal color with transparency
                borderwidth=1,
                cursor="hand2",  # Use "hand2" for a hand cursor
                font=("Arial", 14, "bold"),
                border=1,
                relief="solid",
                width=30,
                height=2,
            )
            game_button.bind("<Enter>", self.on_button_hover)
            game_button.bind("<Leave>", self.on_button_leave)

    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def open_game_link(self, url):
        try:
            webbrowser.open(url)
        except Exception as e:
            print(f"Error opening URL: {e}")

    def on_button_hover(self, event):
        event.widget.configure(
            background="#4A1F94",  # Color change on hover
            relief="raised",
            border=2,
            font=("Arial", 15, "bold"),
        )

    def on_button_leave(self, event):
        event.widget.configure(
            background="#5D30AF",  # Hexadecimal color with transparency
            relief="solid",
            border=1,
            font=("Arial", 14, "bold"),
        )

    def show_hover_menu(self):
        # Add code to show a hover menu
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = GameLauncherApp(root)
    root.mainloop()
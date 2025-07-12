import tkinter as tk
import time
import os
import webbrowser
import random

# === Ruby App Window (prozori unutar OS-a) ===
class RubyAppWindow(tk.Frame):
    def __init__(self, master, title, content_callback, close_callback):
        super().__init__(master, bg="#2a2a2a", bd=2, relief="raised")
        self.title = title
        self.close_callback = close_callback

        self.titlebar = tk.Frame(self, bg="#444", height=30)
        self.titlebar.pack(fill="x", side="top")

        self.title_label = tk.Label(self.titlebar, text=title, bg="#444", fg="white")
        self.title_label.pack(side="left", padx=5)

        close_btn = tk.Button(self.titlebar, text="✕", bg="#444", fg="white", bd=0, command=self.close)
        close_btn.pack(side="right", padx=5)

        self.content = tk.Frame(self, bg="#1e1e1e")
        self.content.pack(expand=True, fill="both")

        content_callback(self.content)

        self.titlebar.bind("<B1-Motion>", self.drag)
        self.titlebar.bind("<Button-1>", self.click)

    def click(self, event):
        self._drag_start_x = event.x
        self._drag_start_y = event.y

    def drag(self, event):
        x = self.winfo_x() + event.x - self._drag_start_x
        y = self.winfo_y() + event.y - self._drag_start_y
        self.place(x=x, y=y)

    def close(self):
        self.close_callback(self.title)
        self.destroy()

# === Ruby OS ===
class RubyOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Ruby OS")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)

        self.app_windows = {}

        self.create_desktop()
        self.create_taskbar()
        self.update_clock()

    def create_desktop(self):
        self.desktop = tk.Frame(self.root, bg="#1e1e1e")
        self.desktop.pack(expand=True, fill="both")

        tk.Button(self.desktop, text="Notepad", width=12, height=2, command=self.open_notepad).place(x=40, y=40)
        tk.Button(self.desktop, text="File Manager", width=12, height=2, command=self.open_file_manager).place(x=40, y=120)
        tk.Button(self.desktop, text="Terminal", width=12, height=2, command=self.open_terminal).place(x=40, y=200)
        tk.Button(self.desktop, text="Web Browser", width=12, height=2, command=self.open_browser).place(x=40, y=280)
        tk.Button(self.desktop, text="Paint", width=12, height=2, command=self.open_paint).place(x=40, y=360)
        tk.Button(self.desktop, text="Game Manager", width=12, height=2, command=self.open_game_manager).place(x=40, y=440)
        tk.Button(self.desktop, text="Task Manager", width=12, height=2, command=self.open_task_manager).place(x=40, y=520)

    def create_taskbar(self):
        self.taskbar = tk.Frame(self.root, bg="#333", height=30)
        self.taskbar.pack(side="bottom", fill="x")

        self.start_btn = tk.Button(self.taskbar, text="Start", bg="#444", fg="white", width=8,
                                   command=self.toggle_start_menu)
        self.start_btn.pack(side="left", padx=5)

        self.open_apps_frame = tk.Frame(self.taskbar, bg="#333")
        self.open_apps_frame.pack(side="left", padx=5)

        self.clock_label = tk.Label(self.taskbar, fg="white", bg="#333")
        self.clock_label.pack(side="right", padx=10)

        self.start_menu = tk.Frame(self.root, bg="#222", bd=2, relief="ridge")
        shutdown_btn = tk.Button(self.start_menu, text="Shutdown", bg="#550000", fg="white", width=20,
                                  command=self.shutdown)
        shutdown_btn.pack(padx=10, pady=10)

        self.start_menu_visible = False

    def toggle_start_menu(self):
        if self.start_menu_visible:
            self.start_menu.place_forget()
            self.start_menu_visible = False
        else:
            self.start_menu.place(x=5, y=self.root.winfo_height() - 130)
            self.start_menu_visible = True

    def shutdown(self):
        self.root.destroy()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.clock_label.config(text=now)
        self.root.after(1000, self.update_clock)

    def add_app_to_taskbar(self, app_name):
        btn = tk.Button(self.open_apps_frame, text=app_name, bg="#555", fg="white", height=1,
                        command=lambda: self.focus_app(app_name))
        btn.pack(side="left", padx=2)
        return btn

    def remove_app_from_taskbar(self, app_name):
        if app_name in self.app_windows:
            btn = self.app_windows[app_name]['taskbar_btn']
            btn.destroy()
            del self.app_windows[app_name]

    def open_app(self, name, content_callback):
        if name in self.app_windows:
            self.focus_app(name)
            return

        app_win = RubyAppWindow(self.desktop, name, content_callback, self.remove_app_from_taskbar)
        app_win.place(x=200, y=100, width=600, height=400)

        taskbar_btn = self.add_app_to_taskbar(name)
        self.app_windows[name] = {'window': app_win, 'taskbar_btn': taskbar_btn}

    def focus_app(self, name):
        app = self.app_windows.get(name)
        if app:
            app['window'].lift()

    # Notepad
    def open_notepad(self):
        def content(frame):
            text_area = tk.Text(frame, bg="black", fg="white", insertbackground="white")
            text_area.pack(expand=True, fill="both")
        self.open_app("Notepad", content)

    # File Manager
    def open_file_manager(self):
        def content(frame):
            files = os.listdir(".")
            text = "\n".join(files)
            lbl = tk.Label(frame, text=text, fg="white", bg="#1e1e1e", justify="left", anchor="nw")
            lbl.pack(expand=True, fill="both", padx=10, pady=10)
        self.open_app("File Manager", content)

    # Terminal
    def open_terminal(self):
        def content(frame):
            output = tk.Text(frame, bg="black", fg="lime", height=15)
            output.pack(expand=True, fill="both")

            input_field = tk.Entry(frame, bg="#111", fg="white")
            input_field.pack(fill="x")

            cwd = [os.getcwd()]

            def execute_cmd(event=None):
                cmd_line = input_field.get()
                input_field.delete(0, tk.END)
                output.insert(tk.END, f">>> {cmd_line}\n")

                if not cmd_line.strip():
                    return

                parts = cmd_line.strip().split()
                cmd = parts[0]
                args = parts[1:]

                try:
                    if cmd == "ls":
                        path = args[0] if args else cwd[0]
                        if not os.path.isabs(path):
                            path = os.path.join(cwd[0], path)
                        if os.path.isdir(path):
                            files = os.listdir(path)
                            output.insert(tk.END, "\n".join(files) + "\n")
                        else:
                            output.insert(tk.END, f"ls: cannot access '{path}': No such directory\n")

                    elif cmd == "cd":
                        if not args:
                            cwd[0] = os.path.expanduser("~")
                        else:
                            new_path = args[0]
                            if not os.path.isabs(new_path):
                                new_path = os.path.join(cwd[0], new_path)
                            if os.path.isdir(new_path):
                                cwd[0] = os.path.normpath(new_path)
                            else:
                                output.insert(tk.END, f"cd: no such directory: {args[0]}\n")

                    elif cmd == "pwd":
                        output.insert(tk.END, cwd[0] + "\n")

                    elif cmd == "clear":
                        output.delete("1.0", tk.END)

                    elif cmd == "echo":
                        output.insert(tk.END, " ".join(args) + "\n")

                    elif cmd == "rm":
                        if not args:
                            output.insert(tk.END, "rm: missing operand\n")
                        else:
                            target = args[0]
                            if not os.path.isabs(target):
                                target = os.path.join(cwd[0], target)
                            if os.path.isfile(target):
                                try:
                                    os.remove(target)
                                    output.insert(tk.END, f"Removed file: {target}\n")
                                except Exception as e:
                                    output.insert(tk.END, f"rm: cannot remove '{target}': {e}\n")
                            else:
                                output.insert(tk.END, f"rm: cannot remove '{target}': No such file\n")

                    else:
                        output.insert(tk.END, f"Unknown command: {cmd_line}\n")

                except Exception as e:
                    output.insert(tk.END, f"Error: {e}\n")

                output.see(tk.END)

            input_field.bind("<Return>", execute_cmd)

        self.open_app("Terminal", content)

    # Browser
    def open_browser(self):
        webbrowser.open("https://www.google.com")

    # Paint sa Clear dugmetom
    def open_paint(self):
        def content(frame):
            canvas = tk.Canvas(frame, bg="white")
            canvas.pack(expand=True, fill="both")

            last_x, last_y = None, None

            def on_button_press(event):
                nonlocal last_x, last_y
                last_x, last_y = event.x, event.y

            def on_move(event):
                nonlocal last_x, last_y
                if last_x is not None and last_y is not None:
                    canvas.create_line(last_x, last_y, event.x, event.y, fill="black", width=3, capstyle=tk.ROUND, smooth=True)
                last_x, last_y = event.x, event.y

            def on_button_release(event):
                nonlocal last_x, last_y
                last_x, last_y = None, None

            canvas.bind("<ButtonPress-1>", on_button_press)
            canvas.bind("<B1-Motion>", on_move)
            canvas.bind("<ButtonRelease-1>", on_button_release)

            clear_btn = tk.Button(frame, text="Clear", command=lambda: canvas.delete("all"))
            clear_btn.pack(side="bottom", pady=5)

        self.open_app("Paint", content)

    # Snake
    def open_snake(self):
        def content(frame):
            frame.focus_set()
            width, height = 600, 400
            cell_size = 20

            canvas = tk.Canvas(frame, width=width, height=height, bg="black")
            canvas.pack()

            direction = 'Right'
            snake = [(5, 10), (4, 10), (3, 10)]
            food = (10, 10)
            game_over = [False]

            def draw():
                canvas.delete("all")
                for x, y in snake:
                    x1, y1 = x * cell_size, y * cell_size
                    x2, y2 = x1 + cell_size, y1 + cell_size
                    canvas.create_rectangle(x1, y1, x2, y2, fill="green")
                fx1, fy1 = food[0] * cell_size, food[1] * cell_size
                fx2, fy2 = fx1 + cell_size, fy1 + cell_size
                canvas.create_oval(fx1, fy1, fx2, fy2, fill="red")

            def move_snake():
                if game_over[0]:
                    canvas.create_text(width//2, height//2, text="Game Over", fill="white", font=("Arial", 24))
                    return

                nonlocal snake, food, direction
                head_x, head_y = snake[0]
                if direction == 'Up':
                    head_y -= 1
                elif direction == 'Down':
                    head_y += 1
                elif direction == 'Left':
                    head_x -= 1
                elif direction == 'Right':
                    head_x += 1

                new_head = (head_x, head_y)

                if (head_x < 0 or head_x >= width // cell_size or
                    head_y < 0 or head_y >= height // cell_size or
                    new_head in snake):
                    game_over[0] = True
                    move_snake()
                    return

                snake.insert(0, new_head)

                if new_head == food:
                    while True:
                        new_food = (random.randint(0, (width // cell_size) - 1),
                                    random.randint(0, (height // cell_size) - 1))
                        if new_food not in snake:
                            food = new_food
                            break
                else:
                    snake.pop()

                draw()
                frame.after(150, move_snake)

            def change_direction(event):
                nonlocal direction
                opposites = {'Up':'Down', 'Down':'Up', 'Left':'Right', 'Right':'Left'}
                if event.keysym in ['Up', 'Down', 'Left', 'Right']:
                    if opposites[event.keysym] != direction:
                        direction = event.keysym

            frame.bind("<Key>", change_direction)

            draw()
            move_snake()

        self.open_app("Snake", content)

    # Pong
    def open_pong(self):
        def content(frame):
            frame.focus_set()
            width, height = 600, 400
            canvas = tk.Canvas(frame, width=width, height=height, bg="black")
            canvas.pack()

            paddle_width = 10
            paddle_height = 80
            ball_size = 15

            paddle1_y = height // 2 - paddle_height // 2
            paddle2_y = height // 2 - paddle_height // 2
            ball_x = width // 2
            ball_y = height // 2
            ball_dx = 5
            ball_dy = 3

            score1 = 0
            score2 = 0

            def draw():
                canvas.delete("all")
                # Paddles
                canvas.create_rectangle(10, paddle1_y, 10 + paddle_width, paddle1_y + paddle_height, fill="white")
                canvas.create_rectangle(width - 10 - paddle_width, paddle2_y, width - 10, paddle2_y + paddle_height, fill="white")
                # Ball
                canvas.create_oval(ball_x - ball_size//2, ball_y - ball_size//2,
                                   ball_x + ball_size//2, ball_y + ball_size//2, fill="white")
                # Scores
                canvas.create_text(width//4, 20, text=str(score1), fill="white", font=("Arial", 20))
                canvas.create_text(3*width//4, 20, text=str(score2), fill="white", font=("Arial", 20))

            def move():
                nonlocal paddle1_y, paddle2_y, ball_x, ball_y, ball_dx, ball_dy, score1, score2

                ball_x += ball_dx
                ball_y += ball_dy

                # Ball collision with top/bottom
                if ball_y - ball_size//2 <= 0 or ball_y + ball_size//2 >= height:
                    ball_dy = -ball_dy

                # Ball collision with paddles
                if (ball_x - ball_size//2 <= 20 and paddle1_y <= ball_y <= paddle1_y + paddle_height):
                    ball_dx = -ball_dx
                elif (ball_x + ball_size//2 >= width - 20 and paddle2_y <= ball_y <= paddle2_y + paddle_height):
                    ball_dx = -ball_dx

                # Ball out of bounds left/right
                if ball_x < 0:
                    score2 += 1
                    reset_ball()
                elif ball_x > width:
                    score1 += 1
                    reset_ball()

                # AI paddle movement (right paddle)
                if paddle2_y + paddle_height//2 < ball_y:
                    paddle2_y += 4
                elif paddle2_y + paddle_height//2 > ball_y:
                    paddle2_y -= 4
                paddle2_y = max(0, min(height - paddle_height, paddle2_y))

                draw()
                frame.after(30, move)

            def reset_ball():
                nonlocal ball_x, ball_y, ball_dx, ball_dy
                ball_x = width // 2
                ball_y = height // 2
                ball_dx = random.choice([-5,5])
                ball_dy = random.choice([-3,3])

            def on_key(event):
                nonlocal paddle1_y
                if event.keysym == "Up":
                    paddle1_y = max(0, paddle1_y - 20)
                elif event.keysym == "Down":
                    paddle1_y = min(height - paddle_height, paddle1_y + 20)

            frame.bind("<Key>", on_key)

            reset_ball()
            move()

        self.open_app("Pong", content)

    # Tic Tac Toe
    def open_tictactoe(self):
        def content(frame):
            current_player = ['X']
            board = [['' for _ in range(3)] for _ in range(3)]
            buttons = []

            def check_winner():
                lines = []

                # Rows
                lines.extend(board)
                # Columns
                lines.extend([[board[r][c] for r in range(3)] for c in range(3)])
                # Diagonals
                lines.append([board[i][i] for i in range(3)])
                lines.append([board[i][2 - i] for i in range(3)])

                for line in lines:
                    if line == ['X', 'X', 'X']:
                        return 'X'
                    elif line == ['O', 'O', 'O']:
                        return 'O'
                return None

            def on_click(r, c):
                if board[r][c] == '':
                    board[r][c] = current_player[0]
                    buttons[r][c].config(text=current_player[0])
                    winner = check_winner()
                    if winner:
                        status_label.config(text=f"Player {winner} wins!")
                        disable_all_buttons()
                    else:
                        current_player[0] = 'O' if current_player[0] == 'X' else 'X'
                        status_label.config(text=f"Player {current_player[0]}'s turn")

            def disable_all_buttons():
                for row in buttons:
                    for btn in row:
                        btn.config(state="disabled")

            for r in range(3):
                row = []
                for c in range(3):
                    b = tk.Button(frame, text="", width=6, height=3, font=("Arial", 20),
                                  command=lambda r=r, c=c: on_click(r, c))
                    b.grid(row=r, column=c)
                    row.append(b)
                buttons.append(row)

            status_label = tk.Label(frame, text="Player X's turn", fg="white", bg="#1e1e1e", font=("Arial", 14))
            status_label.grid(row=3, column=0, columnspan=3, pady=10)

        self.open_app("Tic Tac Toe", content)

    # Game Manager sa svim igrama
    def open_game_manager(self):
        def content(frame):
            tk.Button(frame, text="Snake", width=20, height=2, command=self.open_snake).pack(pady=5)
            tk.Button(frame, text="Pong", width=20, height=2, command=self.open_pong).pack(pady=5)
            tk.Button(frame, text="Tic Tac Toe", width=20, height=2, command=self.open_tictactoe).pack(pady=5)
        self.open_app("Game Manager", content)

    # Task Manager sa End Task dugmetom
    def open_task_manager(self):
        def content(frame):
            app_listbox = tk.Listbox(frame, bg="#1e1e1e", fg="white")
            app_listbox.pack(expand=True, fill="both", padx=10, pady=10)

            for app_name in self.app_windows:
                app_listbox.insert(tk.END, app_name)

            def end_task():
                selected = app_listbox.curselection()
                if selected:
                    app_name = app_listbox.get(selected[0])
                    if app_name in self.app_windows:
                        self.app_windows[app_name]['window'].destroy()
                        self.remove_app_from_taskbar(app_name)
                        app_listbox.delete(selected[0])

            end_btn = tk.Button(frame, text="End Task", bg="#aa2222", fg="white", command=end_task)
            end_btn.pack(pady=5)

        self.open_app("Task Manager", content)

# === Pokretanje RubyOS ===
def main():
    root = tk.Tk()
    root.state('zoomed')  # Maksimizira glavni prozor (na Windows)
    os_system = RubyOS(root)
    root.mainloop()

if __name__ == "__main__":
    main()

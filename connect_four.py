#!/usr/bin/env python3
"""
Modern Connect Four Game - Clean Version
A beautiful, modern Connect Four game with AI opponent and engaging features.
"""

import tkinter as tk
from tkinter import messagebox
from connect_four_game import ConnectFourGame

class ConnectFourGUI:
    """Modern Connect Four GUI with clean, professional design."""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Connect Four - Modern Edition")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Game instance
        self.game = ConnectFourGame()
        
        # Modern color scheme
        self.colors = {
            'bg': '#f0f0f0',
            'header': '#6366f1',
            'panel': '#ffffff',
            'board_bg': '#1e293b',
            'slot': '#334155',
            'red': '#ef4444',
            'yellow': '#f59e0b',
            'text': '#1e293b',
            'white': '#ffffff'
        }
        
        self.cell_size = 60
        self.padding = 20
        
        self.create_widgets()
        self.game.start_game()
        self.draw_board()
        self.update_status()
    
    def create_widgets(self):
        """Create all GUI widgets."""
        # Header
        header_frame = tk.Frame(self.root, bg=self.colors['header'], height=80)
        header_frame.pack(fill='x', pady=(0, 20))
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text="🎮 Connect Four - Modern Edition", 
                              font=('Arial', 20, 'bold'),
                              bg=self.colors['header'], fg='white')
        title_label.pack(expand=True)
        
        # Main content
        main_frame = tk.Frame(self.root, bg=self.colors['bg'])
        main_frame.pack(fill='both', expand=True, padx=20)
        
        # Left panel - Players
        self.create_left_panel(main_frame)
        
        # Center panel - Game board
        self.create_center_panel(main_frame)
        
        # Right panel - Controls
        self.create_right_panel(main_frame)
        
        # Status bar
        self.create_status_bar()
    
    def create_left_panel(self, parent):
        """Create the left panel with player information."""
        left_frame = tk.Frame(parent, bg=self.colors['panel'], width=200)
        left_frame.pack(side='left', fill='y', padx=(0, 10))
        left_frame.pack_propagate(False)
        
        # Player info
        tk.Label(left_frame, text="Players", font=('Arial', 14, 'bold'),
                bg=self.colors['panel'], fg=self.colors['text']).pack(pady=10)
        
        # Player 1
        p1_frame = tk.Frame(left_frame, bg=self.colors['panel'])
        p1_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(p1_frame, text="🔴 Player 1", font=('Arial', 12),
                bg=self.colors['panel'], fg=self.colors['text']).pack(side='left')
        self.p1_score = tk.Label(p1_frame, text="0", font=('Arial', 12, 'bold'),
                                bg=self.colors['panel'], fg=self.colors['text'])
        self.p1_score.pack(side='right')
        
        # Player 2
        p2_frame = tk.Frame(left_frame, bg=self.colors['panel'])
        p2_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(p2_frame, text="🟡 AI Player", font=('Arial', 12),
                bg=self.colors['panel'], fg=self.colors['text']).pack(side='left')
        self.p2_score = tk.Label(p2_frame, text="0", font=('Arial', 12, 'bold'),
                                bg=self.colors['panel'], fg=self.colors['text'])
        self.p2_score.pack(side='right')
        
        # Current player indicator
        self.current_label = tk.Label(left_frame, text="Player 1's Turn",
                                    font=('Arial', 12, 'bold'),
                                    bg=self.colors['panel'], fg=self.colors['text'])
        self.current_label.pack(pady=10)
    
    def create_center_panel(self, parent):
        """Create the center panel with the game board."""
        center_frame = tk.Frame(parent, bg=self.colors['panel'])
        center_frame.pack(side='left', fill='both', expand=True)
        
        # Board title
        tk.Label(center_frame, text="Game Board", font=('Arial', 16, 'bold'),
                bg=self.colors['panel'], fg=self.colors['text']).pack(pady=10)
        
        # Game board canvas
        canvas_size = self.game.COLS * self.cell_size + 2 * self.padding
        self.canvas = tk.Canvas(center_frame, width=canvas_size, height=canvas_size,
                               bg=self.colors['board_bg'])
        self.canvas.pack(pady=10)
        
        # Column indicators
        indicators_frame = tk.Frame(center_frame, bg=self.colors['panel'])
        indicators_frame.pack(pady=5)
        
        for col in range(self.game.COLS):
            label = tk.Label(indicators_frame, text=str(col + 1),
                           font=('Arial', 10, 'bold'),
                           bg=self.colors['header'], fg='white',
                           width=3)
            label.pack(side='left', padx=2)
        
        # Bind click events
        self.canvas.bind('<Button-1>', self.on_click)
    
    def create_right_panel(self, parent):
        """Create the right panel with game controls."""
        right_frame = tk.Frame(parent, bg=self.colors['panel'], width=200)
        right_frame.pack(side='right', fill='y', padx=(10, 0))
        right_frame.pack_propagate(False)
        
        tk.Label(right_frame, text="Controls", font=('Arial', 14, 'bold'),
                bg=self.colors['panel'], fg=self.colors['text']).pack(pady=10)
        
        # Control buttons
        self.start_btn = tk.Button(right_frame, text="🎮 Start Game",
                                  command=self.start_game,
                                  bg=self.colors['header'], fg='white',
                                  font=('Arial', 10, 'bold'), width=15)
        self.start_btn.pack(pady=5)
        
        self.reset_btn = tk.Button(right_frame, text="🔄 Reset",
                                  command=self.reset_game,
                                  bg='#10b981', fg='white',
                                  font=('Arial', 10, 'bold'), width=15)
        self.reset_btn.pack(pady=5)
        
        self.undo_btn = tk.Button(right_frame, text="↶ Undo",
                                 command=self.undo_move,
                                 bg='#f59e0b', fg='white',
                                 font=('Arial', 10, 'bold'), width=15,
                                 state='disabled')
        self.undo_btn.pack(pady=5)
        
        # Game mode selection
        tk.Label(right_frame, text="Game Mode", font=('Arial', 12, 'bold'),
                bg=self.colors['panel'], fg=self.colors['text']).pack(pady=(20, 5))
        
        self.mode_var = tk.StringVar(value='pve')
        
        tk.Radiobutton(right_frame, text="Player vs AI",
                      variable=self.mode_var, value='pve',
                      bg=self.colors['panel'], fg=self.colors['text'],
                      font=('Arial', 10)).pack(anchor='w', padx=10)
        
        tk.Radiobutton(right_frame, text="Player vs Player",
                      variable=self.mode_var, value='pvp',
                      bg=self.colors['panel'], fg=self.colors['text'],
                      font=('Arial', 10)).pack(anchor='w', padx=10)
    
    def create_status_bar(self):
        """Create the status bar at the bottom."""
        self.status_label = tk.Label(self.root, text="Ready to play!",
                                   font=('Arial', 10),
                                   bg=self.colors['header'], fg='white')
        self.status_label.pack(fill='x', pady=(20, 0))
    
    def draw_board(self):
        """Draw the game board on the canvas."""
        self.canvas.delete("all")
        
        for row in range(self.game.ROWS):
            for col in range(self.game.COLS):
                x1 = self.padding + col * self.cell_size
                y1 = self.padding + row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                
                # Draw slot
                self.canvas.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5,
                                      fill=self.colors['slot'], outline='white')
                
                # Draw piece if present
                if self.game.board[row][col] != 0:
                    color = (self.colors['red'] if self.game.board[row][col] == 1 
                            else self.colors['yellow'])
                    self.canvas.create_oval(x1 + 8, y1 + 8, x2 - 8, y2 - 8,
                                          fill=color, outline='white')
    
    def on_click(self, event):
        """Handle canvas click events."""
        if self.game.game_state != 'playing':
            return
        
        col = (event.x - self.padding) // self.cell_size
        if 0 <= col < self.game.COLS:
            self.make_move(col)
    
    def make_move(self, col):
        """Make a move in the specified column."""
        if self.game.drop_piece(col):
            self.draw_board()
            self.update_status()
            
            if self.game.game_state == 'finished':
                self.show_game_over()
            elif (self.game.game_state == 'playing' and 
                  self.game.current_player == 2 and 
                  self.mode_var.get() == 'pve'):
                # AI move
                self.root.after(500, self.make_ai_move)
    
    def make_ai_move(self):
        """Make an AI move."""
        if self.game.game_state == 'playing' and self.game.current_player == 2:
            col = self.game.get_ai_move()
            if col != -1:
                self.make_move(col)
    
    def start_game(self):
        """Start a new game."""
        self.game.start_game()
        self.update_status()
        self.status_label.config(text="Game started!")
    
    def reset_game(self):
        """Reset the current game."""
        self.game.reset_game()
        self.game.start_game()
        self.draw_board()
        self.update_status()
        self.status_label.config(text="Game reset!")
    
    def undo_move(self):
        """Undo the last move."""
        if self.game.undo_move():
            self.draw_board()
            self.update_status()
            self.status_label.config(text="Move undone!")
    
    def update_status(self):
        """Update the game status display."""
        if self.game.game_state == 'playing':
            if self.game.current_player == 1:
                self.current_label.config(text="🔴 Player 1's Turn")
            else:
                self.current_label.config(text="🟡 AI Player's Turn")
        elif self.game.game_state == 'finished':
            if self.game.winner == 1:
                self.current_label.config(text="🎉 Player 1 Wins!")
            elif self.game.winner == 2:
                self.current_label.config(text="🤖 AI Player Wins!")
            else:
                self.current_label.config(text="🤝 It's a Draw!")
        
        # Update scores
        self.p1_score.config(text=str(self.game.stats['player1_wins']))
        self.p2_score.config(text=str(self.game.stats['player2_wins']))
        
        # Update button states
        if self.game.game_state == 'playing':
            self.start_btn.config(state='disabled')
            self.reset_btn.config(state='normal')
            self.undo_btn.config(state='normal' if self.game.move_history else 'disabled')
        else:
            self.start_btn.config(state='normal')
            self.reset_btn.config(state='normal')
            self.undo_btn.config(state='disabled')
    
    def show_game_over(self):
        """Show the game over dialog."""
        if self.game.winner == 0:
            message = "It's a draw!"
        elif self.game.winner == 1:
            message = "Player 1 wins!"
        else:
            message = "AI Player wins!"
        
        messagebox.showinfo("Game Over", message)
    
    def run(self):
        """Start the GUI main loop."""
        self.root.mainloop()

if __name__ == "__main__":
    print("🎮 Starting Modern Connect Four Game...")
    app = ConnectFourGUI()
    app.run()

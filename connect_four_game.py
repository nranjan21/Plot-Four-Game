#!/usr/bin/env python3
"""
Modern Connect Four Game - 2025 Edition
A beautiful, engaging Connect Four game with modern UI design, AI opponent, and advanced features.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import json
import os
from typing import List, Tuple, Optional, Dict, Any
import threading
import math

class ConnectFourGame:
    """Modern Connect Four game engine with optimized algorithms."""
    
    def __init__(self):
        self.ROWS = 6
        self.COLS = 7
        self.board = [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.current_player = 1
        self.game_state = 'waiting'  # waiting, playing, paused, finished
        self.winner = None
        self.move_history = []
        self.game_start_time = None
        self.game_end_time = None
        self.move_count = 0
        
        # Settings
        self.settings = {
            'game_mode': 'pve',  # pvp, pve
            'ai_difficulty': 'medium',  # easy, medium, hard
            'sound_enabled': True,
            'animations_enabled': True,
            'theme': 'dark'  # light, dark
        }
        
        # Statistics
        self.stats = {
            'games_played': 0,
            'player1_wins': 0,
            'player2_wins': 0,
            'best_time': None,
            'total_moves': 0,
            'win_streak': 0,
            'longest_streak': 0
        }
        
        self.load_settings()
        self.load_stats()
    
    def reset_game(self) -> None:
        """Reset the game to initial state."""
        self.board = [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.current_player = 1
        self.game_state = 'waiting'
        self.winner = None
        self.move_history = []
        self.game_start_time = None
        self.game_end_time = None
        self.move_count = 0
    
    def start_game(self) -> None:
        """Start a new game."""
        self.reset_game()
        self.game_state = 'playing'
        self.game_start_time = time.time()
    
    def drop_piece(self, col: int) -> bool:
        """Drop a piece in the specified column."""
        if self.game_state != 'playing':
            return False
        
        if col < 0 or col >= self.COLS:
            return False
        
        # Find the lowest available row
        for row in range(self.ROWS - 1, -1, -1):
            if self.board[row][col] == 0:
                self.board[row][col] = self.current_player
                self.move_history.append({
                    'row': row, 'col': col, 'player': self.current_player,
                    'timestamp': time.time()
                })
                self.move_count += 1
                
                # Check for win
                if self.check_win(row, col, self.current_player):
                    self.game_state = 'finished'
                    self.winner = self.current_player
                    self.game_end_time = time.time()
                    self.update_stats()
                    return True
                
                # Check for draw
                if self.is_board_full():
                    self.game_state = 'finished'
                    self.winner = 0  # Draw
                    self.game_end_time = time.time()
                    return True
                
                self.switch_player()
                return True
        
        return False  # Column is full
    
    def check_win(self, row: int, col: int, player: int) -> bool:
        """Check if the current move results in a win."""
        directions = [
            (0, 1),   # horizontal
            (1, 0),   # vertical
            (1, 1),   # diagonal \
            (1, -1)   # diagonal /
        ]
        
        for dr, dc in directions:
            count = 1  # Count the current piece
            
            # Check in positive direction
            for i in range(1, 4):
                new_row, new_col = row + dr * i, col + dc * i
                if (0 <= new_row < self.ROWS and 0 <= new_col < self.COLS and 
                    self.board[new_row][new_col] == player):
                    count += 1
                else:
                    break
            
            # Check in negative direction
            for i in range(1, 4):
                new_row, new_col = row - dr * i, col - dc * i
                if (0 <= new_row < self.ROWS and 0 <= new_col < self.COLS and 
                    self.board[new_row][new_col] == player):
                    count += 1
                else:
                    break
            
            if count >= 4:
                return True
        
        return False
    
    def is_board_full(self) -> bool:
        """Check if the board is full."""
        return all(self.board[0][col] != 0 for col in range(self.COLS))
    
    def switch_player(self) -> None:
        """Switch to the other player."""
        self.current_player = 2 if self.current_player == 1 else 1
    
    def undo_move(self) -> bool:
        """Undo the last move."""
        if not self.move_history or self.game_state != 'playing':
            return False
        
        last_move = self.move_history.pop()
        self.board[last_move['row']][last_move['col']] = 0
        self.move_count -= 1
        self.switch_player()
        return True
    
    def get_ai_move(self) -> int:
        """Get AI move based on difficulty setting."""
        if self.game_state != 'playing' or self.current_player != 2:
            return -1
        
        difficulty = self.settings['ai_difficulty']
        
        if difficulty == 'easy':
            return self._get_random_move()
        elif difficulty == 'medium':
            return self._get_medium_ai_move()
        else:  # hard
            return self._get_hard_ai_move()
    
    def _get_random_move(self) -> int:
        """Get a random valid move."""
        available_moves = [col for col in range(self.COLS) if self.board[0][col] == 0]
        return random.choice(available_moves) if available_moves else -1
    
    def _get_medium_ai_move(self) -> int:
        """Get a medium difficulty AI move."""
        # Check for immediate win
        for col in range(self.COLS):
            if self.board[0][col] == 0:
                row = self._get_lowest_row(col)
                self.board[row][col] = 2
                if self.check_win(row, col, 2):
                    self.board[row][col] = 0
                    return col
                self.board[row][col] = 0
        
        # Check for immediate loss (block player)
        for col in range(self.COLS):
            if self.board[0][col] == 0:
                row = self._get_lowest_row(col)
                self.board[row][col] = 1
                if self.check_win(row, col, 1):
                    self.board[row][col] = 0
                    return col
                self.board[row][col] = 0
        
        # Prefer center columns
        center_cols = [3, 2, 4, 1, 5, 0, 6]
        for col in center_cols:
            if self.board[0][col] == 0:
                return col
        
        return self._get_random_move()
    
    def _get_hard_ai_move(self) -> int:
        """Get a hard difficulty AI move using minimax."""
        best_move = self._minimax(4, -float('inf'), float('inf'), True)
        return best_move['column']
    
    def _minimax(self, depth: int, alpha: float, beta: float, maximizing: bool) -> Dict[str, Any]:
        """Minimax algorithm with alpha-beta pruning."""
        if depth == 0:
            return {'score': self._evaluate_board(), 'column': -1}
        
        available_moves = self._get_available_moves()
        if not available_moves:
            return {'score': 0, 'column': -1}
        
        # Check for immediate win/loss
        for col in available_moves:
            row = self._get_lowest_row(col)
            self.board[row][col] = 2 if maximizing else 1
            
            if self.check_win(row, col, 2 if maximizing else 1):
                self.board[row][col] = 0
                return {
                    'score': 1000000 if maximizing else -1000000,
                    'column': col
                }
            self.board[row][col] = 0
        
        if maximizing:
            max_eval = -float('inf')
            best_column = available_moves[0]
            
            for col in available_moves:
                row = self._get_lowest_row(col)
                self.board[row][col] = 2
                eval_result = self._minimax(depth - 1, alpha, beta, False)
                self.board[row][col] = 0
                
                if eval_result['score'] > max_eval:
                    max_eval = eval_result['score']
                    best_column = col
                
                alpha = max(alpha, eval_result['score'])
                if beta <= alpha:
                    break
            
            return {'score': max_eval, 'column': best_column}
        else:
            min_eval = float('inf')
            best_column = available_moves[0]
            
            for col in available_moves:
                row = self._get_lowest_row(col)
                self.board[row][col] = 1
                eval_result = self._minimax(depth - 1, alpha, beta, True)
                self.board[row][col] = 0
                
                if eval_result['score'] < min_eval:
                    min_eval = eval_result['score']
                    best_column = col
                
                beta = min(beta, eval_result['score'])
                if beta <= alpha:
                    break
            
            return {'score': min_eval, 'column': best_column}
    
    def _evaluate_board(self) -> int:
        """Evaluate the current board state."""
        score = 0
        
        # Evaluate all possible 4-piece sequences
        for row in range(self.ROWS):
            for col in range(self.COLS):
                score += self._evaluate_position(row, col)
        
        return score
    
    def _evaluate_position(self, row: int, col: int) -> int:
        """Evaluate a specific position on the board."""
        score = 0
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        
        for dr, dc in directions:
            sequence = []
            for i in range(4):
                new_row, new_col = row + dr * i, col + dc * i
                if 0 <= new_row < self.ROWS and 0 <= new_col < self.COLS:
                    sequence.append(self.board[new_row][new_col])
                else:
                    sequence.append(-1)  # Invalid position
            
            score += self._evaluate_sequence(sequence)
        
        return score
    
    def _evaluate_sequence(self, sequence: List[int]) -> int:
        """Evaluate a sequence of 4 positions."""
        ai_count = sequence.count(2)
        player_count = sequence.count(1)
        empty_count = sequence.count(0)
        
        if ai_count == 4:
            return 1000000
        if ai_count == 3 and empty_count == 1:
            return 1000
        if ai_count == 2 and empty_count == 2:
            return 100
        if ai_count == 1 and empty_count == 3:
            return 10
        
        if player_count == 4:
            return -1000000
        if player_count == 3 and empty_count == 1:
            return -1000
        if player_count == 2 and empty_count == 2:
            return -100
        if player_count == 1 and empty_count == 3:
            return -10
        
        return 0
    
    def _get_available_moves(self) -> List[int]:
        """Get list of available moves."""
        return [col for col in range(self.COLS) if self.board[0][col] == 0]
    
    def _get_lowest_row(self, col: int) -> int:
        """Get the lowest available row in a column."""
        for row in range(self.ROWS - 1, -1, -1):
            if self.board[row][col] == 0:
                return row
        return -1
    
    def get_game_time(self) -> float:
        """Get current game time in seconds."""
        if not self.game_start_time:
            return 0
        end_time = self.game_end_time or time.time()
        return end_time - self.game_start_time
    
    def format_time(self, seconds: float) -> str:
        """Format time as MM:SS."""
        minutes = int(seconds // 60)
        secs = int(seconds % 60)
        return f"{minutes:02d}:{secs:02d}"
    
    def update_stats(self) -> None:
        """Update game statistics."""
        self.stats['games_played'] += 1
        self.stats['total_moves'] += self.move_count
        
        if self.winner == 1:
            self.stats['player1_wins'] += 1
            self.stats['win_streak'] += 1
            self.stats['longest_streak'] = max(self.stats['longest_streak'], self.stats['win_streak'])
        elif self.winner == 2:
            self.stats['player2_wins'] += 1
            self.stats['win_streak'] = 0
        
        game_time = self.get_game_time()
        if not self.stats['best_time'] or game_time < self.stats['best_time']:
            self.stats['best_time'] = game_time
        
        self.save_stats()
    
    def load_settings(self) -> None:
        """Load settings from file."""
        try:
            if os.path.exists('settings.json'):
                with open('settings.json', 'r') as f:
                    saved_settings = json.load(f)
                    self.settings.update(saved_settings)
        except Exception:
            pass
    
    def save_settings(self) -> None:
        """Save settings to file."""
        try:
            with open('settings.json', 'w') as f:
                json.dump(self.settings, f, indent=2)
        except Exception:
            pass
    
    def load_stats(self) -> None:
        """Load statistics from file."""
        try:
            if os.path.exists('stats.json'):
                with open('stats.json', 'r') as f:
                    saved_stats = json.load(f)
                    self.stats.update(saved_stats)
        except Exception:
            pass
    
    def save_stats(self) -> None:
        """Save statistics to file."""
        try:
            with open('stats.json', 'w') as f:
                json.dump(self.stats, f, indent=2)
        except Exception:
            pass


if __name__ == "__main__":
    # This will be imported by the GUI
    pass

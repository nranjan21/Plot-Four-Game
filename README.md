# 🎮 Modern Connect Four Game

A beautiful, modern Connect Four game with AI opponent and engaging features.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Ready%20to%20Play-brightgreen.svg)

## ✨ Features

### 🎨 Modern UI Design
- **Clean Interface**: Professional, modern design
- **Color-Coded Elements**: Intuitive visual feedback
- **Responsive Layout**: Three-panel design
- **Real-Time Updates**: Live game status and scores

### 🤖 Advanced AI Opponent
- **3 Difficulty Levels**: Easy, Medium, Hard
- **Smart Strategy**: Blocks threats and seeks wins
- **Minimax Algorithm**: Optimal play on hard difficulty
- **Adaptive AI**: Adjusts strategy based on difficulty

### 🎯 Game Features
- **Player vs AI**: Challenge the computer
- **Player vs Player**: Local multiplayer
- **Undo Move**: Take back your last move
- **Score Tracking**: Win counters and statistics
- **Game Modes**: Switch between PvP and PvE

## 🚀 Quick Start

### Run the Game
```bash
python connect_four.py
```

### Requirements
- **Python 3.8+** (uses only standard library)
- **tkinter** (included with Python)
- **No additional dependencies required!**

## 🎮 How to Play

1. **Start the Game**: Click "🎮 Start Game"
2. **Make Moves**: Click on any column to drop your piece
3. **Win Condition**: Get 4 pieces in a row (horizontal, vertical, or diagonal)
4. **Controls**:
   - 🎮 Start Game - Begin a new game
   - 🔄 Reset - Reset the current game
   - ↶ Undo - Undo your last move
   - Game Mode - Switch between Player vs AI and Player vs Player

## 🎯 Game Modes

### Player vs AI (PvE)
- Play against computer opponent
- 3 difficulty levels:
  - **Easy**: Random moves with basic strategy
  - **Medium**: Blocks threats, seeks wins
  - **Hard**: Minimax algorithm, optimal play

### Player vs Player (PvP)
- Two human players take turns
- Perfect for local multiplayer
- Equal playing field

## 🎨 UI Features

- **Purple Header**: Modern gradient header design
- **Three-Panel Layout**: Players, Game Board, Controls
- **Color-Coded Buttons**: 
  - Blue: Start Game
  - Green: Reset
  - Orange: Undo
- **Real-Time Status**: Current player and game state
- **Score Tracking**: Win counters for both players

## 🔧 Technical Details

### Architecture
- **Game Engine**: `connect_four_game.py` - Core game logic
- **GUI Interface**: `connect_four.py` - Modern UI
- **Clean Code**: Well-structured, maintainable code

### Algorithms
- **Win Detection**: Optimized 4-directional checking
- **AI Strategy**: Minimax with alpha-beta pruning
- **Board Evaluation**: Position scoring system
- **Move Generation**: Efficient valid move detection

### Performance
- **Time Complexity**: O(1) for moves, O(n) for win detection
- **Space Complexity**: O(rows × cols) for board storage
- **AI Depth**: Configurable search depth (default: 4)

## 📁 Project Structure

```
PlotFour/
├── connect_four.py          # 🎮 Main GUI application
├── connect_four_game.py     # 🧠 Game engine and AI
├── requirements.txt         # 📋 Dependencies (none required!)
├── README.md               # 📖 This documentation
├── .gitignore              # 🚫 Git ignore file
├── plot_four.cpp           # 📜 Original C++ version
└── LICENSE                 # 📄 MIT License
```

## 🎉 Features Summary

 **Modern UI** with clean, professional design  
 **AI Opponent** with 3 difficulty levels  
 **Game Modes** (PvP and PvE)  
 **Undo Functionality**  
 **Score Tracking**  
 **Real-Time Updates**  
 **Color-Coded Interface**  
 **Responsive Design**  
 **No External Dependencies**  

## 🐛 Troubleshooting

### Common Issues

**Game won't start?**
- Ensure Python 3.8+ is installed
- Check that tkinter is available: `python -c "import tkinter"`
- Verify all files are in the same directory

**AI too easy/hard?**
- The AI difficulty is set in the game engine
- Easy: Random moves
- Medium: Basic strategy
- Hard: Optimal play

**Performance issues?**
- The game uses minimal resources (<50MB RAM)
- Close other applications if needed

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Enhanced graphics and animations
- Online multiplayer support
- Tournament mode
- Custom board sizes
- Advanced AI algorithms
- Mobile app version

## 📄 License

MIT License - Feel free to use, modify, and distribute!

## 🎉 Credits

- **Game Design**: Classic Connect Four rules
- **Modern UI**: Clean, professional design
- **AI Algorithm**: Minimax with alpha-beta pruning
- **Python Implementation**: Optimized for performance and readability

## 🤖 Glimpse
<img width="1918" height="997" alt="image" src="https://github.com/user-attachments/assets/fdef7f07-73fb-4e68-b30d-d87db4b94303" />


---

**Enjoy playing Modern Connect Four! 🎮✨**

*Built with ❤️ using Python and modern UI design principles*

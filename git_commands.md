# Git Commands to Push Connect Four Game to Main

## Step 1: Check Status
```bash
git status
```

## Step 2: Add All Files
```bash
git add .
```

## Step 3: Commit Changes
```bash
git commit -m "🎮 Add Modern Connect Four Game

✨ Features:
- Modern UI with clean, professional design
- AI opponent with 3 difficulty levels (Easy, Medium, Hard)
- Player vs Player and Player vs AI modes
- Undo move functionality
- Score tracking and statistics
- Color-coded interface with purple header
- Real-time game status updates

🔧 Technical:
- Optimized game engine with minimax AI algorithm
- Clean Python implementation using only standard library
- No external dependencies required
- Well-structured, maintainable code

🎯 Game Features:
- Classic Connect Four gameplay
- Smart AI that blocks threats and seeks wins
- Modern three-panel UI layout
- Responsive design and intuitive controls"
```

## Step 4: Push to Main
```bash
git push origin main
```

## Alternative: Use the Batch File
```bash
push_to_main.bat
```

## Files Being Committed:
- `connect_four.py` - Main game application
- `connect_four_game.py` - Game engine and AI
- `requirements.txt` - Dependencies (none required!)
- `README.md` - Updated documentation
- `push_to_main.bat` - Git push script
- `git_commands.md` - This file

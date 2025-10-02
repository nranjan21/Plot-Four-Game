@echo off
echo 🚀 Pushing Connect Four Game to Main Branch
echo ==========================================

echo.
echo 📋 Checking git status...
git status

echo.
echo 📦 Adding all files...
git add .

echo.
echo 💾 Committing changes...
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

echo.
echo 🚀 Pushing to main branch...
git push origin main

echo.
echo ✅ Done! Modern Connect Four Game pushed to main branch.
pause

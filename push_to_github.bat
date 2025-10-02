@echo off
echo 🚀 Setting up Git and Pushing Modern Connect Four to GitHub
echo ==========================================================

echo.
echo 📋 Current directory: %CD%
echo.

echo 🔗 Setting up git remote...
git remote -v
git remote add origin https://github.com/nranjan21/Plot-Four-Game.git
git remote -v

echo.
echo 🌿 Creating and switching to main branch...
git checkout -b main

echo.
echo 📦 Adding all files...
git add .

echo.
echo 📊 Checking git status...
git status

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
- Responsive design and intuitive controls

📁 Files Added:
- connect_four.py: Main GUI application
- connect_four_game.py: Game engine and AI
- requirements.txt: Dependencies (none required!)
- README.md: Updated documentation
- .gitignore: Git ignore file for Python projects
- push_to_main.bat: Git push script
- git_commands.md: Manual git commands
- LICENSE: MIT License

🎉 This modernizes the original C++ implementation with:
- Beautiful GUI instead of terminal
- AI opponent instead of human-only
- Modern design and user experience
- Enhanced features and functionality"

echo.
echo 🚀 Pushing to main branch on GitHub...
git push -u origin main

echo.
echo ✅ Success! Modern Connect Four Game pushed to GitHub!
echo 🌐 Repository: https://github.com/nranjan21/Plot-Four-Game
echo.
echo 🎮 To run the game: python connect_four.py
echo.
pause

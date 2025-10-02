# 🚀 Manual Git Commands to Push to GitHub

## Repository: https://github.com/nranjan21/Plot-Four-Game.git

### Step-by-Step Instructions:

## 1. Initialize Git Repository (if not already done)
```bash
git init
```

## 2. Add Remote Repository
```bash
git remote add origin https://github.com/nranjan21/Plot-Four-Game.git
```

## 3. Check Remote (verify it's set correctly)
```bash
git remote -v
```

## 4. Create Main Branch
```bash
git checkout -b main
```

## 5. Add All Files
```bash
git add .
```

## 6. Check Status (verify files are staged)
```bash
git status
```

## 7. Commit Changes
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
- Responsive design and intuitive controls

📁 Files Added:
- connect_four.py: Main GUI application
- connect_four_game.py: Game engine and AI
- requirements.txt: Dependencies (none required!)
- README.md: Updated documentation
- .gitignore: Git ignore file for Python projects
- LICENSE: MIT License
- plot_four.cpp: Original C++ version (preserved)

🎉 This modernizes the original C++ implementation with:
- Beautiful GUI instead of terminal
- AI opponent instead of human-only
- Modern design and user experience
- Enhanced features and functionality"
```

## 8. Push to GitHub
```bash
git push -u origin main
```

## Alternative: If you get authentication errors, try:
```bash
git push -u origin main --force
```

## 🎯 What This Will Do:

1. **Connect** your local repository to GitHub
2. **Create** a main branch (modern Git standard)
3. **Add** all the modern Python files
4. **Commit** with a comprehensive message
5. **Push** to GitHub, making it the main branch

## 📁 Files Being Pushed:

- ✅ `connect_four.py` - Modern GUI game
- ✅ `connect_four_game.py` - Game engine with AI
- ✅ `README.md` - Professional documentation
- ✅ `requirements.txt` - Dependencies (none!)
- ✅ `.gitignore` - Git ignore file
- ✅ `LICENSE` - MIT License
- ✅ `plot_four.cpp` - Original C++ version (preserved)

## 🚨 Troubleshooting:

### If you get "repository not found" error:
- Make sure you have access to the repository
- Check the repository URL is correct
- Ensure you're logged into GitHub

### If you get authentication errors:
- Use GitHub CLI: `gh auth login`
- Or use personal access token
- Or use SSH keys

### If you get "branch already exists" error:
```bash
git push -u origin main --force
```

## 🎉 Expected Result:

After successful push, your GitHub repository will have:
- **Modern Python Connect Four Game** as the main content
- **Original C++ version** preserved
- **Professional documentation**
- **Clean project structure**

## 🌐 Repository URL:
https://github.com/nranjan21/Plot-Four-Game

Run these commands in your terminal/command prompt to push the code!

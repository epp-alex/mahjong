# Mahjong — Cross-Platform Ultimate Edition

A modern, highly polished, and cross-platform Mahjong Solitaire/Pairs game built with Python
and Pygame. It features fluid particle physics, lightning victory effects, dynamic grid scaling, a
localized AppData persistence system, and a flexible layout system that adapts to any monitor resolution.

This repository provides **ready-to-run, standalone executable binaries** for Windows,
macOS, and Linux. No Python installation or setup is required.

---

## 🌟 Key Features

*   **Massive Image Variety:** Ships with a database of **220 images** that are completely
randomly selected and mixed at the start of each level, making every single playthrough unique.
*   **16 Native Languages:** Full localized support for **16 different languages** using a robust Unicode system font fallback system (guaranteeing zero rendering issues or broken glyphs on Windows, Mac, or Linux).
*   **4 Distinct Difficulties:**
    *   **Easy:** 8 Pairs (4×4 Grid)
    *   **Medium:** 16 Pairs (4×8 Grid)
    *   **Hard:** 25 Pairs (5×10 Grid)
    *   **EXPERT:** 40 Pairs (8×10 Grid)
*   **1 & 2 Player Modes:** 
    *   *Single Player:* Traditional time-attack and click-efficiency mode.
    *   *2-Player Couch Co-Op:* An active turn-based duel mode with dynamic colored HUD tracking and customizable score points.
*   **Immersive Sound Design:** Adaptive volume scaling with background tracks and feedback sound effects.

---

## 🛠 Supported Languages

The game interface can be toggled instantly between the following 16 languages:
*   German (*Deutsch*), English, French (*Français*), Spanish (*Español*), Italian (*Italiano*), Portuguese (*Português*), Dutch (*Nederlands*), Polish (*Polski*), Russian (*Русский*), Ukrainian (*Українська*), Turkish (*Türkçe*), Hungarian (*Magyar*), Czech (*Čeština*), Swedish (*Svenska*), Romanian (*Română*), and Greek (*Ελληνικά*).

---

## 🚀 How to Download and Run (Pre-Built Binaries)

Go to the **Releases** section on GitHub and download the appropriate package for your operating system.

### 🪟 Windows
1. Download and extract the Windows ZIP archive.
2. Open the folder and double-click `mahjong.exe` to play.

### 🍏 macOS
1. Download the macOS `.dmg` file.
2. Double-click the `.dmg` file to mount it, then drag the `Mahjong` application into your **Applications** folder.
3. Launch the game from your Applications folder or Launchpad.
*(Note: Depending on your system security settings, you may need to right-click the app and select "Open" the first time to bypass the macOS Gatekeeper warning).*

### 🐧 Linux
1. Download and extract the Linux archive.
2. Mark the binary as executable (`chmod +x mahjong`) and run it via terminal or desktop environment.

---

## 🎮 How to Play

1. Run the game (it automatically starts in a borderless/native full-screen container matched to your display architecture).
2. Choose your **Game Mode** (1 Player or 2 Players) and **Difficulty Level** in the main menu.
3. Use your **Mouse Left-Click** to turn over the tiles and match identical pairs.
4. **Volume Control:** Press `+` / `-` on your keyboard during gameplay to adjust sound levels on the fly.
5. Press `ESC` to go back to the menu or exit, and `SPACEBAR` to restart from the victory screen.

---

## 📁 Repository Structure

The portable applications are self-contained. For transparency, the build architecture includes:

```text
├── mahjong.exe / .dmg / binary  # Ready-to-run game file
├── mahjong_config.json          # Configuration definitions (JSON standard)
├── 001.wav                      # Match sound effect
├── 002.wav                      # Victory background music track
└── bild/                        # Directory containing the 220 PNG tile images

📝 License


This project is open-source and free to distribute.

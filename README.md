\---

# Game RPA - Forge of Empires Automation

## 📋 Project Overview

This project is a **custom Robotic Process Automation (RPA)** solution demonstrating how RPA techniques can be applied to automate gameplay in browser-based games. It specifically targets the game "Forge of Empires" to automate repetitive tasks such as collecting resources, managing production, and handling in-game notifications.

**Purpose**: This project showcases that RPA techniques, traditionally used for business process automation, can be applied to virtually any application with a visual interface - even games.

## 🎯 Motivation

This project was developed to demonstrate that:
- RPA can interact with any visual interface, not just business applications
- Similar techniques were historically used for mainframe applications and legacy systems that lacked APIs
- Computer vision and browser automation can work together to create sophisticated automation workflows
- Screen scraping and image recognition remain viable automation approaches when APIs are unavailable

## 🛠 Technologies Used

- **Python 3.x** - Core programming language
- **Selenium WebDriver** - Browser automation and control
- **OpenCV (cv2)** - Computer vision and template matching
- **NumPy** - Image processing and array operations
- **PyAutoGUI** - Mouse and keyboard automation
- **Pillow (PIL)** - Image manipulation
- **Python Logging** - Activity logging and debugging

## 🏗 Architecture

The project consists of four main components:

### 1. **Vision Module** (`vision.py`)
- Implements computer vision using OpenCV template matching
- Finds UI elements (buttons, icons, indicators) in screenshots
- Supports both single and multiple object detection
- Uses `cv.TM_CCOEFF_NORMED` method for matching
- Configurable confidence thresholds for detection

### 2. **Browser Module** (`browser.py`)
- Manages Chrome browser using Selenium WebDriver
- Handles site navigation and login automation
- Captures full-page screenshots for vision processing
- Manages browser window state (fullscreen, dimensions)

### 3. **Bot Module** (`bot.py`, `bot2.py`)
- Orchestrates the automation workflow
- Translates detected image positions to screen coordinates
- Executes mouse movements and clicks using PyAutoGUI
- Implements game-specific logic and decision making
- Manages state tracking (e.g., clicked buttons, completed tasks)

### 4. **Main Entry Point** (`main.py`, `main2.py`)
- Initializes logging
- Creates bot instance
- Starts the automation loop

## 🔄 How It Works

```
┌─────────────────────────────────────────────────────────┐
│ 1. Browser Module opens game in Chrome                 │
│    - Logs in automatically                              │
│    - Sets fullscreen mode                               │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│ 2. Main Loop captures screenshot                        │
│    - Takes full browser screenshot                      │
│    - Converts to OpenCV-compatible format               │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│ 3. Vision Module analyzes screenshot                    │
│    - Searches for predefined UI elements (templates)    │
│    - Returns coordinates of matches                     │
│    - Applies confidence threshold                       │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│ 4. Bot Module executes actions                          │
│    - Calculates click positions                         │
│    - Moves mouse to target                              │
│    - Performs clicks                                    │
│    - Waits for UI responses                             │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
                  [Repeat]
```

### Key Automation Features:
- **Resource Collection**: Automatically collects coins, tools, and production outputs
- **Quest Management**: Detects and completes quest rewards
- **Production Management**: Starts new production cycles
- **Training Units**: Automatically trains military units
- **Event Handling**: Manages pop-ups and dialog boxes
- **Window Management**: Closes unnecessary windows

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- Chrome browser installed
- ChromeDriver matching your Chrome version

### Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd game_rpa
```

2. **Install dependencies**
```bash
pip install opencv-python numpy selenium pillow pyautogui
```

3. **Download ChromeDriver**
   - Download from: https://chromedriver.chromium.org/
   - Place `chromedriver.exe` in the project root directory

4. **Configure browser profile**
   - Edit `browser.py` line 46
   - Update the Chrome user data directory path:
   ```python
   optionsList.add_argument(r"--user-data-dir=C:\Users\<YOUR_USER>\AppData\Local\Google\Chrome\User Data\Default")
   ```

5. **Update credentials**
   - Edit `bot2.py` line 158
   - Add your game credentials:
   ```python
   browser = Browser('https://en14.forgeofempires.com/game/index', 
                     windowW, windowH, 
                     'Game', 
                     '<YOUR_USERNAME>', 
                     '<YOUR_PASSWORD>', 
                     '<WORLD_NAME>')
   ```

## 🚀 Usage

Run the automation:
```bash
python main2.py
```

### Controls
- **H key**: Stop the bot and close all windows
- **P key**: Pause the bot
- **O key**: Resume the bot

### Logging
- All activities are logged to `foe.log`
- Debug images saved to `results/` directory
- Timestamped log entries for troubleshooting

## ✅ Benefits

### 1. **Automation Without APIs**
- Works with applications that don't provide APIs or automation interfaces
- Interacts through the visual layer, just like a human user

### 2. **Cross-Application Technique**
- Same approach can be adapted for:
  - Legacy mainframe applications (green screen terminals)
  - Desktop applications without automation support
  - Web applications with limited scripting access
  - Virtual desktop environments

### 3. **Rapid Prototyping**
- Quick to develop compared to reverse engineering game protocols
- No need to understand internal game mechanics
- Visual debugging through screenshot analysis

### 4. **Educational Value**
- Demonstrates practical computer vision applications
- Shows browser automation techniques
- Illustrates state machine design patterns
- Example of event-driven automation

### 5. **Historical Context**
- Represents techniques used for decades in enterprise automation
- Screen scraping was the primary automation method before APIs
- Still relevant for legacy system integration

## ⚠️ Limitations and Issues

### 1. **Resolution Dependency** ⚠️
**Critical Limitation**: Template images must match the game's display resolution exactly.

- **Problem**: If the game runs at 1920x1080, template images must be captured at that resolution
- **Impact**: Changing screen resolution or zoom level breaks detection
- **Workaround**: Create multiple template sets for different resolutions
- **Better Solution**: Use scale-invariant feature detection (SIFT, SURF) instead of template matching

### 2. **UI Changes Break Automation** ⚠️
**High Risk**: Any UI update renders the automation non-functional.

- **Problem**: Positions and visuals are hardcoded
- **Impact**: 
  - Game updates change button positions
  - New UI designs require recapturing all templates
  - Seasonal themes may affect image matching
- **Maintenance**: Requires constant template updates
- **Mitigation**: Use OCR for text detection, multiple template variants

### 3. **Performance Issues** ⚠️
- **Screenshot overhead**: Taking full screenshots is CPU intensive
- **Template matching speed**: Searching multiple templates on large images is slow
- **Mouse movement delays**: PyAutoGUI has artificial delays (2-5 seconds per action)
- **Impact**: Actions take much longer than human players

### 4. **Reliability Problems** ⚠️
- **False Positives**: Similar UI elements can be misidentified
- **False Negatives**: Lighting changes, animations, or transparency can break detection
- **Timing Issues**: 
  - Network lag may cause UI delays
  - Hardcoded sleep times may be too short or too long
  - Race conditions when UI updates

### 5. **Limited Adaptability** ⚠️
- **Static Logic**: Cannot adapt to unexpected game states
- **Error Recovery**: Poor handling of unusual scenarios
- **No Learning**: Doesn't improve from experience

### 6. **Configuration Complexity** ⚠️
**Setup Barrier**: Requires significant configuration effort.

- Chrome profile paths
- Game credentials
- Template image creation
- Coordinate calibration
- Confidence threshold tuning

### 7. **Ethical and Legal Concerns** ⚠️
- **Terms of Service**: May violate game's ToS
- **Fair Play**: Gives unfair advantage over human players
- **Account Risk**: Could result in account bans
- **Legal Status**: Automation may be prohibited

### 8. **Platform Specific** ⚠️
- **Windows Dependency**: PyAutoGUI behavior varies across OS
- **Browser Dependency**: Only works with Chrome
- **Game Server**: Hardcoded for specific server (en14.forgeofempires.com)

### 9. **Maintenance Overhead** ⚠️
- Constant template image updates needed
- Confidence thresholds require tuning
- Game logic changes require code updates
- No automated testing possible

### 10. **Security Concerns** ⚠️
- Credentials stored in plain text
- Browser profile access required
- No encryption of sensitive data

## 🏛 Historical Context - Legacy System Automation

This project demonstrates techniques that were essential for automating legacy systems:

### Mainframe Screen Scraping
In the 1980s-2000s, many businesses relied on mainframe applications that:
- Had no APIs or automation interfaces
- Only provided "green screen" terminal access
- Required human operators to read screens and type commands

**Solution**: Screen scraping tools that would:
1. Capture terminal screens
2. Parse text positions
3. Identify fields and values
4. Automate data entry
5. Extract information for reporting

### Why These Techniques Remain Relevant

1. **Legacy System Integration**
   - Many organizations still run 30-40 year old systems
   - Replacing them is expensive and risky
   - Screen scraping bridges old and new systems

2. **Closed Applications**
   - Some vendors don't provide APIs
   - Third-party automation is the only option

3. **Rapid Prototyping**
   - Faster than waiting for official API development
   - Good for proof-of-concept work

4. **Last Resort Automation**
   - When all else fails, visual automation works
   - Better than manual processes

## 📸 Template Images

The `images/` directory contains template images for detection:
- **Coins**: Various coin indicators (`coin.png` - `coin6.png`)
- **Buttons**: Collect, close, OK, train buttons
- **Status**: Sleep indicators, completed goods, full buildings
- **Events**: Event notification templates

### Creating New Templates
1. Take screenshot of game at target resolution
2. Crop the exact UI element you want to detect
3. Save as PNG with transparent background if possible
4. Test with various confidence thresholds (0.5-0.9)

## 🔧 Configuration

### Adjust Detection Sensitivity

```python
# In bot.py - modify confidence thresholds
coins = vision_coin.findMultiple(screenshot, 0.7, ...)  # 70% confidence
sleeps = vision_sleep.findMultiple(screenshot, 0.5, ...) # 50% confidence
```

Lower values = more detections but more false positives
Higher values = fewer false positives but may miss targets

### Modify Action Delays

```python
# In bot.py - adjust sleep times
sleep(2)  # Wait 2 seconds after action
pyautogui.moveTo(x=screen_x, y=screen_y, duration=3.0)  # 3 second move
```

## 📝 Future Improvements

Potential enhancements to address limitations:

1. **Scale-Invariant Detection**: Use SIFT/SURF instead of template matching
2. **OCR Integration**: Use Tesseract for text-based element detection
3. **Machine Learning**: Train models to recognize UI elements
4. **Multi-Resolution Support**: Automatically scale templates
5. **Error Recovery**: Implement retry logic and fallback strategies
6. **Configuration File**: Move credentials and settings to external config
7. **Dynamic Thresholds**: Auto-adjust confidence based on detection success
8. **API Integration**: Use game APIs if/when available

## 📚 Educational Use

This project is ideal for learning:
- **Computer Vision**: Template matching, image processing
- **Browser Automation**: Selenium WebDriver patterns
- **State Machines**: Game state tracking and decision making
- **Event-Driven Programming**: Responding to visual cues
- **Logging and Debugging**: Troubleshooting visual automation

## ⚖️ Legal Disclaimer

This project is for **educational purposes only**. Using automation tools with online games may:
- Violate the game's Terms of Service
- Result in account suspension or banning
- Be considered cheating by the game community
- Have legal consequences depending on jurisdiction

**Use at your own risk.** The authors assume no responsibility for consequences of using this software.

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Better error handling
- Multi-resolution support
- Performance optimizations
- Additional game support
- Documentation improvements

## 📄 License

[Specify your license here]

## 🙏 Acknowledgments

- OpenCV community for computer vision tools
- Selenium project for browser automation
- PyAutoGUI for cross-platform GUI automation

---

**Note**: This README represents automation techniques that have been used in enterprise software for decades. While demonstrated on a game, these same principles apply to automating legacy systems, terminal applications, and other software without programmatic interfaces.

---
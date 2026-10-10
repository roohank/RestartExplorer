# RestartExplorer

An NVDA add-on that restarts the Windows Explorer process with a single keyboard shortcut. This is useful when Windows Explorer stops responding and shortcuts like **Win+M** (show desktop) stop working.

**Repository:** [https://github.com/roohank/RestartExplorer](https://github.com/roohank/RestartExplorer)

## Features

- Restarts `explorer.exe` instantly with a keyboard shortcut.
- Runs silently in the background without freezing NVDA.
- Provides audio feedback via NVDA's speech.
- Uses a conflict-free default shortcut (`NVDA + Shift + Control + R`) that can be customized by the user.

## Keyboard Shortcut

| Key Combination | Action |
|---|---|
| `NVDA + Shift + Control + R` | Restart Windows Explorer |

## How to Use

Press `NVDA + Shift + Control + R` at any time. NVDA will announce:

- "Restarting Explorer..." while the operation is in progress.
- "Explorer restarted successfully." when done.

If something goes wrong, NVDA will announce the error message.

### Changing the Shortcut

If you prefer a different key combination:

1. Open the NVDA menu (`NVDA + N`).
2. Go to **Preferences** → **Input Gestures**.
3. In the tree view, find **RestartExplorer**.
4. Select **Restart the Windows Explorer process**.
5. Click **Add**, press your desired key combination, and confirm.
6. Click **OK**.

## Why Use This Add-on?

Sometimes on Windows 10 and Windows 11, Windows Explorer may hang or become unresponsive. When this happens, some keyboard shortcuts — such as `Win + M` for showing the desktop — stop working. The usual fix is to restart `explorer.exe` manually. This add-on automates that process with a single key press.

## Requirements

- NVDA version 2019.3 or later.
- Windows 10 or Windows 11.

## Installation

1. Download the latest `RestartExplorer.nvda-addon` file from the [Releases](https://github.com/roohank/RestartExplorer/releases) page.
2. Press `Enter` on the file or double-click it.
3. Follow the on-screen instructions in NVDA to install the add-on.
4. Restart NVDA when prompted.

## Building from Source

If you want to build the add-on yourself:

1. Clone this repository:

   ```bash
   git clone https://github.com/roohank/RestartExplorer.git
2. 
Make sure the folder structure looks like this:
text
Copy
Download
RestartExplorer/
├── manifest.ini
├── README.md
├── LICENSE
├── doc/
│   └── en/
│       └── readme.html
└── globalPlugins/
    └── restartExplorer.py
3. 
Select manifest.ini, doc, and the globalPlugins folder.
4. 
Right-click → Send to → Compressed (zipped) folder.
5. 
Rename the resulting .zip file to RestartExplorer.nvda-addon.
License
This add-on is released under the GNU General Public License v2.0. See the LICENSE file for details.
Author
• 
Roohan — GitHub: @roohank
Changelog
Version 1.3
• 
Added a conflict-free default shortcut (NVDA + Shift + Control + R).
• 
This is necessary because NVDA 2026.1 does not show scripts without a default gesture in the Input Gestures dialog, so users could not assign a shortcut themselves.
• 
The shortcut can still be changed by the user via Input Gestures.
Version 1.2
• 
Removed the default keyboard shortcut to avoid conflicts with NVDA's Remote Access.
• 
Updated documentation.
Version 1.1
• 
Translated UI messages from Persian to English.
• 
Updated documentation.
Version 1.0
• 
Initial release.
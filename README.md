# RestartExplorer

An NVDA add-on that restarts the Windows Explorer process with a single keyboard shortcut. This is useful when Windows Explorer stops responding and shortcuts like **Win+M** (show desktop) stop working.

**Repository:** [https://github.com/roohank/RestartExplorer](https://github.com/roohank/RestartExplorer)

## Features

- Restarts `explorer.exe` instantly with a keyboard shortcut.
- Runs silently in the background without freezing NVDA.
- Provides audio feedback to the user via NVDA's speech.

## Keyboard Shortcut

| Key Combination | Action |
|---|---|
| `NVDA + Alt + R` | Restart Windows Explorer |

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

## Usage

Press `NVDA + Alt + R` at any time. NVDA will announce:

> "Restarting Explorer..."

Then, after a moment:

> "Explorer restarted successfully."

If something goes wrong, NVDA will announce the error message.

## Building from Source

If you want to build the add-on yourself:

1. Clone this repository:

   ```bash
   git clone https://github.com/roohank/RestartExplorer.git
2. 
Make sure the folder structure looks like this:
RestartExplorer/
├── manifest.ini
├── README.md
├── LICENSE
└── globalPlugins/
    └── restartExplorer.py
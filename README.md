# JiraTime

A native iOS time tracking application built with SwiftUI and SwiftData.

## Features

- **Dashboard**: Displays active timer and project list.
- **Manual Entry**: Create custom time entries with start/stop functionality.
- **Jira Integration**: Settings screen for Jira API credentials (base URL, API token).
- **Local Storage**: Persist time logs locally on the device using SwiftData.

## Technical Stack

- **Language**: Swift
- **UI Framework**: SwiftUI
- **Data Persistence**: SwiftData
- **Networking**: URLSession (for Jira API integration)

## Installation

1. Clone the repository
2. Open `JiraTime.xcodeproj` in Xcode
3. Select a target (iOS Simulator)
4. Press Play

## Usage

1. Launch the app in the simulator.
2. Navigate to the Dashboard to start the timer.
3. Use the Manual Entry screen to log time manually.
4. Go to Settings to configure Jira API credentials.

## Jira API Setup

To use the Jira integration, you need a Jira API key:
1. Log in to your Jira account.
2. Go to **Profile** (top right) -> **API Settings**.
3. Click **Create API Key**.
4. Enter a description (e.g., "JiraTime iOS App") and paste into the app's Settings screen.

## Configuration

- No environment variables required; credentials are stored securely in the device's Keychain via KeychainWrapper.

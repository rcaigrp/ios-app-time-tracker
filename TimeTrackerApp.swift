import SwiftUI
import SwiftData

@main
struct TimeTrackerApp: App {
    var body: some Scene {
        WindowGroup {
            TabView {
                DashboardView()
                    .tabItem {
                        Label("Dashboard", systemImage: "list")
                    }
                TimerView()
                    .tabItem {
                        Label("Timer", systemImage: "timer")
                    }
                SettingsView()
                    .tabItem {
                        Label("Settings", systemImage: "gear")
                    }
            }
        }
    }
}
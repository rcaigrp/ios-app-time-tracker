import SwiftUI
import SwiftData

@main
struct JiraTimeApp: App {
    var body: some Scene {
        WindowGroup {
            DashboardView()
        }
        .modelContainer(for: [TimeEntry.self, Project.self])
    }
}
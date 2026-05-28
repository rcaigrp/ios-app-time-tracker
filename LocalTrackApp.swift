import SwiftUI
import SwiftData

@main
struct JiraTimeApp: App {
    @Environment(\.@.modelContext) private var modelContext
    
    var body: some Scene {
        WindowGroup {
            DashboardView()
        }
        .modelContainer(for: [TimeEntry.self])
    }
}
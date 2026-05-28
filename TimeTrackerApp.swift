import SwiftUI
import SwiftData

@main
struct JiraTimeApp: App {
    @Environment(\.@.modelContext) private var modelContext

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: [TimeEntry.self])
    }
}
import SwiftUI
import SwiftData

@main
struct JiraTimeApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: [TimeEntry.self], defaultConfiguration: .init(storageBehavior: .onQueue(.main)))
    }
}
import SwiftUI
import SwiftData

@main
struct LocalTrackApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .modelContainer(for: [TimeEntry.self])
    }
}
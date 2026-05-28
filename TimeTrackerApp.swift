import SwiftUI
import SwiftData

@main
struct TimeTrackerApp: App {
    @StateModel var dataController: DataController

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(\.modelContext, dataController.modelContext)
        }
    }

    init() {
        let url = FileManager.default.url(for: .applicationSupportDirectory, in: .userDomainMask, appropriateFor: nil, create: false)
        let storeURL = url!.appendingPathComponent("TimeTracker.sqlite")

        let container = try! ModelContainer(
            for: TimeEntry.self,
            configuration: ModelConfiguration("TimeTrackerModel", url: storeURL),
            defaultModel: nil
        )

        dataController = DataController(inMemory: false, container: container)
    }
}
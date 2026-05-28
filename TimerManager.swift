import SwiftData

@MainActor
final class TimerManager: ObservableObject {
    @Published var isRunning = false
    @Published var currentEntry: TimeEntry?

    let modelContext: ModelContext

    init(modelContext: ModelContext) {
        self.modelContext = modelContext
    }

    func startTimer() {
        let entry = TimeEntry(description: "New Entry", startTime: Date(), modelContext: modelContext)
        modelContext.insert(entry)
        currentEntry = entry
        isRunning = true
    }

    func stopTimer() {
        guard let entry = currentEntry else { return }
        entry.endTime = Date()
        isRunning = false
        currentEntry = nil
    }
}
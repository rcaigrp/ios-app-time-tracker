import SwiftData

@Model
final class TimeLog {
    var project: String
    var startTime: Date
    var endTime: Date
    var notes: String
    
    init(project: String, startTime: Date, endTime: Date, notes: String) {
        self.project = project
        self.startTime = startTime
        self.endTime = endTime
        self.notes = notes
    }
}

class LogStorage {
    let container: NSPersistentContainer
    
    init() {
        self.container = NSPersistentContainer(name: "TimeTracker")
        self.container.loadPersistentStores { _, error in
            print("Failed to load persistent stores: \(error?.localizedDescription)")
        }
    }
    
    func saveLog(_ log: TimeLog) {
        // Save logic
    }
}

import SwiftData

@Model
class TimeEntryModel {
    var name: String
    var startTime: Date
    var endTime: Date?
    var duration: TimeInterval

    init(name: String, startTime: Date, duration: TimeInterval) {
        self.name = name
        self.startTime = startTime
        self.duration = duration
    }

    var hasStarted: Bool { endTime == nil }
}

struct DataModel {
    static let container = ModelContainer([TimeEntryModel.self])

    static func saveEntry(_ entry: TimeEntryModel) {
        // SwiftData context save logic
    }
}
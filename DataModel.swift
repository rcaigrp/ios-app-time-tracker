import SwiftData

@Model
final class TimeEntry {
    var id = UUID()
    var startTime = Date()
    var endTime: Date?
    var project = ""
    var description = ""

    init(project: String, description: String) {
        self.project = project
        self.description = description
        self.startTime = Date()
    }
}
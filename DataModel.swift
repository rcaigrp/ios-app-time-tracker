import SwiftData

@Model
final class TimeEntry {
    var id = UUID()
    var description: String
    var startTime: Date
    var endTime: Date?
    var project: Project?

    var elapsedTime: TimeInterval {
        if let end = endTime {
            return end.timeIntervalSince(startTime)
        }
        return Date().timeIntervalSince(startTime)
    }
}

@Model
final class Project {
    var id = UUID()
    var name: String
    var jiraKey: String?
}
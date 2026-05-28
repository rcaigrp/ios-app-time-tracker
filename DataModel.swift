import SwiftData

@Model
class TimeEntry {
    var id = UUID()
    var taskName: String
    var startTime: Date
    var endTime: Date?
    var jiraTicketId: String?
    var duration: TimeInterval = 0

    init(taskName: String, startTime: Date) {
        self.taskName = taskName
        self.startTime = startTime
    }
}
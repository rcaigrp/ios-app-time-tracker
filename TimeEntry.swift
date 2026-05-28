import Foundation
import SwiftData

@Model
final class TimeEntry {
    var id: UUID
    var project: String
    var date: Date
    var startTime: Date
    var endTime: Date
    var duration: Double // in hours
    var notes: String?

    init(project: String, date: Date, startTime: Date, endTime: Date, duration: Double, notes: String? = "") {
        self.id = UUID()
        self.project = project
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.duration = duration
        self.notes = notes
    }
}
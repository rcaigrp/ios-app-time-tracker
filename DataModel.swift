import Foundation
import SwiftData

@Model
final class TimeEntry {
    var id: UUID
    var description: String
    var startTime: Date
    var stopTime: Date?
    var project: String?

    init(description: String = "", startTime: Date = Date(), project: String? = nil) {
        self.id = UUID()
        self.description = description
        self.startTime = startTime
        self.stopTime = nil
        self.project = project
    }
}
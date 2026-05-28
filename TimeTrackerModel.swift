import Foundation
import SwiftData

@MainActor
class TimeTrackerDataModel {
    let context: Context
    
    init(context: Context) {
        self.context = context
    }
    
    func addEntry(_ entry: TimeEntry) {
        context.insert(entry)
        try? context.save()
    }
    
    func fetchEntries() -> [TimeEntry] {
        let descriptor = FetchDescriptor<TimeEntry>()
        return try? context.fetch(descriptor) ?? []
    }
    
    func deleteEntry(_ entry: TimeEntry) {
        context.delete(entry)
        try? context.save()
    }
}

@MainActor
class JiraService {
    var baseUrl: String
    var username: String
    var token: String
    
    init(baseUrl: String, username: String, token: String) {
        self.baseUrl = baseUrl
        self.username = username
        self.token = token
    }
    
    func fetchProjects() async -> [String] {
        // Mock implementation for testing
        return ["Project 1", "Project 2"]
    }
}

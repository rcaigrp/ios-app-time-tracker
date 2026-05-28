import SwiftUI
import SwiftData

struct DashboardView: View {
    @Environment(\.managedContext) private var managedContext
    @Query private var entries: [TimeEntry]
    
    var body: some View {
        List(entries) { entry in
            VStack(alignment: .leading) {
                Text(entry.projectName).font(.headline)
                Text(entry.notes).font(.subscript())
                Text("Duration: \(entry.duration.formatted())s").font(.caption())
            }
        }
        .navigationTitle("Projects")
    }
}
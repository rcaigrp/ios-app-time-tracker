import SwiftUI
import SwiftData

struct DashboardView: View {
    @Environment(\.@.modelContext) private var modelContext
    @Query private var timeEntries: [TimeEntry]
    
    @State private var timerRunning = false
    @State private var elapsedTime = TimeInterval()
    
    // TimerManager Integration
    @StateObject private var timerManager = TimerManager()
    
    var body: some View {
        NavigationStack {
            List {
                // Project List
                ForEach(timeEntries) { entry in
                    NavigationLink {
                        // Manual Entry Screen for details
                        ManualEntryView(entry: entry)
                    } label: {
                        HStack {
                            VStack(alignment: .leading) {
                                Text(entry.taskName)
                                    .font(.headline)
                                Text("Started: \(entry.startTime.formatted())")
                                    .font(.caption)
                                    .foregroundColor(.secondary)
                            }
                            Spacer()
                            Text("\(entry.duration, specifier: "%.1f")s")
                                .font(.caption)
                                .foregroundColor(.secondary)
                        }
                    }
                }
                
                // Active Timer Section
                if timerRunning {
                    HStack {
                        Text("Timer Running")
                        Spacer()
                        Text("\(timerManager.elapsedTime, specifier: "%.1f")s")
                            .font(.caption)
                    }
                    .padding()
                    .background(Color.gray.opacity(0.1))
                }
            }
            .navigationTitle("JiraTime")
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button(timerRunning ? "Stop" : "Start") {
                        if timerRunning {
                            timerManager.stop()
                        } else {
                            timerManager.start()
                        }
                        timerRunning = !timerRunning
                    }
                    .disabled(timeEntries.isEmpty)
                }
            }
        }
    }
}

#Preview {
    DashboardView()
        .modelContainer(for: [TimeEntry.self])
}
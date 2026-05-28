import SwiftUI
import SwiftData

struct DashboardView: View {
    @Environment(\.modelContext) private var modelContext
    @Query(sort: \..startTime, order: .reverse) private var entries: [TimeEntry]

    @State private var timerManager = TimerManager(modelContext: modelContext)

    var body: some View {
        NavigationStack {
            List {
                ForEach(entries) { entry in
                    HStack {
                        VStack(alignment: .leading) {
                            Text(entry.description)
                            Text(entry.elapsedTime.formatted())
                                .font(.caption)
                                .foregroundColor(.secondary)
                            if entry == entries.first && entry.endTime == nil {
                                ProgressView()
                                    .padding(.trailing, 10)
                            }
                        }
                        Spacer()
                    }
                    .onTapGesture {
                        if entry == entries.first && entry.endTime == nil {
                            timerManager.stopTimer()
                        }
                    }
                }
                .onDelete(perform: deleteEntries)
            }
            .navigationTitle("JiraTime")
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button {
                        timerManager.startTimer()
                    } label {
                        Label("Add", systemImage: "plus")
                    }
                }
            }
        }
    }

    private func deleteEntries(offsets: IndexSet) {
        withAnimation {
            for index in offsets {
                modelContext.delete(entries[index])
            }
        }
    }
}
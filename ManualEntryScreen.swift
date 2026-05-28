import SwiftUI

struct ManualEntryScreen: View {
    var body: some View {
        VStack {
            Text("Manual Time Entry")
            TextField("Project Name", text: .constant(""))
            TextField("Notes", text: .constant(""))
            Button("Start Timer") { }
        }
    }
}

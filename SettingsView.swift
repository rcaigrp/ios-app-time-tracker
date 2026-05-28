import SwiftUI

struct SettingsView: View {
    @AppStorage("jiraBaseUrl") private var jiraBaseUrl = ""
    @AppStorage("jiraApiToken") private var jiraApiToken = ""
    @AppStorage("jiraUsername") private var jiraUsername = ""

    var body: some View {
        Form {
            Section("Jira Settings") {
                TextField("Base URL", text: $jiraBaseUrl)
                TextField("API Token", text: $jiraApiToken)
                TextField("Username", text: $jiraUsername)
            }
        }
        .navigationTitle("Settings")
    }
}
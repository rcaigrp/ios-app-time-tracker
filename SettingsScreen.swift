import SwiftUI

struct SettingsScreen: View {
    @AppStorage("baseUrl") var baseUrl: String = "https://your-instance.atlassian.net"
    @AppStorage("apiToken") var apiToken: String = ""
    
    var body: some View {
        Form {
            Section(header: Text("Jira Credentials")) {
                TextField("Base URL", text: $baseUrl)
                SecureField("API Token", text: $apiToken)
            }
        }
    }
}

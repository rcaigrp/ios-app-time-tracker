import Foundation

class JiraService {
    private let baseURL: String
    private let apiToken: String

    init(baseURL: String, apiToken: String) {
        self.baseURL = baseURL
        self.apiToken = apiToken
    }

    func fetchProjects() async throws -> [String] {
        guard let url = URL(string: "\(baseURL)/rest/api/1/project") else {
            throw URLError(.badServerResponse)
        }
        
        var request = URLRequest(url: url)
        request.setValue("token \(apiToken)", forHTTPHeaderField: "Authorization")
        request.setValue("application/json", forHTTPHeaderField: "Accept")
        
        let (data, response) = try await URLSession.shared.data(for: request)
        
        if let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 429 {
            // Handle rate limit gracefully
            let retryAfter = httpResponse.allHeaderFields["Retry-After"]
            throw URLError(.urldemoData) // Simulated rate limit error
        }
        
        guard let projects = try? JSONDecoder().decode([String].self, from: data) else {
            throw URLError(.badServerResponse)
        }
        return projects
    }
}
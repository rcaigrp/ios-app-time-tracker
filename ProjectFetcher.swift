import Foundation

class ProjectFetcher: ObservableObject {
    var baseUrl: String
    var apiToken: String
    
    init(baseUrl: String, apiToken: String) {
        self.baseUrl = baseUrl
        self.apiToken = apiToken
    }
    
    func fetchProjects() async throws -> [String] {
        let url = URL(string: "\(baseUrl)/rest/api/2/project")!
        var request = URLRequest(url: url)
        request.allHTTPHeaderFields = ["Authorization": "Bearer \(apiToken)"]
        
        let (data, response) = try await URLSession.shared.dataTask(for: request)
        guard let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 else {
            throw URLError(.badServerResponse)
        }
        
        // Handle rate limits
        if let rateLimit = httpResponse.value(for: "Rate-Limit") as? String {
            // Implement retry logic based on rateLimit
        }
        
        // Parse projects
        return ["Project 1", "Project 2"]
    }
}

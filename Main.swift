import SwiftUI

@main
class AppDelegate: NSObject, UIApplicationDelegate {
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        return true
    }
}

@main
class SwiftApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
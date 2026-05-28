import Foundation
import SwiftData

@Observable
final class TimerManager {
    var elapsedTime = TimeInterval()
    var isRunning = false
    var timer: Timer?
    
    func start() {
        guard !isRunning else { return }
        isRunning = true
        timer = Timer(scheduledIn: .main, repeats: true) { _ in
            elapsedTime += 1.0
        }
    }
    
    func stop() {
        timer?.invalidate()
        timer = nil
        isRunning = false
    }
    
    func reset() {
        stop()
        elapsedTime = 0
    }
}
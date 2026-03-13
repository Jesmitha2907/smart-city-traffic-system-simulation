# Smart City Traffic System Simulation

## Project Overview
This project is a Python-based simulation designed to solve urban traffic congestion using a coordinated signal propagation mechanism. Developed as a term project at Gayatri Vidya Parishad College of Engineering for Women under the guidance of Dr. M. Bhanu Sridhar, the system demonstrates how fundamental physics can optimize city infrastructure.

## Key Features
1. Green Wave Algorithm: Uses the physics-based formula Time = Distance / Speed to synchronize signals across multiple junctions.
2. Real-time Visualization: A grid-based terminal dashboard displaying 4-lane signal statuses and live countdowns.
3. Dynamic Synchronization: Automatically calculates signal offsets based on user-defined junction counts, distances, and vehicle speeds.
4. Visual Clarity: Implements ANSI color codes (Red, Green, Yellow) for an intuitive, live-updating user interface.

## Technologies Used
1. Language: Python
2. Modules: Time (for real-time refresh) and OS (for terminal management)
3. Styling: ANSI Color Codes for Terminal UI
4. Logic: Physics-based motion algorithms

## How It Works
1. Input Parameters: The user provides the number of junctions, the distance between them in meters, and the average vehicle speed in kilometers per hour.
2. Logic Computation: The system determines the time gap required for a vehicle to move from one junction to the next.
3. Execution: The simulation starts a synchronized countdown, ensuring that a vehicle moving at the set speed hits a Green Wave at every intersection.

 ## Future Scope
(i)   Integration with IoT-based vehicle density sensors.
(ii)  Emergency vehicle priority control for ambulances and fire engines.
(iii) Development of a Graphical User Interface.
output
(output.png)

Author: Mellamputi Jesmitha
Academic Year: 2026
Department: Information Technology

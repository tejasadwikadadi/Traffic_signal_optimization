def display_results(results):

    print("\n")
    print("=" * 60)
    print("        TRAFFIC SIGNAL OPTIMIZATION REPORT")
    print("=" * 60)

    for road, info in results.items():

        print(
            f"{road:<10} | "
            f"Vehicles: {info['vehicles']:<3} | "
            f"Density: {info['density']:<6} | "
            f"Green Time: {info['green_time']} sec"
        )

    print("=" * 60)


# ==========================================================
# MODE SELECTION
# ==========================================================

print("\nSelect Mode")
print("1. Manual Input")
print("2. Demo Data")

choice = input("Enter your choice (1 or 2): ")


# ==========================================================
# MANUAL INPUT MODE
# ==========================================================

if choice == "1":

    traffic_data = {

        "North": int(input("Enter North Road Vehicle Count : ")),

        "South": int(input("Enter South Road Vehicle Count : ")),

        "East": int(input("Enter East Road Vehicle Count : ")),

        "West": int(input("Enter West Road Vehicle Count : "))
    }


# ==========================================================
# DEMO MODE
# ==========================================================

else:

    traffic_data = {

        "North": 50,
        "South": 28,
        "East": 10,
        "West": 42
    }


# ==========================================================
# PROCESS DATA
# ==========================================================

optimized_results = optimize_signals(traffic_data)


# ==========================================================
# DISPLAY OUTPUT
# ==========================================================

display_results(optimized_results)

# CO6 : Explainable AI Trace
explain_decision(optimized_results)


# ==========================================================
# CO2 FUTURE EXTENSION
# ==========================================================
#
# Search Algorithms:
#
# - BFS
# - DFS
# - Uniform Cost Search
# - A*
#
# Future Enhancement:
#
# Optimize vehicle routing across multiple
# intersections using A* Search.
#
# Example:
#
# Junction A ---- Junction B ---- Junction C
#
# A* can determine the least congested path.
#
# ==========================================================


# ==========================================================
# CO5 FUTURE EXTENSION
# ==========================================================
#
# Bayesian Traffic Prediction
#
# Example:
#
# P(Congestion | Rain)
#
# Predict future traffic conditions
# using probabilistic reasoning.
#
# ==========================================================


# ==========================================================
# CO6 FUTURE HYBRID AI
# ==========================================================
#
# Rule-Based System
#        +
# Search Algorithms
#        +
# Bayesian Inference
#
# = Intelligent Traffic Management System
#
# ==========================================================
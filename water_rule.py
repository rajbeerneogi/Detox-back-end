
def generate_recommendations(analysis: dict) -> dict:
    """
    Convert AI visual observations into cautious
    water-quality recommendations.

    This function does not estimate chemical measurements
    or determine whether water is safe to drink.
    """

    appearance = str(
        analysis.get("appearance", "Uncertain")
    ).lower()

    particles = analysis.get("visible_particles", False)
    sediment = analysis.get("possible_sediment", False)
    algae = analysis.get("possible_algae", False)

    concerns = []
    recommendations = []

    # Cloudy or murky water
    if appearance in ["cloudy", "murky"]:
        concerns.append("Reduced visual clarity")
        recommendations.extend([
            "Arrange a physical turbidity test.",
            "Investigate possible suspended particles."
        ])

    # Discoloured water
    if appearance in ["discolored", "discoloured", "brown", "yellow"]:
        concerns.append("Unusual water coloration")
        recommendations.extend([
            "Investigate possible sediment or other causes of discoloration.",
            "Consider appropriate laboratory testing."
        ])

    # Greenish appearance
    if appearance in ["green", "greenish"]:
        concerns.append("Greenish water appearance")
        recommendations.extend([
            "Investigate possible algae growth.",
            "Consider appropriate algae and microbiological testing."
        ])

    # Visible particles
    if particles:
        concerns.append("Visible suspended particles")
        recommendations.append(
            "Investigate the source of the visible particles."
        )

    # Possible sediment
    if sediment:
        concerns.append("Possible visible sediment")
        recommendations.append(
            "Consider sediment analysis and appropriate filtration assessment."
        )

    # Possible algae
    if algae:
        concerns.append("Possible algae-like appearance")
        recommendations.append(
            "Arrange appropriate testing before considering the water safe."
        )

    # Clear water
    if appearance == "clear" and not concerns:
        recommendations.extend([
            "Clear appearance does not establish drinking-water safety.",
            "Consider appropriate chemical and microbiological testing."
        ])

    # Uncertain or unsupported descriptions
    if not concerns and appearance not in ["clear"]:
        concerns.append("Uncertain visual condition")
        recommendations.extend([
            "Try another photograph with better lighting.",
            "Arrange appropriate physical water-quality testing."
        ])

    recommendations.append(
        "Do not drink water of uncertain quality until its safety "
        "has been appropriately established."
    )

    # Remove duplicate recommendations
    recommendations = list(dict.fromkeys(recommendations))

    if concerns:
        status = "Caution"
    else:
        status = "Visual concerns not observed"

    return {
        "visual_status": appearance.capitalize(),
        "potential_concerns": concerns,
        "recommendations": recommendations,
        "measurements": {
            "ph": None,
            "tds": None,
            "turbidity": None
        },
        "safety_status": "Not verified",
        "recommendation_status": status
    }

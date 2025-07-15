def calculate_risk_score(data):
    score = 0

    # Assign points based on risk factors
    if data['age'] >= 45:
        score += 2
    elif data['age'] >= 30:
        score += 1

    if data['bmi'] >= 30:
        score += 2
    elif data['bmi'] >= 25:
        score += 1

    if data['smoking']:
        score += 2

    if data['alcohol_consumption']:
        score += 1

    if data['physical_activity'] == 'low':
        score += 2
    elif data['physical_activity'] == 'moderate':
        score += 1

    if data['family_history']:
        score += 2

    # Categorize
    if score >= 7:
        category = 'High'
    elif score >= 4:
        category = 'Moderate'
    else:
        category = 'Low'

    return score, category

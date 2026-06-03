def grade_processor(scores):
    valid_scores = {}
    
    for index, score in enumerate(scores): # Get a list of all valid scores
        if score == -999:
            print(f"Encountered -999, stopping the loop.")
            break

        if score < 0:
            print(f"Skipping negative score: {score}")
            continue
        
        print(f"Score {index + 1}: {score}.")
        valid_scores[index] = score, calculate_letter_grade(score)

    if not valid_scores: # Check if there are any valid scores to process
        print("No valid scores to process.")
        return
    
    # Print statistics about the valid scores
    average_score = sum(score for score, _ in valid_scores.values()) / len(valid_scores)
    print(f"Average Score: {average_score:.2f}")
    
    highest_grade = max(score for score, _ in valid_scores.values())
    lowest_grade = min(score for score, _ in valid_scores.values())
    print(f"Highest Grade: {highest_grade}")
    print(f"Lowest Grade: {lowest_grade}")
    
    print("Grade Distribution:")
    distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for _, grade in valid_scores.values():
        distribution[grade] += 1
    
    print(f"A: {distribution['A']}")
    print(f"B: {distribution['B']}")
    print(f"C: {distribution['C']}")
    print(f"D: {distribution['D']}")
    print(f"F: {distribution['F']}")
    

def calculate_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

if __name__ == "__main__":
    scores = [88, 92, 75, -1, 63, 95, 81, 70, -5, 55, 100, 78, -999, 90, 85]
    
    grade_processor(scores)
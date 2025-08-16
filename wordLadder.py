from collections import deque

def word_ladder(start, end, dictionary):
    """
    Transform a start word into an end word by changing one letter at a time,
    using BFS to find the shortest transformation sequence.
    
    Args:
        start (str): Starting word
        end (str): Target word
        dictionary (set): Set of valid intermediate words
    
    Returns:
        list: Shortest transformation sequence, or empty list if no path exists
    """
    # Edge cases
    if start == end:
        return [start]
    
    if end not in dictionary:
        return []
    
    # Add start word to dictionary for processing
    dictionary = set(dictionary)
    dictionary.add(start)
    
    # BFS setup
    queue = deque([(start, [start])])  # (current_word, path_to_current_word)
    visited = {start}
    
    while queue:
        current_word, path = queue.popleft()
        
        # Generate all possible one-letter variations
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == current_word[i]:
                    continue
                
                # Create new word by changing one letter
                new_word = current_word[:i] + c + current_word[i+1:]
                
                # Check if we reached the target
                if new_word == end:
                    return path + [new_word]
                
                # If valid word and not visited, add to queue
                if new_word in dictionary and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, path + [new_word]))
    
    # No transformation sequence found
    return []


def is_one_letter_different(word1, word2):
    """Helper function to check if two words differ by exactly one letter"""
    if len(word1) != len(word2):
        return False
    
    diff_count = sum(1 for c1, c2 in zip(word1, word2) if c1 != c2)
    return diff_count == 1


# Test with the provided example
def test_word_ladder():
    start = 'hit'
    end = 'cog'
    dictionary = {'hot', 'dot', 'dog', 'lot', 'log', 'cog'}
    
    result = word_ladder(start, end, dictionary)
    print(f"Start: {start}")
    print(f"End: {end}")
    print(f"Dictionary: {dictionary}")
    print(f"Transformation sequence: {result}")
    print(f"Steps: {len(result) - 1}")
    
    # Verify the transformation is valid
    if result:
        print("\nVerification:")
        for i in range(len(result) - 1):
            current = result[i]
            next_word = result[i + 1]
            is_valid = is_one_letter_different(current, next_word)
            print(f"{current} -> {next_word}: {'✓' if is_valid else '✗'}")
    
    return result


# Additional test cases
def run_additional_tests():
    print("\n" + "="*50)
    print("ADDITIONAL TEST CASES")
    print("="*50)
    
    test_cases = [
        # Test case 1: No transformation possible
        {
            'start': 'hit',
            'end': 'cog',
            'dictionary': {'hot', 'dot', 'dog', 'lot', 'log'},  # Missing 'cog'
            'expected': []
        },
        
        # Test case 2: Same start and end word
        {
            'start': 'cat',
            'end': 'cat',
            'dictionary': {'bat', 'hat'},
            'expected': ['cat']
        },
        
        # Test case 3: Simple one-step transformation
        {
            'start': 'cat',
            'end': 'bat',
            'dictionary': {'bat'},
            'expected': ['cat', 'bat']
        },
        
        # Test case 4: Longer transformation
        {
            'start': 'cold',
            'end': 'warm',
            'dictionary': {'cold', 'cord', 'word', 'ward', 'warm'},
            'expected': ['cold', 'cord', 'word', 'ward', 'warm']
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        result = word_ladder(test['start'], test['end'], test['dictionary'])
        print(f"Start: {test['start']}, End: {test['end']}")
        print(f"Result: {result}")
        print(f"Expected: {test['expected']}")
        print(f"Status: {'PASS' if result == test['expected'] else 'FAIL'}")


if __name__ == "__main__":
    # Run the main example
    test_word_ladder()
    
    # Run additional tests
    run_additional_tests()
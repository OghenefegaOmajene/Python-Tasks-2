import re
from collections import defaultdict, Counter

def normalize_sentence(sentence):
    """
    Normalize a sentence by removing spaces, punctuation and converting to lowercase.
    
    Args:
        sentence (str): Input sentence
        
    Returns:
        str: Normalized sentence with only alphabetic characters
    """
    # Remove all non-alphabetic characters and convert to lowercase
    normalized = re.sub(r'[^a-zA-Z]', '', sentence).lower()
    return normalized

def get_anagram_key_sorted(sentence):
    """
    Get anagram key using sorted characters approach.
    
    Args:
        sentence (str): Input sentence
        
    Returns:
        str: Sorted characters as anagram key
    """
    normalized = normalize_sentence(sentence)
    return ''.join(sorted(normalized))

def get_anagram_key_frequency(sentence):
    """
    Get anagram key using character frequency counts.
    
    Args:
        sentence (str): Input sentence
        
    Returns:
        tuple: Sorted tuple of (char, count) pairs
    """
    normalized = normalize_sentence(sentence)
    char_count = Counter(normalized)
    return tuple(sorted(char_count.items()))

def group_anagrams_sorted(sentences):
    """
    Group anagram sentences using sorted characters approach.
    
    Args:
        sentences (list): List of sentences to group
        
    Returns:
        list: List of lists, each containing anagram sentences
    """
    anagram_groups = defaultdict(list)
    
    for sentence in sentences:
        key = get_anagram_key_sorted(sentence)
        anagram_groups[key].append(sentence)
    
    # Return only groups with more than one sentence
    result = [group for group in anagram_groups.values() if len(group) > 1]
    return result

def group_anagrams_frequency(sentences):
    """
    Group anagram sentences using character frequency approach.
    
    Args:
        sentences (list): List of sentences to group
        
    Returns:
        list: List of lists, each containing anagram sentences
    """
    anagram_groups = defaultdict(list)
    
    for sentence in sentences:
        key = get_anagram_key_frequency(sentence)
        anagram_groups[key].append(sentence)
    
    # Return only groups with more than one sentence
    result = [group for group in anagram_groups.values() if len(group) > 1]
    return result

def group_all_anagrams(sentences):
    """
    Group all anagram sentences (including single sentences).
    
    Args:
        sentences (list): List of sentences to group
        
    Returns:
        list: List of lists, each containing anagram sentences
    """
    anagram_groups = defaultdict(list)
    
    for sentence in sentences:
        key = get_anagram_key_sorted(sentence)
        anagram_groups[key].append(sentence)
    
    # Return all groups
    return list(anagram_groups.values())

def are_anagrams(sentence1, sentence2):
    """
    Check if two sentences are anagrams of each other.
    
    Args:
        sentence1 (str): First sentence
        sentence2 (str): Second sentence
        
    Returns:
        bool: True if sentences are anagrams, False otherwise
    """
    norm1 = normalize_sentence(sentence1)
    norm2 = normalize_sentence(sentence2)
    
    return sorted(norm1) == sorted(norm2)

def detailed_analysis(sentences):
    """
    Provide detailed analysis of the anagram grouping process.
    
    Args:
        sentences (list): List of sentences to analyze
    """
    print("DETAILED ANAGRAM ANALYSIS")
    print("=" * 50)
    
    print("\n1. Sentence Normalization:")
    for i, sentence in enumerate(sentences, 1):
        normalized = normalize_sentence(sentence)
        sorted_chars = get_anagram_key_sorted(sentence)
        print(f"  {i}. '{sentence}'")
        print(f"     Normalized: '{normalized}'")
        print(f"     Sorted chars: '{sorted_chars}'")
    
    print("\n2. Anagram Key Mapping:")
    key_to_sentences = defaultdict(list)
    for sentence in sentences:
        key = get_anagram_key_sorted(sentence)
        key_to_sentences[key].append(sentence)
    
    for key, group in key_to_sentences.items():
        print(f"  Key '{key}': {group}")
    
    print("\n3. Final Groups (only groups with 2+ sentences):")
    result = group_anagrams_sorted(sentences)
    for i, group in enumerate(result, 1):
        print(f"  Group {i}: {group}")

def test_anagram_grouping():
    """Test the anagram grouping with the provided example"""
    
    print("ANAGRAM SENTENCE GROUPING TEST")
    print("=" * 50)
    
    # Test case from the problem
    sentences = ['Listen to me', 'Enlist to me', 'The eyes', 'They see']
    expected = [['Listen to me', 'Enlist to me'], ['The eyes', 'They see']]
    
    print(f"Input sentences: {sentences}")
    print(f"Expected output: {expected}")
    
    # Test both approaches
    result_sorted = group_anagrams_sorted(sentences)
    result_frequency = group_anagrams_frequency(sentences)
    
    print(f"\nResult (sorted approach): {result_sorted}")
    print(f"Result (frequency approach): {result_frequency}")
    
    # Verify results (order of groups doesn't matter)
    def normalize_result(result):
        return sorted([sorted(group) for group in result])
    
    expected_normalized = normalize_result(expected)
    result_normalized = normalize_result(result_sorted)
    
    print(f"\nTest Status: {'PASS' if result_normalized == expected_normalized else 'FAIL'}")
    
    # Detailed analysis
    print("\n")
    detailed_analysis(sentences)
    
    return result_sorted

def run_comprehensive_tests():
    """Run comprehensive test cases"""
    
    print("\n" + "=" * 60)
    print("COMPREHENSIVE TEST CASES")
    print("=" * 60)
    
    test_cases = [
        {
            'name': 'Basic anagrams',
            'input': ['Listen to me', 'Enlist to me', 'The eyes', 'They see'],
            'expected': [['Listen to me', 'Enlist to me'], ['The eyes', 'They see']]
        },
        {
            'name': 'No anagrams',
            'input': ['Hello world', 'Python code', 'Data science'],
            'expected': []
        },
        {
            'name': 'Single anagram group',
            'input': ['abc', 'bca', 'cab'],
            'expected': [['abc', 'bca', 'cab']]
        },
        {
            'name': 'Mixed punctuation',
            'input': ['A gentleman', 'Elegant man', 'Listen!', 'Silent.'],
            'expected': [['A gentleman', 'Elegant man'], ['Listen!', 'Silent.']]
        },
        {
            'name': 'Case insensitive',
            'input': ['LISTEN', 'Silent', 'enlist', 'TINSEL'],
            'expected': [['LISTEN', 'Silent', 'enlist', 'TINSEL']]
        },
        {
            'name': 'Complex punctuation and spacing',
            'input': ['A decimal point!', 'Im a dot in place', 'The Morse Code', 'Here come dots'],
            'expected': [['A decimal point!', 'Im a dot in place'], ['The Morse Code', 'Here come dots']]
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {test['name']}")
        print(f"Input: {test['input']}")
        
        result = group_anagrams_sorted(test['input'])
        
        # Normalize for comparison (order doesn't matter)
        def normalize_for_comparison(groups):
            return sorted([sorted(group) for group in groups])
        
        expected_norm = normalize_for_comparison(test['expected'])
        result_norm = normalize_for_comparison(result)
        
        print(f"Result: {result}")
        print(f"Expected: {test['expected']}")
        print(f"Status: {'PASS' if result_norm == expected_norm else 'FAIL'}")
        
        # Show individual anagram verification for failed cases
        if result_norm != expected_norm and test['name'] != 'No anagrams':
            print("  Anagram verification:")
            for sentence in test['input']:
                norm = normalize_sentence(sentence)
                key = get_anagram_key_sorted(sentence)
                print(f"    '{sentence}' -> '{norm}' -> '{key}'")

def performance_comparison():
    """Compare performance of different approaches"""
    
    print("\n" + "=" * 50)
    print("PERFORMANCE COMPARISON")
    print("=" * 50)
    
    import time
    
    # Create test data
    test_sentences = [
        'Listen to me', 'Enlist to me', 'The eyes', 'They see',
        'A gentleman', 'Elegant man', 'Conversation', 'Voices rant on',
        'Astronomer', 'Moon starer', 'The earthquakes', 'That queer shake'
    ] * 100  # Multiply for performance testing
    
    print(f"Testing with {len(test_sentences)} sentences...")
    
    # Test sorted approach
    start_time = time.time()
    result_sorted = group_anagrams_sorted(test_sentences)
    time_sorted = time.time() - start_time
    
    # Test frequency approach
    start_time = time.time()
    result_frequency = group_anagrams_frequency(test_sentences)
    time_frequency = time.time() - start_time
    
    print(f"Sorted approach time: {time_sorted:.4f} seconds")
    print(f"Frequency approach time: {time_frequency:.4f} seconds")
    print(f"Results match: {len(result_sorted) == len(result_frequency)}")

if __name__ == "__main__":
    # Run main test
    test_anagram_grouping()
    
    # Run comprehensive tests
    run_comprehensive_tests()
    
    # Performance comparison
    performance_comparison()
    
    # Interactive demo
    print("\n" + "=" * 50)
    print("INTERACTIVE DEMO")
    print("=" * 50)
    
    demo_sentences = [
        "The detectives", 
        "Detect thieves", 
        "Conversation", 
        "Voices rant on",
        "Astronomer",
        "Moon starer",
        "Not anagram"
    ]
    
    print(f"Demo sentences: {demo_sentences}")
    result = group_all_anagrams(demo_sentences)
    
    print(f"\nAll groups (including singles): {result}")
    print(f"Anagram groups only: {group_anagrams_sorted(demo_sentences)}")
import re
from collections import OrderedDict

def compress_sentence(sentence):
    """
    Compress a sentence by replacing each unique word with an integer ID.
    
    Args:
        sentence (str): Input sentence to compress
        
    Returns:
        tuple: (encoded_list, word_mapping_dict)
            - encoded_list: List of integer IDs representing words
            - word_mapping_dict: Dictionary mapping IDs to original words
    """
    # Split sentence into words (handle punctuation)
    words = sentence.lower().split()
    
    # Clean words by removing punctuation
    cleaned_words = []
    for word in words:
        # Remove punctuation but keep the word
        cleaned_word = re.sub(r'[^\w]', '', word)
        if cleaned_word:  # Only add non-empty words
            cleaned_words.append(cleaned_word)
    
    # Create mapping and encoded sequence
    word_to_id = {}
    id_to_word = {}
    encoded = []
    next_id = 1
    
    for word in cleaned_words:
        if word not in word_to_id:
            # First occurrence - assign new ID
            word_to_id[word] = next_id
            id_to_word[next_id] = word
            next_id += 1
        
        # Add ID to encoded sequence
        encoded.append(word_to_id[word])
    
    return encoded, id_to_word

def compress_sentence_preserve_case(sentence):
    """
    Compress sentence while preserving original case and punctuation info.
    
    Args:
        sentence (str): Input sentence to compress
        
    Returns:
        tuple: (encoded_list, word_mapping_dict, case_info, punctuation_info)
    """
    words = sentence.split()
    
    word_to_id = {}
    id_to_word = {}
    encoded = []
    case_info = []
    punctuation_info = []
    next_id = 1
    
    for word in words:
        # Extract punctuation
        punctuation = re.findall(r'[^\w\s]', word)
        clean_word = re.sub(r'[^\w]', '', word).lower()
        
        if clean_word:
            # Store case information
            original_case = re.sub(r'[^\w]', '', word)
            
            if clean_word not in word_to_id:
                word_to_id[clean_word] = next_id
                id_to_word[next_id] = clean_word
                next_id += 1
            
            encoded.append(word_to_id[clean_word])
            case_info.append(original_case)
            punctuation_info.append(''.join(punctuation))
    
    return encoded, id_to_word, case_info, punctuation_info

def decompress_sentence(encoded, mapping):
    """
    Decompress an encoded sentence back to original text.
    
    Args:
        encoded (list): List of integer IDs
        mapping (dict): Dictionary mapping IDs to words
        
    Returns:
        str: Decompressed sentence
    """
    words = [mapping[id_num] for id_num in encoded]
    return ' '.join(words)

def decompress_sentence_with_case(encoded, mapping, case_info, punctuation_info):
    """
    Decompress sentence with original case and punctuation restored.
    
    Args:
        encoded (list): List of integer IDs
        mapping (dict): Dictionary mapping IDs to words
        case_info (list): Original case information
        punctuation_info (list): Original punctuation information
        
    Returns:
        str: Decompressed sentence with original formatting
    """
    words = []
    for i, id_num in enumerate(encoded):
        base_word = mapping[id_num]
        
        # Restore case
        if i < len(case_info):
            word = case_info[i]
        else:
            word = base_word
        
        # Add punctuation
        if i < len(punctuation_info) and punctuation_info[i]:
            word += punctuation_info[i]
        
        words.append(word)
    
    return ' '.join(words)

def analyze_compression(sentence, encoded, mapping):
    """
    Analyze the compression efficiency and provide statistics.
    
    Args:
        sentence (str): Original sentence
        encoded (list): Encoded sequence
        mapping (dict): Word mapping
    """
    print("COMPRESSION ANALYSIS")
    print("=" * 40)
    
    original_length = len(sentence)
    unique_words = len(mapping)
    total_words = len(encoded)
    
    # Calculate compression ratio
    # Assuming each character = 1 byte, each integer = 4 bytes
    original_bytes = original_length
    compressed_bytes = len(encoded) * 4 + sum(len(word) for word in mapping.values())
    compression_ratio = original_bytes / compressed_bytes if compressed_bytes > 0 else float('inf')
    
    print(f"Original sentence: '{sentence}'")
    print(f"Original length: {original_length} characters")
    print(f"Total words: {total_words}")
    print(f"Unique words: {unique_words}")
    print(f"Compression ratio: {compression_ratio:.2f}")
    print(f"Space saved: {original_bytes - compressed_bytes} bytes")
    
    # Word frequency analysis
    word_freq = {}
    for word_id in encoded:
        word = mapping[word_id]
        word_freq[word] = word_freq.get(word, 0) + 1
    
    print(f"\nWord frequencies:")
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print(f"  '{word}': {freq} times")

def batch_compress(sentences):
    """
    Compress multiple sentences using a shared vocabulary.
    
    Args:
        sentences (list): List of sentences to compress
        
    Returns:
        tuple: (encoded_sentences, shared_mapping)
    """
    word_to_id = {}
    id_to_word = {}
    next_id = 1
    encoded_sentences = []
    
    for sentence in sentences:
        words = sentence.lower().split()
        cleaned_words = [re.sub(r'[^\w]', '', word) for word in words if re.sub(r'[^\w]', '', word)]
        
        encoded = []
        for word in cleaned_words:
            if word not in word_to_id:
                word_to_id[word] = next_id
                id_to_word[next_id] = word
                next_id += 1
            encoded.append(word_to_id[word])
        
        encoded_sentences.append(encoded)
    
    return encoded_sentences, id_to_word

def test_sentence_compression():
    """Test the sentence compression with the provided example"""
    
    print("SENTENCE COMPRESSION TEST")
    print("=" * 50)
    
    # Test case from the problem
    sentence = 'the cat sat on the mat'
    expected_encoded = [1, 2, 3, 4, 1, 5]
    expected_mapping = {1: 'the', 2: 'cat', 3: 'sat', 4: 'on', 5: 'mat'}
    
    print(f"Input: '{sentence}'")
    print(f"Expected encoded: {expected_encoded}")
    print(f"Expected mapping: {expected_mapping}")
    
    # Test compression
    encoded, mapping = compress_sentence(sentence)
    
    print(f"\nResult encoded: {encoded}")
    print(f"Result mapping: {mapping}")
    
    # Verify results
    encoded_match = encoded == expected_encoded
    mapping_match = mapping == expected_mapping
    
    print(f"\nEncoded matches: {encoded_match}")
    print(f"Mapping matches: {mapping_match}")
    print(f"Overall test: {'PASS' if encoded_match and mapping_match else 'FAIL'}")
    
    # Test decompression
    decompressed = decompress_sentence(encoded, mapping)
    print(f"\nDecompressed: '{decompressed}'")
    print(f"Decompression correct: {decompressed == sentence}")
    
    # Analysis
    print("\n")
    analyze_compression(sentence, encoded, mapping)
    
    return encoded, mapping

def run_comprehensive_tests():
    """Run comprehensive test cases"""
    
    print("\n" + "=" * 60)
    print("COMPREHENSIVE TEST CASES")
    print("=" * 60)
    
    test_cases = [
        {
            'name': 'Basic compression',
            'input': 'the cat sat on the mat',
            'expected_encoded': [1, 2, 3, 4, 1, 5],
            'expected_mapping': {1: 'the', 2: 'cat', 3: 'sat', 4: 'on', 5: 'mat'}
        },
        {
            'name': 'No repeated words',
            'input': 'hello world python',
            'expected_encoded': [1, 2, 3],
            'expected_mapping': {1: 'hello', 2: 'world', 3: 'python'}
        },
        {
            'name': 'All same word',
            'input': 'test test test',
            'expected_encoded': [1, 1, 1],
            'expected_mapping': {1: 'test'}
        },
        {
            'name': 'Single word',
            'input': 'hello',
            'expected_encoded': [1],
            'expected_mapping': {1: 'hello'}
        },
        {
            'name': 'With punctuation',
            'input': 'hello, world! how are you?',
            'expected_encoded': [1, 2, 3, 4, 5],
            'expected_mapping': {1: 'hello', 2: 'world', 3: 'how', 4: 'are', 5: 'you'}
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {test['name']}")
        print(f"Input: '{test['input']}'")
        
        encoded, mapping = compress_sentence(test['input'])
        
        print(f"Result encoded: {encoded}")
        print(f"Result mapping: {mapping}")
        print(f"Expected encoded: {test['expected_encoded']}")
        print(f"Expected mapping: {test['expected_mapping']}")
        
        encoded_match = encoded == test['expected_encoded']
        mapping_match = mapping == test['expected_mapping']
        
        print(f"Status: {'PASS' if encoded_match and mapping_match else 'FAIL'}")
        
        # Test round-trip compression/decompression
        decompressed = decompress_sentence(encoded, mapping)
        original_cleaned = ' '.join([re.sub(r'[^\w]', '', word).lower() 
                                   for word in test['input'].split() 
                                   if re.sub(r'[^\w]', '', word)])
        
        print(f"Round-trip test: {'PASS' if decompressed == original_cleaned else 'FAIL'}")

def demonstrate_advanced_features():
    """Demonstrate advanced compression features"""
    
    print("\n" + "=" * 50)
    print("ADVANCED FEATURES DEMO")
    print("=" * 50)
    
    # Case-preserving compression
    print("\n1. Case-Preserving Compression:")
    sentence = "The Quick Brown Fox jumps over THE lazy dog."
    encoded, mapping, case_info, punct_info = compress_sentence_preserve_case(sentence)
    
    print(f"Original: '{sentence}'")
    print(f"Encoded: {encoded}")
    print(f"Mapping: {mapping}")
    print(f"Case info: {case_info}")
    print(f"Punctuation: {punct_info}")
    
    restored = decompress_sentence_with_case(encoded, mapping, case_info, punct_info)
    print(f"Restored: '{restored}'")
    
    # Batch compression
    print("\n2. Batch Compression:")
    sentences = [
        "the cat sat on the mat",
        "the dog ran in the park", 
        "a cat and a dog played together"
    ]
    
    print("Input sentences:")
    for i, s in enumerate(sentences, 1):
        print(f"  {i}. '{s}'")
    
    encoded_batch, shared_mapping = batch_compress(sentences)
    
    print(f"\nShared mapping: {shared_mapping}")
    print("Encoded sentences:")
    for i, encoded in enumerate(encoded_batch, 1):
        print(f"  {i}. {encoded}")
    
    # Show compression efficiency
    print(f"\nVocabulary size: {len(shared_mapping)} unique words")
    total_words = sum(len(encoded) for encoded in encoded_batch)
    print(f"Total word instances: {total_words}")
    print(f"Compression efficiency: {len(shared_mapping)/total_words:.2%} unique words")

def interactive_compression_tool():
    """Interactive tool for sentence compression"""
    
    print("\n" + "=" * 50)
    print("INTERACTIVE COMPRESSION TOOL")
    print("=" * 50)
    
    # Demo with user-like interaction
    demo_sentences = [
        "Python is a great programming language",
        "Machine learning with Python is powerful",
        "Data science uses Python extensively",
        "Python Python Python everywhere!"
    ]
    
    print("Compressing sample sentences:")
    
    for i, sentence in enumerate(demo_sentences, 1):
        print(f"\nSentence {i}: '{sentence}'")
        encoded, mapping = compress_sentence(sentence)
        decompressed = decompress_sentence(encoded, mapping)
        
        print(f"  Encoded: {encoded}")
        print(f"  Mapping: {mapping}")
        print(f"  Decompressed: '{decompressed}'")
        print(f"  Vocabulary size: {len(mapping)}")
        print(f"  Compression ratio: {len(sentence.split())}/{len(mapping)} = {len(sentence.split())/len(mapping):.2f}")

if __name__ == "__main__":
    # Run main test
    test_sentence_compression()
    
    # Run comprehensive tests
    run_comprehensive_tests()
    
    # Demonstrate advanced features
    demonstrate_advanced_features()
    
    # Interactive tool
    interactive_compression_tool()
    
    # Performance demonstration
    print("\n" + "=" * 50)
    print("PERFORMANCE DEMONSTRATION")
    print("=" * 50)
    
    # Large text compression
    large_text = ("the quick brown fox jumps over the lazy dog " * 10 + 
                  "python is great for data science and machine learning " * 8 +
                  "compression algorithms help reduce storage space " * 6)
    
    print(f"Large text sample ({len(large_text)} characters):")
    print(f"'{large_text[:100]}...'")
    
    encoded_large, mapping_large = compress_sentence(large_text)
    
    print(f"\nCompression results:")
    print(f"  Original words: {len(large_text.split())}")
    print(f"  Unique words: {len(mapping_large)}")
    print(f"  Encoded length: {len(encoded_large)}")
    print(f"  Vocabulary: {list(mapping_large.values())}")
    
    # Verify large text compression
    decompressed_large = decompress_sentence(encoded_large, mapping_large)
    original_cleaned = ' '.join([re.sub(r'[^\w]', '', word).lower() 
                                for word in large_text.split() 
                                if re.sub(r'[^\w]', '', word)])
    
    print(f"  Large text round-trip: {'SUCCESS' if decompressed_large == original_cleaned else 'FAILED'}")
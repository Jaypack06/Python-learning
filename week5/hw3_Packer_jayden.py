import re

# Part 1: Advanced String Methods 

def format_receipt(items, prices, quantities):
    
    if not items or not prices or not quantities:
        return ""
    
    lines = []
    separator = "=" * 40
    
    # Header
    lines.append(separator)
    lines.append(f"{'Item':<20} {'Qty':^5} {'Price':>8}")
    lines.append(separator)
    
    total = 0.0
    
    # Items
    for item, price, qty in zip(items, prices, quantities):
        line_total = price * qty
        total += line_total
        lines.append(f"{item:<20} {qty:^5} ${line_total:>7.2f}")
    
    # Footer
    lines.append(separator)
    lines.append(f"{'TOTAL':<26} ${total:>7.2f}")
    lines.append(separator)
    
    return "\n".join(lines)


def process_user_data(raw_data):
    
    result = {}
    
    # Clean name
    name = raw_data.get('name', '').strip()
    result['name'] = ' '.join(word.capitalize() for word in name.split())
    
    # Clean email
    email = raw_data.get('email', '').replace(' ', '').lower()
    result['email'] = email
    
    # Clean phone (digits only)
    phone = raw_data.get('phone', '')
    result['phone'] = ''.join(c for c in phone if c.isdigit())
    
    # Clean address
    address = raw_data.get('address', '').strip()
    result['address'] = ' '.join(word.capitalize() for word in address.split())
    
    # Generate username
    name_parts = result['name'].split()
    if len(name_parts) >= 2:
        result['username'] = f"{name_parts[0].lower()}_{name_parts[1].lower()}"
    else:
        result['username'] = name_parts[0].lower() if name_parts else ""
    
    # Basic validation
    result['validation'] = {
        'name_valid': len(result['name']) > 0,
        'email_valid': '@' in result['email'] and '.' in result['email'],
        'phone_valid': len(result['phone']) >= 10,
        'address_valid': len(result['address']) > 0
    }
    
    return result


def analyze_text(text):
    
    if not text:
        return {
            'total_chars': 0, 'total_words': 0, 'total_lines': 0,
            'avg_word_length': 0.0, 'most_common_word': '',
            'longest_line': '', 'words_per_line': [],
            'capitalized_sentences': 0, 'questions': 0, 'exclamations': 0
        }
    
    lines = text.split('\n')
    all_words = []
    words_per_line = []
    
    for line in lines:
        words = line.split()
        words_per_line.append(len(words))
        all_words.extend([word.lower().strip('.,!?;:"()[]') for word in words])
    
    # Find longest line
    longest_line = max(lines, key=len) if lines else ""
    
    # Most common word 
    word_counts = {}
    for word in all_words:
        if word:
            word_counts[word] = word_counts.get(word, 0) + 1
    
    most_common_word = ""
    max_count = 0
    for word, count in word_counts.items():
        if count > max_count:
            max_count = count
            most_common_word = word
    
    # Average word length
    clean_words = [word for word in all_words if word]
    avg_word_length = sum(len(word) for word in clean_words) / len(clean_words) if clean_words else 0.0
    
    # Sentence analysis
    sentences = text.replace('!', '.').replace('?', '.').split('.')
    capitalized_sentences = sum(1 for s in sentences if s.strip() and s.strip()[0].isupper())
    questions = text.count('?')
    exclamations = text.count('!')
    
    return {
        'total_chars': len(text),
        'total_words': len(clean_words),
        'total_lines': len(lines),
        'avg_word_length': round(avg_word_length, 2),
        'most_common_word': most_common_word,
        'longest_line': longest_line,
        'words_per_line': words_per_line,
        'capitalized_sentences': capitalized_sentences,
        'questions': questions,
        'exclamations': exclamations
    }

# Part 2: Introduction to Regular Expressions

def find_patterns(text):
   
    patterns = {
        'integers': r'\b\d+\b',  
        'decimals': r'\b\d+\.\d+\b',  
        'words_with_digits': r'\b\w*\d+\w*\b',  
        'capitalized_words': r'\b[A-Z][a-z]*\b',  
        'all_caps_words': r'\b[A-Z]{2,}\b',  
        'repeated_chars': r'\b\w*([a-zA-Z])\1+\w*\b'  
    }
    
    result = {}
    for pattern_name, pattern in patterns.items():
        if pattern_name == 'repeated_chars':
            
            matches = re.findall(r'\b\w*[a-zA-Z]{2,}\w*\b', text)
            result[pattern_name] = [word for word in matches 
                                  if any(word[i] == word[i+1] for i in range(len(word)-1) 
                                        if word[i].isalpha())]
        else:
            result[pattern_name] = re.findall(pattern, text)
    
    return result


def validate_format(input_string, format_type):
    
    patterns = {
        
        'phone': r'^\(?(\d{3})\)?\s?-?(\d{3})-?(\d{4})$',
        
        'date': r'^(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/(\d{4})$',
        
        'time': r'^(0?\d|1[0-2]):([0-5]\d)\s?(AM|PM)$|^([01]?\d|2[0-3]):([0-5]\d)$',
        
        'email': r'^([a-zA-Z0-9._%-]+)@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})$',
        
        'url': r'^https?://([a-zA-Z0-9.-]+\.[a-zA-Z]{2,}).*$',
        
        'ssn': r'^(\d{3})-(\d{2})-(\d{4})$'
    }
    
    pattern = patterns.get(format_type)
    if not pattern:
        return (False, None)
    
    match = re.match(pattern, input_string)
    if not match:
        return (False, None)
    
    # Extract parts based on format type
    parts = {}
    if format_type == 'phone':
        parts = {'area_code': match.group(1), 'prefix': match.group(2), 'line': match.group(3)}
    elif format_type == 'date':
        month, day, year = int(match.group(1)), int(match.group(2)), int(match.group(3))
        
        if month > 12 or day > 31:
            return (False, None)
        parts = {'month': match.group(1), 'day': match.group(2), 'year': match.group(3)}
    elif format_type == 'time':
        if match.group(3):  
            parts = {'hour': match.group(1), 'minute': match.group(2), 'period': match.group(3)}
        else:  
            parts = {'hour': match.group(4), 'minute': match.group(5)}
    elif format_type == 'email':
        parts = {'username': match.group(1), 'domain': match.group(2), 'extension': match.group(3)}
    elif format_type == 'url':
        parts = {'domain': match.group(1)}
    elif format_type == 'ssn':
        parts = {'area': match.group(1), 'group': match.group(2), 'serial': match.group(3)}
    
    return (True, parts)


def extract_information(text):
    
    result = {}
    
    # Prices
    result['prices'] = re.findall(r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?', text)
    
    # Percentages
    result['percentages'] = re.findall(r'\d+(?:\.\d+)?%', text)
    
    # Years
    result['years'] = re.findall(r'\b(19|20)\d{2}\b', text)
    
    # Sentences
    sentences = re.split(r'[.!?]+', text)
    result['sentences'] = [s.strip() for s in sentences if s.strip()]
    
    # Questions
    questions = re.findall(r'[^.!?]*\?', text)
    result['questions'] = [q.strip() + '?' for q in questions if q.strip()]
    
    # Quoted text
    result['quoted_text'] = re.findall(r'"([^"]*)"', text)
    
    return result
# Part 3: Combining String Methods and Regex 
def clean_text_pipeline(text, operations):
    
    result = {
        'original': text,
        'cleaned': text,
        'steps': []
    }
    
    current_text = text
    
    for operation in operations:
        if operation == 'trim':
            # Remove whitespace
            current_text = current_text.strip()
        elif operation == 'lowercase':
            # lowercase
            current_text = current_text.lower()
        elif operation == 'remove_punctuation':
            # Remove all punctuation
            current_text = re.sub(r'[^\w\s]', '', current_text)
        elif operation == 'remove_digits':
            # Remove all digits
            current_text = re.sub(r'\d', '', current_text)
        elif operation == 'remove_extra_spaces':
            # Replace multiple spaces with single space
            current_text = re.sub(r'\s+', ' ', current_text)
        elif operation == 'remove_urls':
            # Remove URLs starting with http/https
            current_text = re.sub(r'https?://\S+', '', current_text)
        elif operation == 'remove_emails':
            # Remove email
            current_text = re.sub(r'\S+@\S+', '', current_text)
        elif operation == 'capitalize_sentences':
            # Capitalize first letter of sentences
            sentences = current_text.split('. ')
            sentences = [s.capitalize() for s in sentences]
            current_text = '. '.join(sentences)
        
        result['steps'].append(current_text)
    
    result['cleaned'] = current_text
    return result


def smart_replace(text, replacements):
    
    # Contractions dictionary
    contractions = {
        "don't": "do not", "won't": "will not", "can't": "cannot",
        "I'm": "I am", "you're": "you are", "it's": "it is",
        "he's": "he is", "she's": "she is", "we're": "we are",
        "they're": "they are", "I've": "I have", "you've": "you have",
        "we've": "we have", "they've": "they have"
    }
    
    # Number to word mapping
    number_words = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    
    result = text
    
    if replacements.get('censor_phone'):
        
        result = re.sub(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', 'XXX-XXX-XXXX', result)
        result = re.sub(r'\(\d{3}\)\s?\d{3}-\d{4}', 'XXX-XXX-XXXX', result)
    
    if replacements.get('censor_email'):
        
        result = re.sub(r'\S+@\S+', '[EMAIL]', result)
    
    if replacements.get('fix_spacing'):
        result = re.sub(r'\s*([,.!?;:])\s*', r'\1 ', result)
        result = re.sub(r'\s+', ' ', result).strip()
    
    if replacements.get('expand_contractions'):
        for contraction, expansion in contractions.items():
            result = re.sub(r'\b' + re.escape(contraction) + r'\b', expansion, result, flags=re.IGNORECASE)
    
    if replacements.get('number_to_word'):
        for digit, word in number_words.items():
            result = re.sub(r'\b' + digit + r'\b', word, result)
    
    return result


# Part 4: Practical Application  

def analyze_log_file(log_text):
    
    if not log_text.strip():
        return {
            'total_entries': 0, 'error_count': 0, 'warning_count': 0,
            'info_count': 0, 'dates': [], 'error_messages': [],
            'time_range': (None, None), 'most_active_hour': None
        }
    
    lines = log_text.strip().split('\n')
    
    
    log_pattern = r'\[(\d{4}-\d{2}-\d{2}) (\d{2}):(\d{2}):(\d{2})\] (\w+): (.+)'
    
    total_entries = 0
    error_count = warning_count = info_count = 0
    dates = set()
    error_messages = []
    times = []
    hours = []
    
    for line in lines:
        match = re.match(log_pattern, line.strip())
        if match:
            total_entries += 1
            date, hour, minute, second, level, message = match.groups()
            
            dates.add(date)
            times.append(f"{hour}:{minute}:{second}")
            hours.append(int(hour))
            
            if level == 'ERROR':
                error_count += 1
                error_messages.append(message)
            elif level == 'WARNING':
                warning_count += 1
            elif level == 'INFO':
                info_count += 1
    
    
    time_range = (min(times), max(times)) if times else (None, None)
    
    
    hour_counts = {}
    for hour in hours:
        hour_counts[hour] = hour_counts.get(hour, 0) + 1
    
    most_active_hour = None
    max_count = 0
    for hour, count in hour_counts.items():
        if count > max_count:
            max_count = count
            most_active_hour = hour
    
    return {
        'total_entries': total_entries,
        'error_count': error_count,
        'warning_count': warning_count,
        'info_count': info_count,
        'dates': sorted(list(dates)),
        'error_messages': error_messages,
        'time_range': time_range,
        'most_active_hour': most_active_hour
    }
# Testing Code

def run_tests():
    
    print("="*50)
    print("Testing Part 1: String Methods")
    print("="*50)
    
    # Test 1.1: Receipt formatting
    items = ["Coffee", "Sandwich"]
    prices = [3.50, 8.99]
    quantities = [2, 1]
    receipt = format_receipt(items, prices, quantities)
    print("Receipt Test:")
    print(receipt)
    
    # Test 1.2: User data processing
    test_data = {
        'name': ' john DOE ',
        'email': ' JOHN@EXAMPLE.COM ',
        'phone': '(555) 123-4567',
        'address': '123 main street'
    }
    cleaned = process_user_data(test_data)
    print(f"\nCleaned name: {cleaned.get('name', 'ERROR')}")
    print(f"Cleaned email: {cleaned.get('email', 'ERROR')}")
    
    print("\n" + "="*50)
    print("Testing Part 2: Regular Expressions")
    print("="*50)
    
    # Test 2.1: Pattern finding
    test_text = "I have 25 apples and 3.14 pies"
    patterns = find_patterns(test_text)
    print(f"Found integers: {patterns.get('integers', [])}")
    print(f"Found decimals: {patterns.get('decimals', [])}")
    
    # Test 2.2: Format validation
    phone_valid, phone_parts = validate_format("(555) 123-4567", "phone")
    print(f"\nPhone validation: {phone_valid}")
    if phone_parts:
        print(f"Extracted parts: {phone_parts}")
    
    # Test 2.3: Information extraction
    info_text = 'The price is $19.99 (20% off).'
    info = extract_information(info_text)
    print(f"\nPrices found: {info.get('prices', [])}")
    print(f"Percentages found: {info.get('percentages', [])}")
    
    print("\n" + "="*50)
    print("Testing Part 3: Combined Operations")
    print("="*50)
    
    # Test 3.1: Cleaning pipeline
    dirty_text = " Hello WORLD! "
    operations = ['trim', 'lowercase', 'remove_extra_spaces']
    cleaned_result = clean_text_pipeline(dirty_text, operations)
    print(f"Original: '{cleaned_result.get('original', '')}'")
    print(f"Cleaned: '{cleaned_result.get('cleaned', '')}'")
    
    print("\n" + "="*50)
    print("Testing Part 4: Log Analysis")
    print("="*50)
    
    # Test 4.1: Log analysis
    sample_log = """[2024-01-15 10:30:45] ERROR: Connection failed
[2024-01-15 10:31:00] INFO: Retry attempt
[2024-01-15 10:32:00] WARNING: Timeout warning"""
    log_analysis = analyze_log_file(sample_log)
    print(f"Total entries: {log_analysis.get('total_entries', 0)}")
    print(f"Error count: {log_analysis.get('error_count', 0)}")
    print(f"Unique dates: {log_analysis.get('dates', [])}")
    
    print("\n" + "="*50)
    print("All tests completed!")
    print("="*50)


if __name__ == "__main__":
    run_tests()
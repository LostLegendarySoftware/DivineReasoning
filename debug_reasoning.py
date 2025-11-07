# debug_reasoning.py
import sys
import time

print("🐛 DEBUG MODE ACTIVATED")

class DebugReasoner:
    def __init__(self):
        print("🔧 INITIALIZING DEBUG REASONER...")
        self.debug_log = []
        
    def log(self, message):
        print(f"   📝 DEBUG: {message}")
        self.debug_log.append(message)
        
    def analyze_question(self, question):
        self.log(f"Analyzing question: '{question}'")
        
        # Show exact string analysis
        words = question.lower().split()
        self.log(f"Words detected: {words}")
        
        # Question type analysis
        q_types = {
            'who': 'information_seeking',
            'what': 'information_seeking', 
            'where': 'information_seeking',
            'when': 'information_seeking',
            'why': 'causal_seeking',
            'how': 'process_seeking',
            'should': 'advice_seeking',
            'can': 'capability_seeking',
            'would': 'hypothetical_seeking'
        }
        
        detected_types = []
        for word in words:
            if word in q_types:
                detected_types.append(q_types[word])
                self.log(f"Found question word '{word}' -> {q_types[word]}")
                
        q_type = detected_types[0] if detected_types else 'general_inquiry'
        self.log(f"Question type: {q_type}")
        
        # Domain detection
        domain_keywords = {
            'math': 'mathematical',
            'calculate': 'mathematical', 
            'number': 'mathematical',
            'time': 'temporal',
            'when': 'temporal',
            'before': 'temporal',
            'after': 'temporal',
            'space': 'spatial',
            'where': 'spatial',
            'location': 'spatial',
            'cause': 'causal',
            'effect': 'causal',
            'because': 'causal',
            'why': 'causal',
            'should': 'ethical',
            'ethical': 'ethical',
            'moral': 'ethical'
        }
        
        domains_involved = []
        for word in words:
            if word in domain_keywords:
                domain = domain_keywords[word]
                if domain not in domains_involved:
                    domains_involved.append(domain)
                    self.log(f"Found domain keyword '{word}' -> {domain}")
                    
        if not domains_involved:
            domains_involved = ['logical', 'practical']
            self.log(f"No specific domains detected, using default: {domains_involved}")
            
        return {
            'type': q_type,
            'domains': domains_involved,
            'complexity': len(words) / 10.0
        }
    
    def mathematical_reasoning(self, question):
        self.log("Starting mathematical reasoning...")
        words = question.split()
        numbers_found = []
        operations_found = []
        
        for i, word in enumerate(words):
            # Try to convert to number
            try:
                num = float(word)
                numbers_found.append(num)
                self.log(f"Found number: {num}")
            except ValueError:
                # Check for operation words
                if word in ['plus', '+', 'and', 'add']:
                    operations_found.append('+')
                    self.log("Found addition operation")
                elif word in ['minus', '-', 'subtract']:
                    operations_found.append('-')
                    self.log("Found subtraction operation")
                elif word in ['times', 'x', '*', 'multiply']:
                    operations_found.append('*') 
                    self.log("Found multiplication operation")
                elif word in ['divided', '/', 'divide']:
                    operations_found.append('/')
                    self.log("Found division operation")
                    
        self.log(f"Numbers found: {numbers_found}")
        self.log(f"Operations found: {operations_found}")
        
        # Try to perform calculation
        if len(numbers_found) >= 2 and operations_found:
            try:
                if operations_found[0] == '+':
                    result = numbers_found[0] + numbers_found[1]
                    response = f"Mathematical calculation: {numbers_found[0]} + {numbers_found[1]} = {result}"
                elif operations_found[0] == '-':
                    result = numbers_found[0] - numbers_found[1]
                    response = f"Mathematical calculation: {numbers_found[0]} - {numbers_found[1]} = {result}"
                elif operations_found[0] == '*':
                    result = numbers_found[0] * numbers_found[1]
                    response = f"Mathematical calculation: {numbers_found[0]} × {numbers_found[1]} = {result}"
                elif operations_found[0] == '/':
                    if numbers_found[1] != 0:
                        result = numbers_found[0] / numbers_found[1]
                        response = f"Mathematical calculation: {numbers_found[0]} ÷ {numbers_found[1]} = {result}"
                    else:
                        response = "Mathematical analysis: Division by zero is undefined"
                self.log(f"Calculation result: {response}")
                return response
            except Exception as e:
                self.log(f"Calculation error: {e}")
                
        return "Mathematical analysis: Insufficient data for calculation"
    
    def process_question(self, question):
        print(f"\n🎯 PROCESSING QUESTION: '{question}'")
        print("🔍 STEP-BY-STEP ANALYSIS:")
        
        # Step 1: Analyze question
        analysis = self.analyze_question(question)
        print(f"   📊 FINAL ANALYSIS: {analysis}")
        
        # Step 2: Apply reasoning based on domains
        print("   🧠 APPLYING REASONING:")
        for domain in analysis['domains']:
            print(f"      - {domain.upper()} reasoning...")
            if domain == 'mathematical':
                result = self.mathematical_reasoning(question)
                print(f"      ↳ RESULT: {result}")
                return result
            elif domain == 'logical':
                result = "Logical analysis: Applied deductive reasoning to evaluate the proposition"
                print(f"      ↳ RESULT: {result}")
                return result
            elif domain == 'temporal':
                result = "Temporal analysis: Evaluated time-based relationships in the query"
                print(f"      ↳ RESULT: {result}")
                return result
            elif domain == 'causal':
                result = "Causal analysis: Identified potential cause-effect relationships"
                print(f"      ↳ RESULT: {result}")
                return result
            else:
                result = f"General analysis: Processed through {domain} reasoning domain"
                print(f"      ↳ RESULT: {result}")
                return result

def test_specific_questions():
    """Test the system with specific questions to see exactly what's happening"""
    reasoner = DebugReasoner()
    
    test_cases = [
        "What is 15 plus 27?",
        "Can you calculate 100 minus 45?",
        "Should I learn Python?",
        "Why is the sky blue?",
        "How do I build an AI?",
        "2 + 2",
        "simple math test"
    ]
    
    print("\n" + "="*60)
    print("🧪 TEST SUITE RUNNING")
    print("="*60)
    
    for i, question in enumerate(test_cases, 1):
        print(f"\n{'='*20} TEST {i} {'='*20}")
        print(f"INPUT: {question}")
        result = reasoner.process_question(question)
        print(f"FINAL OUTPUT: {result}")
        time.sleep(1)

def interactive_debug():
    """Interactive mode for testing your own questions"""
    reasoner = DebugReasoner()
    
    print("\n" + "="*60)
    print("🔍 INTERACTIVE DEBUG MODE")
    print("   Enter questions to see detailed reasoning process")
    print("   Type 'exit' to quit")
    print("="*60)
    
    while True:
        question = input("\n🤔 YOUR QUESTION: ").strip()
        
        if question.lower() in ['exit', 'quit']:
            break
            
        if not question:
            print("   Please enter a question")
            continue
            
        result = reasoner.process_question(question)
        print(f"\n💡 FINAL ANSWER: {result}")

# Choose mode
if __name__ == "__main__":
    print("Select mode:")
    print("1 - Run test suite")
    print("2 - Interactive debug")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        test_specific_questions()
    else:
        interactive_debug()

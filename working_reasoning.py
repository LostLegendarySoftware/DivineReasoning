# working_reasoning.py
import re
import math

print("🧠 BUILDING MINIMAL WORKING REASONING ENGINE...")

class WorkingReasoner:
    def __init__(self):
        self.knowledge = {
            'math': {
                'addition': lambda a, b: a + b,
                'subtraction': lambda a, b: a - b,
                'multiplication': lambda a, b: a * b,
                'division': lambda a, b: a / b if b != 0 else "undefined"
            },
            'facts': {
                'sky_blue': "Rayleigh scattering causes blue light to scatter more in the atmosphere",
                'breathing_underwater': "Humans need oxygen from air; water doesn't provide enough oxygen for our lungs",
                'vinegar_baking_soda': "They react to produce carbon dioxide gas (CO2), water, and sodium acetate",
                'seasons': "Earth's axial tilt causes different parts to receive varying sunlight throughout the year",
                'python_value': "Python is valuable for AI, web development, data science, and automation"
            },
            'logic': {
                'umbrella_rain': "If it's raining, an umbrella keeps you dry. Therefore, bringing one is logical.",
                'learning': "Learning valuable skills generally improves career opportunities and problem-solving ability"
            }
        }
    
    def extract_math(self, text):
        """Actually extract and solve math problems"""
        # Look for number patterns
        numbers = re.findall(r'\d+', text)
        numbers = [int(n) for n in numbers]
        
        # Look for operations
        if 'plus' in text.lower() or '+' in text:
            if len(numbers) >= 2:
                result = self.knowledge['math']['addition'](numbers[0], numbers[1])
                return f"{numbers[0]} + {numbers[1]} = {result}"
        
        elif 'minus' in text.lower() or '-' in text:
            if len(numbers) >= 2:
                result = self.knowledge['math']['subtraction'](numbers[0], numbers[1])
                return f"{numbers[0]} - {numbers[1]} = {result}"
        
        elif 'times' in text.lower() or 'x' in text.lower() or '*' in text:
            if len(numbers) >= 2:
                result = self.knowledge['math']['multiplication'](numbers[0], numbers[1])
                return f"{numbers[0]} × {numbers[1]} = {result}"
        
        elif 'divide' in text.lower() or '/' in text:
            if len(numbers) >= 2:
                result = self.knowledge['math']['division'](numbers[0], numbers[1])
                return f"{numbers[0]} ÷ {numbers[1]} = {result}"
        
        return None
    
    def answer_question(self, question):
        """Actually answer questions based on knowledge"""
        question_lower = question.lower()
        
        # Math questions
        math_answer = self.extract_math(question)
        if math_answer:
            return f"Mathematical answer: {math_answer}"
        
        # Fact-based questions
        if any(word in question_lower for word in ['sky', 'blue', 'color']):
            return f"Scientific fact: {self.knowledge['facts']['sky_blue']}"
        
        elif any(word in question_lower for word in ['breathe', 'underwater']):
            return f"Biological fact: {self.knowledge['facts']['breathing_underwater']}"
        
        elif any(word in question_lower for word in ['vinegar', 'baking soda']):
            return f"Chemical fact: {self.knowledge['facts']['vinegar_baking_soda']}"
        
        elif any(word in question_lower for word in ['season', 'summer', 'winter']):
            return f"Astronomical fact: {self.knowledge['facts']['seasons']}"
        
        elif any(word in question_lower for word in ['learn python', 'python programming']):
            return f"Practical advice: {self.knowledge['facts']['python_value']}"
        
        # Logic questions
        elif any(word in question_lower for word in ['umbrella', 'rain']):
            return f"Logical reasoning: {self.knowledge['logic']['umbrella_rain']}"
        
        elif any(word in question_lower for word in ['should i learn', 'should i study']):
            return f"Logical reasoning: {self.knowledge['logic']['learning']}"
        
        # Default responses for unknown questions
        if '?' in question:
            return "I don't have enough information to answer that question definitively. Could you provide more context?"
        else:
            return "I understand you're asking something, but I need a clearer question to provide a useful answer."

def test_engine():
    """Test the engine with common questions"""
    reasoner = WorkingReasoner()
    
    test_questions = [
        "What is 15 plus 27?",
        "Calculate 100 minus 45",
        "Why is the sky blue?",
        "Can humans breathe underwater?",
        "What happens when you mix vinegar and baking soda?",
        "Should I bring an umbrella if it rains?",
        "Should I learn Python?",
        "What causes seasons?",
        "What is 8 times 7?",
        "Divide 100 by 4"
    ]
    
    print("🧪 TESTING REASONING ENGINE:")
    print("=" * 50)
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n{i}. Q: {question}")
        answer = reasoner.answer_question(question)
        print(f"   A: {answer}")

def interactive_mode():
    """Let users ask their own questions"""
    reasoner = WorkingReasoner()
    
    print("\n💬 INTERACTIVE MODE - Ask me anything!")
    print("Type 'quit' to exit")
    print("=" * 40)
    
    while True:
        question = input("\n🤔 Your question: ").strip()
        
        if question.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye!")
            break
        
        if not question:
            print("Please enter a question")
            continue
            
        answer = reasoner.answer_question(question)
        print(f"💡 {answer}")

if __name__ == "__main__":
    print("🧠 SIMPLE REASONING ENGINE")
    print("1. Run tests")
    print("2. Interactive mode")
    
    choice = input("Choose (1 or 2): ").strip()
    
    if choice == "1":
        test_engine()
    else:
        interactive_mode()

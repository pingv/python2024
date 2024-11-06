import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import textwrap
import gc

class InterviewAssistant:
    def __init__(self):
        self.model_name = "google/flan-t5-small"
        print("Loading model and tokenizer...")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
        self.conversation_history = []
        print("Model loaded successfully!")

    def get_relevant_follow_up(self, response_text):
        """
        Determine relevant follow-up areas based on the response
        """
        response_lower = response_text.lower()
        
        # Define follow-up areas based on keywords
        follow_ups = {
            'technical_skills': any(word in response_lower for word in ['developer', 'react', 'node.js', 'programming', 'code']),
            'leadership': any(word in response_lower for word in ['led', 'team', 'managed', 'coordinated']),
            'project_details': any(word in response_lower for word in ['project', 'portal', 'built', 'developed']),
            'experience': any(word in response_lower for word in ['years', 'experience', 'working'])
        }
        
        # Get the most relevant follow-up area
        relevant_areas = [area for area, present in follow_ups.items() if present]
        return relevant_areas[0] if relevant_areas else 'general'

    def get_follow_up_template(self, area):
        """
        Get specific follow-up question templates based on the area
        """
        templates = {
            'technical_skills': [
                "Tell me more about the specific technologies you used in the {project}.",
                "What were the most challenging technical problems you solved in the {project}?",
                "How did you ensure code quality and performance in the {project}?"
            ],
            'leadership': [
                "How large was the team you led, and how did you organize the work?",
                "What leadership challenges did you face during the {project}?",
                "How did you handle team collaboration and communication?"
            ],
            'project_details': [
                "What were the key features you implemented in the {project}?",
                "How did this project impact the business?",
                "What was the timeline for completing this project?"
            ],
            'experience': [
                "What have been your biggest learnings in your development career so far?",
                "How has your role evolved over these years?",
                "What kinds of projects do you find most exciting?"
            ],
            'general': [
                "Could you share more about the outcomes of this work?",
                "What aspects of this experience are you most proud of?",
                "How has this experience prepared you for future challenges?"
            ]
        }
        return templates.get(area, templates['general'])

    def generate_follow_up(self, response_text):
        """
        Generate a contextual follow-up interview question
        """
        try:
            # Add to conversation history
            self.conversation_history.append(response_text)
            
            # Identify relevant follow-up area
            area = self.get_relevant_follow_up(response_text)
            
            # Get template questions
            templates = self.get_follow_up_template(area)
            
            # Create a focused prompt
            prompt = f"""
            You are conducting a job interview. The candidate said: "{response_text}"
            
            Generate a natural follow-up interview question that:
            - Builds on the information they just shared
            - Helps understand their experience deeper
            - Is specific and relevant to what they mentioned
            - Encourages them to share more details
            - Sounds like a natural conversation
            
            Do not ask about what they already said. Ask about new details.
            """
            
            # Generate follow-up
            inputs = self.tokenizer(
                prompt,
                return_tensors="pt",
                max_length=256,
                truncation=True
            )

            with torch.no_grad():
                outputs = self.model.generate(
                    inputs.input_ids,
                    max_length=50,
                    temperature=0.7,
                    num_return_sequences=1,
                    do_sample=True,
                    top_p=0.95,
                    top_k=50
                )

            follow_up = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # Validate the generated question
            if not follow_up.endswith('?') or len(follow_up.split()) < 4:
                # Fall back to template if generation is poor
                project = "project" if "project" in response_text.lower() else "work"
                follow_up = templates[0].format(project=project)
            
            # Clean up
            del inputs, outputs
            gc.collect()
            
            return follow_up

        except Exception as e:
            print(f"Error generating follow-up: {str(e)}")
            return "Could you tell me more about the technical challenges you faced?"

def main():
    try:
        assistant = InterviewAssistant()
        
        print("\nInterview Follow-up Question Generator")
        print("=====================================")
        print("Type 'quit' to exit")
        
        while True:
            print("\nEnter the interviewee's response:")
            response = input().strip()
            
            if response.lower() == 'quit':
                break
                
            if not response:
                print("Please enter a valid response.")
                continue
                
            try:
                follow_up = assistant.generate_follow_up(response)
                print("\nSuggested follow-up question:")
                print(textwrap.fill(follow_up, width=70))
                
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                continue
    
    finally:
        if 'assistant' in locals():
            del assistant
        gc.collect()

if __name__ == "__main__":
    main()
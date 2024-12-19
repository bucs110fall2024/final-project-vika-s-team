import requests
import random
import pygame
import html
from src.Text import Text

WHITE = (255, 255, 255)
BLUE = (0,0,255)
LIGHTBLUE = (130,200,255)
BLACK = (0,0,0)
class Play:
    def __init__(self, animal):
        """
        initizalies the trivia screen

        Args:
            animal (Animal): animal object
        """
        self.animal = animal
        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption(f"{self.animal.name}'s Play Time Trivia")
        self.clock = pygame.time.Clock()
        
    def get_questions(self):
        """
        makes an API call and retrieves questions

        Returns:
            str: data string of the trivia questions and answsers from the API
        """
        url = "https://opentdb.com/api.php?amount=10&category=27&difficulty=medium&type=multiple"
        
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["results"]
    
    def get_question(self, question_data):
        """
        formats the questions and stores the answers from a list

        Args:
            question_data (str): list of questions and answers

        Returns:
            questions, answers: one question and answers at a time
        """
        question = html.unescape(question_data["question"])
        correct_answer = html.unescape(question_data["correct_answer"])
        incorrect_answers = question_data["incorrect_answers"]
        
        answers = {
            "correct": correct_answer,
            "incorrect": incorrect_answers
        }
        return question, answers
    
    def display_question(self, question, all_choices):  
        """
        puts the questions and answsers on the screen

        Args:
            question (str): one question
            all_choices (list)): list of all choices
        """
        self.screen.fill(WHITE)             
        message = question
        font = pygame.font.Font(None, 20)
        text_display = font.render(html.unescape(message), True, (BLUE))
        text_rect = text_display.get_rect(center =(300,110))
        self.screen.blit(text_display, text_rect)
            
        counter = 0
        for answer in all_choices:
            answer_button = pygame.Rect(70, 150 + counter * 40, 300, 30)
            pygame.draw.rect(self.screen, (LIGHTBLUE), answer_button)
            answer_text = font.render(answer, True, (BLACK))
            self.screen.blit(answer_text, (80, 150 + counter * 40))
            counter += 1
                
    def display_trivia(self):
        """
        displays the rules and then handles the running of the trivia game
        """
        data = self.get_questions()       
        current_question_index = 0       
        current_question = ''
        current_all_choices=''       
        correct_counter = 0
        self.running = True
        
        self.text = Text(self.screen)
        self.screen.fill(WHITE)
        self.text.print_message(message = "This is a trivia game!", x = 300, y = 80)
        self.text.print_message(message = "To pick a choice, use the number keys 1 - 4", x = 300, y = 100)
        self.text.print_message(message = "Every question you get correct will add an extra coin to your money!", x = 300, y = 120)
        self.text.print_message(message = "Press q to exit the game", x = 300, y = 140)
        self.text.print_message(message = "(This message will automatically disappear)", x = 300, y = 160)
        pygame.display.flip()
        pygame.time.wait(5000) 
        while self.running:         
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    self.running = False 
                elif event.type == pygame.KEYDOWN:
                    if pygame.K_1 <= event.key <= pygame.K_4:
                        chosen_index = event.key - pygame.K_1
                        if all_choices[chosen_index] == answers["correct"]:
                            self.animal.happiness += 10
                            message = f"Correct!" 
                            correct_counter += 1                                           
                        else:
                            self.animal.happiness -= 10
                            message = f"Wrong!"
                                
                        font = pygame.font.Font(None, 20)
                        text_display = font.render(message, True, (0,0,255))
                        text_rect = text_display.get_rect(center =(550,160))
                        self.screen.blit(text_display, text_rect)
                                 
                        text_display = font.render("The answer is " + answers["correct"], True, (BLUE))
                        text_rect = text_display.get_rect(center =(550,200))
                                
                        self.screen.blit(text_display, text_rect)
                        pygame.display.flip() 
                        pygame.time.wait(500) 
                        current_question_index +=1               
                    else:
                        if event.key == pygame.K_RETURN:
                            current_question_index = 0
                                
                if (current_question_index < len(data)) :            
                    question, answers = self.get_question(data[current_question_index])
                    if(question != current_question):
                        all_choices = answers["incorrect"] + [answers ["correct"]]
                        random.shuffle(all_choices)
                        current_question = question
                        current_all_choices = all_choices
                   
                    self.display_question(current_question, current_all_choices)   
                else:
                    self.screen.fill((255, 255, 255))   
                    font = pygame.font.Font(None, 30)
                    text_display = font.render(f"The End. You earned {correct_counter} dollars. Press q to go back to the menu ", True, (BLUE))
                    text_rect = text_display.get_rect(center =(500,160))
                    self.screen.blit(text_display, text_rect)                         

                pygame.display.flip()
        self.animal.money += correct_counter           
                        
                        
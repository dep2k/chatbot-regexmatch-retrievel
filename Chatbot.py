

from nltk.chat.util import Chat
from ChatReflections import ChatReflections
from ChatPairs import ChatPairs

class Chatbot:
    
    __instance = None
     
    @staticmethod 
    def getInstance():
        if Chatbot.__instance == None:
            Chatbot()
        return Chatbot.__instance
    
    
    def __init__(self):
        
         if Chatbot.__instance != None:
             raise Exception("This class is a singleton!")
         else:
            Chatbot.__instance = self
            self.__reflections = ChatReflections().getReflections()
            self.__pairs = ChatPairs().getPairs()
            self.__chat = Chat(self.__pairs, self.__reflections)
         
 
#    def __init__(self):
#        
#        self.__reflections = ChatReflections().getReflections()
#        self.__pairs = ChatPairs().getPairs()
#        self.__chat = Chat(self.__pairs, self.__reflections)
#            
            
    def reply(self, input):
        response = self.__chat.respond(input)
        return response
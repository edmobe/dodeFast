from analyzers.lexical_analyzer import Lexical_Analyzer
from analyzers.syntax_analyzer import Syntax_Analyzer

class Compiler:
    def __init__(self):
        self.lexical_analyzer = Lexical_Analyzer()
        self.syntax_analyzer = Syntax_Analyzer()
    def compile(self, code):
        lexical_analysis = self.lexical_analyzer.analyze(code)
        if (lexical_analysis[0] == 0):
            syntax_analysis = self.syntax_analyzer.analyze(lexical_analysis[1])
            if (syntax_analysis[0] != 0):
                "Syntax error: " + syntax_analysis[1]
            else:
                return syntax_analysis[1]
        else:
            return "Lexical error: " + lexical_analysis[1]